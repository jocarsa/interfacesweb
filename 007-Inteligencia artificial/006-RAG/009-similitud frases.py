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

def cosine_similarity(vec1, vec2):
    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot / (norm1 * norm2)

# -----------------------------
# LISTA DE PALABRAS
# -----------------------------
words = [
  "yo vivo en Valencia", 
  "yo vivo en Burjassot", 
  "tu vives en Valencia", 
  "ella vive en Valencia"
]

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
results = []

for w1, w2 in itertools.combinations(words, 2):
    sim = cosine_similarity(embeddings[w1], embeddings[w2])
    results.append((w1, w2, sim))

# ordenar por mayor similitud
results.sort(key=lambda x: x[2], reverse=True)

# -----------------------------
# MOSTRAR RESULTADOS
# -----------------------------
print("\nSimilitud coseno (mayor = más similares):\n")

for w1, w2, sim in results:
    print(f"{w1:>7}  vs  {w2:<7} -> {sim:.4f}")