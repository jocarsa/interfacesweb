import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "qwen2.5:3b-instruct",
        "prompt": "Hola, ¿qué puedes hacer?",
        "stream": False
    }
)

print(response.json()["response"])