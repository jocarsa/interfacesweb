#!/usr/bin/env python3
"""
pdf_a_txt.py
Extrae el texto de un PDF y lo guarda en .txt, conservando saltos entre páginas.

Ejemplos de uso
---------------
# PDF completo
python pdf_a_txt.py --archivo informe.pdf

# Solo páginas 2-5
python pdf_a_txt.py --archivo informe.pdf --paginas 2-5
"""
import argparse
from pathlib import Path
from pypdf import PdfReader   # type: ignore

def parsear_rango(cadena: str) -> range:
    """'2-5' → range(2, 6)  (1-basado como en Acrobat)"""
    if "-" not in cadena:
        n = int(cadena)
        return range(n, n + 1)
    ini, fin = map(int, cadena.split("-", 1))
    return range(ini, fin + 1)

def main() -> None:
    p = argparse.ArgumentParser(description="Extraer texto de un PDF")
    p.add_argument("--archivo", required=True, help="Ruta del PDF")
    p.add_argument("--paginas", help="Ej. 3 o 2-5 (1-basado)")
    args = p.parse_args()

    lector = PdfReader(args.archivo)
    total = len(lector.pages)

    rango = (parsear_rango(args.paginas) if args.paginas
             else range(1, total + 1))

    texto = []
    for num in rango:
        if not (1 <= num <= total):
            p.error(f"Página {num} fuera de rango (1–{total})")
        pagina = lector.pages[num - 1]
        texto.append(pagina.extract_text() or "")
        texto.append("\n" + "-" * 40 + f" [Fin página {num}]\n")

    salida = Path(args.archivo).with_suffix(".txt")
    salida.write_text("".join(texto), encoding="utf-8")
    print(f"✅ Texto extraído a {salida} ({len(rango)} pág.).")

if __name__ == "__main__":
    main()

