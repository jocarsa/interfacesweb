#!/usr/bin/env python3
"""
pdf_ocr_texto.py
Convierte cada página de un PDF a imagen, pasa OCR con Tesseract
y genera un .txt. Útil cuando extract_text() devuelve cadenas vacías.

Ejemplo:
    python pdf_ocr_texto.py escaneado.pdf
"""
import argparse, tempfile, sys
from pathlib import Path
from pdf2image import convert_from_path     # type: ignore
import pytesseract                          # type: ignore

def main() -> None:
    p = argparse.ArgumentParser(description="OCR para PDF escaneado")
    p.add_argument("--archivo", required=True, help="PDF escaneado")
    args = p.parse_args()

    pdf_path = Path(args.archivo).expanduser().resolve()
    salida_txt = pdf_path.with_suffix(".txt")

    with tempfile.TemporaryDirectory() as tmp:
        try:
            imgs = convert_from_path(str(pdf_path), output_folder=tmp)
        except Exception as e:
            sys.exit(f"❌ No se pudo convertir PDF a imágenes: {e}")

        print(f"Procesando {len(imgs)} página(s)...")
        texto_total = []
        for idx, img in enumerate(imgs, start=1):
            texto = pytesseract.image_to_string(img, lang="spa+eng")
            texto_total.append(texto)
            print(f" · Página {idx} OK")

    salida_txt.write_text("\n\n".join(texto_total), encoding="utf-8")
    print(f"✅ Texto OCR guardado en {salida_txt}")

if __name__ == "__main__":
    main()

