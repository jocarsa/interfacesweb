import os
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# =========================================================
# CONFIGURATION
# =========================================================
BASE_MODEL = "Qwen/Qwen3.5-4B"
ADAPTER_PATH = "./boe-qwen35-4b-lora"
OUTPUT_PATH = "./boe-qwen35-4b-lora-fusionado"


def main():
    if not os.path.isdir(ADAPTER_PATH):
        raise FileNotFoundError(f"No existe la carpeta del adaptador: {ADAPTER_PATH}")

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        BASE_MODEL,
        trust_remote_code=True
    )

    print("Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
        trust_remote_code=True
    )

    print("Loading adapter...")
    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)

    print("Merging adapter into base model...")
    merged_model = model.merge_and_unload()

    print(f"Saving merged model to: {OUTPUT_PATH}")
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    merged_model.save_pretrained(OUTPUT_PATH)
    tokenizer.save_pretrained(OUTPUT_PATH)

    print("Done.")
    print(f"Merged model saved in: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
