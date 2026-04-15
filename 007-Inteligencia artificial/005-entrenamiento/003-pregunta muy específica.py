import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:3b-instruct",
        "prompt": "Dame el temario de la asignatura Diseño de Interfaces Web de segundo curso de DAW. Si tienes la respuesta en tu base de datos, indicala, y si no la tienes, dilo tambien.",
        "stream": False
    }
)

print(response.json()["response"])