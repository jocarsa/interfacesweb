# pip3 install chromadb --break-system-packages

import requests
import chromadb

# -----------------------------
# CONFIG
# -----------------------------
OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text:v1.5"
DB_PATH = "mi_chromadb"
COLLECTION_NAME = "palabras"

# -----------------------------
# FUNCIÓN PARA OBTENER EMBEDDING
# -----------------------------
def get_embedding(texto):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": texto
        }
    )
    response.raise_for_status()
    return response.json()["embedding"]

# -----------------------------
# INICIALIZAR CHROMADB
# -----------------------------
client = chromadb.PersistentClient(path=DB_PATH)

# Crear o recuperar colección
collection = client.get_or_create_collection(name=COLLECTION_NAME)

# -----------------------------
# PALABRAS A GUARDAR
# -----------------------------
palabras = ["gato", "perro", "camion", "ira"]

# -----------------------------
# GUARDAR EN CHROMADB
# -----------------------------
for i, palabra in enumerate(palabras):
    embedding = get_embedding(palabra)
    collection.add(
        ids=[str(i)],
        documents=[palabra],
        embeddings=[embedding]
    )
    print(f"Guardado: {palabra}")

print("Proceso terminado.")