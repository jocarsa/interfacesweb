#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pdf_ocr_json.py

Convierte cada página de un PDF escaneado a imagen, ejecuta OCR con Tesseract
y genera un JSON estructurado en lugar de un TXT plano.

Intenta detectar:
- páginas
- líneas
- bloques de texto
- tablas heurísticas basadas en posiciones OCR
- metadatos básicos

Ejemplo:
    python3 pdf_ocr_json.py --archivo entrada.pdf

Requisitos:
    sudo apt install tesseract-ocr tesseract-ocr-spa poppler-utils
    pip install pdf2image pytesseract pillow
"""

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Tuple

from pdf2image import convert_from_path  # type: ignore
import pytesseract  # type: ignore
from pytesseract import Output  # type: ignore


# --------------------------------------------------
# UTILIDADES
# --------------------------------------------------

def limpiar_texto(texto: str) -> str:
    texto = texto.replace("\x0c", " ")
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n[ \t]+", "\n", texto)
    return texto.strip()


def normalizar_conf(valor: Any) -> float:
    try:
        return float(valor)
    except Exception:
        return -1.0


def agrupar_por_linea(datos: Dict[str, List[Any]]) -> List[Dict[str, Any]]:
    """
    Agrupa palabras OCR por línea usando:
    page_num, block_num, par_num, line_num
    """
    lineas: Dict[Tuple[int, int, int, int], Dict[str, Any]] = {}

    n = len(datos["text"])
    for i in range(n):
        texto = str(datos["text"][i]).strip()
        conf = normalizar_conf(datos["conf"][i])

        if not texto:
            continue
        if conf < 0:
            continue

        clave = (
            int(datos["page_num"][i]),
            int(datos["block_num"][i]),
            int(datos["par_num"][i]),
            int(datos["line_num"][i]),
        )

        x = int(datos["left"][i])
        y = int(datos["top"][i])
        w = int(datos["width"][i])
        h = int(datos["height"][i])

        if clave not in lineas:
            lineas[clave] = {
                "page_num": int(datos["page_num"][i]),
                "block_num": int(datos["block_num"][i]),
                "par_num": int(datos["par_num"][i]),
                "line_num": int(datos["line_num"][i]),
                "words": [],
                "bbox": {
                    "x": x,
                    "y": y,
                    "w": w,
                    "h": h,
                },
            }

        lineas[clave]["words"].append({
            "text": texto,
            "conf": conf,
            "x": x,
            "y": y,
            "w": w,
            "h": h,
        })

        bbox = lineas[clave]["bbox"]
        min_x = min(bbox["x"], x)
        min_y = min(bbox["y"], y)
        max_x = max(bbox["x"] + bbox["w"], x + w)
        max_y = max(bbox["y"] + bbox["h"], y + h)
        bbox["x"] = min_x
        bbox["y"] = min_y
        bbox["w"] = max_x - min_x
        bbox["h"] = max_y - min_y

    resultado = []
    for _, linea in sorted(lineas.items(), key=lambda item: (
        item[1]["page_num"],
        item[1]["block_num"],
        item[1]["par_num"],
        item[1]["line_num"],
        item[1]["bbox"]["y"],
        item[1]["bbox"]["x"],
    )):
        linea["words"].sort(key=lambda w: w["x"])
        linea["text"] = " ".join(w["text"] for w in linea["words"]).strip()
        if linea["words"]:
            linea["avg_conf"] = round(
                sum(w["conf"] for w in linea["words"]) / len(linea["words"]),
                2
            )
        else:
            linea["avg_conf"] = -1
        resultado.append(linea)

    return resultado


def agrupar_lineas_en_bloques(lineas: List[Dict[str, Any]], tolerancia_y: int = 20) -> List[Dict[str, Any]]:
    """
    Agrupa líneas cercanas verticalmente en bloques de texto.
    """
    if not lineas:
        return []

    lineas_ordenadas = sorted(lineas, key=lambda l: (l["bbox"]["y"], l["bbox"]["x"]))
    bloques: List[Dict[str, Any]] = []
    bloque_actual: Dict[str, Any] | None = None
    ultima_y = None

    for linea in lineas_ordenadas:
        y = linea["bbox"]["y"]

        if bloque_actual is None:
            bloque_actual = {
                "bbox": dict(linea["bbox"]),
                "lines": [linea],
            }
            ultima_y = y
            continue

        if ultima_y is not None and abs(y - ultima_y) <= tolerancia_y:
            bloque_actual["lines"].append(linea)

            bbox = bloque_actual["bbox"]
            min_x = min(bbox["x"], linea["bbox"]["x"])
            min_y = min(bbox["y"], linea["bbox"]["y"])
            max_x = max(bbox["x"] + bbox["w"], linea["bbox"]["x"] + linea["bbox"]["w"])
            max_y = max(bbox["y"] + bbox["h"], linea["bbox"]["y"] + linea["bbox"]["h"])
            bbox["x"] = min_x
            bbox["y"] = min_y
            bbox["w"] = max_x - min_x
            bbox["h"] = max_y - min_y
        else:
            bloque_actual["text"] = "\n".join(l["text"] for l in bloque_actual["lines"]).strip()
            bloques.append(bloque_actual)
            bloque_actual = {
                "bbox": dict(linea["bbox"]),
                "lines": [linea],
            }

        ultima_y = y

    if bloque_actual is not None:
        bloque_actual["text"] = "\n".join(l["text"] for l in bloque_actual["lines"]).strip()
        bloques.append(bloque_actual)

    return bloques


def detectar_tabla_en_lineas(lineas: List[Dict[str, Any]], umbral_columnas: int = 2) -> Dict[str, Any] | None:
    """
    Heurística simple:
    - si muchas líneas tienen varias "celdas" separadas por posiciones X y palabras
    - se considera tabla
    """
    if len(lineas) < 2:
        return None

    filas = []
    posibles_x = []

    for linea in lineas:
        palabras = linea["words"]
        if len(palabras) < 2:
            continue

        celdas = []
        celda_actual = [palabras[0]]

        for i in range(1, len(palabras)):
            prev = palabras[i - 1]
            actual = palabras[i]
            gap = actual["x"] - (prev["x"] + prev["w"])

            # Si hay mucho hueco horizontal, asumimos nueva columna
            if gap > 35:
                celdas.append(celda_actual)
                celda_actual = [actual]
            else:
                celda_actual.append(actual)

        if celda_actual:
            celdas.append(celda_actual)

        if len(celdas) >= umbral_columnas:
            fila = []
            for celda in celdas:
                texto = " ".join(w["text"] for w in celda).strip()
                x = min(w["x"] for w in celda)
                fila.append({
                    "text": texto,
                    "x": x,
                })
                posibles_x.append(x)

            fila.sort(key=lambda c: c["x"])
            filas.append(fila)

    if len(filas) < 2:
        return None

    posibles_x = sorted(posibles_x)
    columnas_base = fusionar_posiciones_x(posibles_x, tolerancia=25)

    tabla = []
    for fila in filas:
        celdas_finales = [""] * len(columnas_base)

        for celda in fila:
            idx = columna_mas_cercana(celda["x"], columnas_base)
            celdas_finales[idx] = celda["text"]

        tabla.append(celdas_finales)

    return {
        "columns_x": columnas_base,
        "rows": tabla,
    }


def fusionar_posiciones_x(posiciones: List[int], tolerancia: int = 25) -> List[int]:
    if not posiciones:
        return []

    grupos = [[posiciones[0]]]
    for p in posiciones[1:]:
        if abs(p - grupos[-1][-1]) <= tolerancia:
            grupos[-1].append(p)
        else:
            grupos.append([p])

    return [round(sum(g) / len(g)) for g in grupos]


def columna_mas_cercana(x: int, columnas: List[int]) -> int:
    mejor_idx = 0
    mejor_dist = abs(x - columnas[0])
    for i, col_x in enumerate(columnas):
        dist = abs(x - col_x)
        if dist < mejor_dist:
            mejor_dist = dist
            mejor_idx = i
    return mejor_idx


def detectar_tablas_por_bloques(bloques: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    tablas = []

    for bloque in bloques:
        tabla = detectar_tabla_en_lineas(bloque["lines"])
        if tabla:
            tablas.append({
                "bbox": bloque["bbox"],
                "table": tabla,
            })

    return tablas


def extraer_pagina_ocr(img, lang: str) -> Dict[str, Any]:
    datos = pytesseract.image_to_data(img, lang=lang, output_type=Output.DICT)

    lineas = agrupar_por_linea(datos)
    bloques = agrupar_lineas_en_bloques(lineas)
    tablas = detectar_tablas_por_bloques(bloques)

    texto_plano = "\n".join(linea["text"] for linea in lineas if linea["text"].strip())
    texto_plano = limpiar_texto(texto_plano)

    confidencias = [
        linea["avg_conf"] for linea in lineas
        if isinstance(linea.get("avg_conf"), (int, float)) and linea["avg_conf"] >= 0
    ]
    avg_conf = round(sum(confidencias) / len(confidencias), 2) if confidencias else -1

    return {
        "text": texto_plano,
        "avg_conf": avg_conf,
        "lines": lineas,
        "blocks": bloques,
        "tables": tablas,
    }


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="OCR de PDF escaneado a JSON estructurado")
    parser.add_argument("--archivo", required=True, help="Ruta al PDF escaneado")
    parser.add_argument("--lang", default="spa+eng", help="Idiomas de Tesseract, por ejemplo spa+eng")
    parser.add_argument("--dpi", type=int, default=250, help="DPI para rasterizar el PDF")
    args = parser.parse_args()

    pdf_path = Path(args.archivo).expanduser().resolve()

    if not pdf_path.exists():
        sys.exit(f"❌ El archivo no existe: {pdf_path}")

    if pdf_path.suffix.lower() != ".pdf":
        sys.exit("❌ El archivo indicado no parece ser un PDF")

    salida_json = pdf_path.with_suffix(".json")

    with tempfile.TemporaryDirectory() as tmp:
        try:
            imgs = convert_from_path(
                str(pdf_path),
                dpi=args.dpi,
                output_folder=tmp,
                fmt="png"
            )
        except Exception as e:
            sys.exit(f"❌ No se pudo convertir PDF a imágenes: {e}")

        print(f"Procesando {len(imgs)} página(s)...")

        documento: Dict[str, Any] = {
            "source_pdf": str(pdf_path),
            "output_json": str(salida_json),
            "ocr_engine": "tesseract",
            "ocr_lang": args.lang,
            "dpi": args.dpi,
            "pages_count": len(imgs),
            "pages": [],
        }

        for idx, img in enumerate(imgs, start=1):
            try:
                pagina = extraer_pagina_ocr(img, args.lang)
                pagina["page_number"] = idx
                pagina["image_size"] = {
                    "width": img.width,
                    "height": img.height,
                }
                documento["pages"].append(pagina)
                print(f" · Página {idx} OK")
            except Exception as e:
                documento["pages"].append({
                    "page_number": idx,
                    "error": str(e),
                    "text": "",
                    "lines": [],
                    "blocks": [],
                    "tables": [],
                })
                print(f" · Página {idx} ERROR: {e}")

    salida_json.write_text(
        json.dumps(documento, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"✅ JSON OCR guardado en {salida_json}")


if __name__ == "__main__":
    main()
