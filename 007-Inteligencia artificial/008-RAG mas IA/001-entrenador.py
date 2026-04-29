# pip install chromadb

import re
import chromadb

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
txt_path = "ciclosformativos.txt"
db_path = "ciclosformativos"
collection_name = "ciclosformativos_parrafos"

# -----------------------------
# LEER ARCHIVO TXT
# -----------------------------
with open(txt_path, "r", encoding="utf-8") as f:
    contenido = f.read()

# -----------------------------
# SEPARAR EN PÁRRAFOS
# Usa doble salto de línea como separador
# -----------------------------
parrafos = re.split(r"\n\s*\n", contenido)
parrafos = [p.strip() for p in parrafos if p.strip()]

print(f"Se han encontrado {len(parrafos)} párrafos")

# -----------------------------
# INICIALIZAR CHROMADB
# -----------------------------
client = chromadb.PersistentClient(path=db_path)

# Borrar colección previa si existe
try:
    client.delete_collection(collection_name)
except:
    pass

collection = client.create_collection(name=collection_name)

# -----------------------------
# GUARDAR PÁRRAFOS
# -----------------------------
for i, parrafo in enumerate(parrafos):
    collection.add(
        ids=[f"parrafo_{i}"],
        documents=[parrafo],
        metadatas=[{"indice": i, "origen": txt_path}]
    )

print(f"Se han guardado {len(parrafos)} párrafos en la colección '{collection_name}'")