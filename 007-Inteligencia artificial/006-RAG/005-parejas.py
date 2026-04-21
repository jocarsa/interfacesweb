import requests
import numpy as np
import itertools

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text:v1.5"

def get_embedding(text):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": text
    })
    response.raise_for_status()
    return np.array(response.json()["embedding"])

def l1_distance(vec1, vec2):
    return np.sum(np.abs(vec1 - vec2))

# -----------------------------
# LISTA DE PALABRAS
# -----------------------------
words = ["gato", "perro", "camion", "ira"]

# -----------------------------
# OBTENER EMBEDDINGS
# -----------------------------
embeddings = {}
for w in words:
    print(f"Embedding: {w}")
    embeddings[w] = get_embedding(w)

# -----------------------------
# CALCULAR TODAS LAS PAREJAS
# -----------------------------
print("\nDistancias L1 entre todas las parejas:\n")

for w1, w2 in itertools.combinations(words, 2):
    dist = l1_distance(embeddings[w1], embeddings[w2])
    print(f"{w1:>7}  vs  {w2:<7} -> {dist:.4f}")