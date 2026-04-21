import requests
import numpy as np

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text:v1.5"

def get_embedding(text):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": text
    })
    response.raise_for_status()
    data = response.json()
    return np.array(data["embedding"])

def l1_distance(vec1, vec2):
    return np.sum(np.abs(vec1 - vec2))

# -----------------------------
# TEXTOS
# -----------------------------
texts = ["gato", "perro", "camion"]

# -----------------------------
# OBTENER EMBEDDINGS
# -----------------------------
embeddings = {}
for t in texts:
    print(f"Generando embedding para: {t}")
    embeddings[t] = get_embedding(t)

# -----------------------------
# CALCULAR DISTANCIAS L1
# -----------------------------
print("\nDistancias L1 (menor = más similares):\n")

for i in range(len(texts)):
    for j in range(i + 1, len(texts)):
        t1 = texts[i]
        t2 = texts[j]
        dist = l1_distance(embeddings[t1], embeddings[t2])
        print(f"{t1} vs {t2}: {dist:.4f}")