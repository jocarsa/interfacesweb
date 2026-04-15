import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "./boe-qwen35-08b-lora-fusionado"
MAX_NEW_TOKENS = 96

REJECTION = "No lo sé según el material entrenado."

def load_model():
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
        trust_remote_code=True
    )

    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    model.eval()
    return tokenizer, model

def build_prompt(question: str) -> str:
    return f"### Pregunta:\n{question}\n\n### Respuesta:\n"

def clean_response(text: str) -> str:
    text = text.strip()

    # corta si el modelo empieza otra pregunta/respuesta
    stops = [
        "\n### Pregunta:",
        "\n### Respuesta:",
        "\nPregunta:",
        "\nRespuesta:"
    ]
    for s in stops:
        if s in text:
            text = text.split(s)[0].strip()

    # compacta espacios
    text = re.sub(r"\s+", " ", text).strip()

    return text

def answer_question(model, tokenizer, question: str) -> str:
    prompt = build_prompt(question)

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            use_cache=True,
        )

    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    response = tokenizer.decode(new_tokens, skip_special_tokens=True)
    response = clean_response(response)

    if not response:
        return REJECTION

    # si se queda en una frase claramente cortada, rechaza
    bad_endings = [
        "dispone que:",
        "establece que:",
        "pertenecen",
        "corresponden",
        "es:",
        "son:"
    ]
    lower = response.lower()
    if any(lower.endswith(x) for x in bad_endings):
        return REJECTION

    return response

def main():
    tokenizer, model = load_model()

    print("Model loaded.")
    print("Write 'salir' to exit.\n")

    while True:
        question = input("Tú: ").strip()
        if question.lower() in ["salir", "exit", "quit"]:
            break

        answer = answer_question(model, tokenizer, question)
        print("\nModelo:", answer)
        print()

if __name__ == "__main__":
    main()