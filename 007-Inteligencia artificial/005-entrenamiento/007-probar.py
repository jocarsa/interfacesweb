import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# =========================================================
# CONFIGURATION
# =========================================================
MODEL_PATH = "./boe-qwen35-4b-lora-fusionado"

MAX_NEW_TOKENS = 192
TEMPERATURE = 0.0
TOP_P = 1.0

PROMPT_PREFIX = "### Pregunta:\n"
PROMPT_MIDDLE = "\n\n### Respuesta:\n"


# =========================================================
# HELPERS
# =========================================================
def build_prompt(question: str) -> str:
    question = question.strip()
    return f"{PROMPT_PREFIX}{question}{PROMPT_MIDDLE}"


def clean_response(text: str) -> str:
    text = text.strip()

    stops = [
        "\n### Pregunta:",
        "\n### Respuesta:",
        "\nPregunta:",
        "\nRespuesta:"
    ]
    for s in stops:
        if s in text:
            text = text.split(s)[0].strip()

    text = re.sub(r"\s+", " ", text).strip()
    return text


def load_model():
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True
    )

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
        trust_remote_code=True
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model.eval()
    return tokenizer, model


def answer_question(model, tokenizer, question: str) -> str:
    prompt = build_prompt(question)

    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=False if TEMPERATURE == 0 else True,
            temperature=None if TEMPERATURE == 0 else TEMPERATURE,
            top_p=TOP_P,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
            use_cache=True,
            repetition_penalty=1.05,
        )

    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    response = tokenizer.decode(new_tokens, skip_special_tokens=True)
    response = clean_response(response)

    if not response:
        return "No he podido generar una respuesta."

    return response


def main():
    tokenizer, model = load_model()

    print("Model loaded.")
    print("Write 'salir' to exit.\n")

    while True:
        question = input("Tú: ").strip()
        if question.lower() in ["salir", "exit", "quit"]:
            break

        if not question:
            continue

        answer = answer_question(model, tokenizer, question)
        print("\nModelo:", answer)
        print()


if __name__ == "__main__":
    main()
