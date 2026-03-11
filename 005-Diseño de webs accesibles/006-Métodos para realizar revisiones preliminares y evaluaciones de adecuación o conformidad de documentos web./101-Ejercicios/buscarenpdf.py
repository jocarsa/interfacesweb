#!/usr/bin/env python3
"""
buscar_en_pdf.py
Busca un término (o expresión regex con --regex) en todo el PDF e imprime
el nº de página y un pequeño contexto.

Ejemplo:
    python buscar_en_pdf.py contrato.pdf "confidencial" --regex
"""
import argparse, re, textwrap
from pathlib import Path
from pypdf import PdfReader   # type: ignore

def main() -> None:
    p = argparse.ArgumentParser(description="Buscar texto dentro de un PDF")
    p.add_argument("archivo", help="PDF de origen")
    p.add_argument("patron", help="Palabra o expresión regular")
    p.add_argument("--regex", action="store_true", help="Interpretar patrón como regex")
    p.add_argument("--contexto", type=int, default=40,
                   help="Nº de caracteres alrededor de la coincidencia")
    args = p.parse_args()

    lector = PdfReader(args.archivo)
    buscar = (lambda txt: re.finditer(args.patron, txt, re.I|re.S)) if args.regex \
             else (lambda txt: (m for m in re.finditer(re.escape(args.patron), txt, re.I)))

    halladas = 0
    for i, pag in enumerate(lector.pages, start=1):
        texto = pag.extract_text() or ""
        for m in buscar(texto):
            inicio = max(m.start() - args.contexto, 0)
            fin = m.end() + args.contexto
            snippet = textwrap.shorten(texto[inicio:fin].replace("\n", " "),
                                       width=args.contexto*2, placeholder="…")
            print(f"Pág {i}: …{snippet}…")
            halladas += 1

    if halladas:
        print(f"\n🔎 Encontradas {halladas} coincidencia(s).")
    else:
        print("💤  No se encontró el término.")

if __name__ == "__main__":
    main()

