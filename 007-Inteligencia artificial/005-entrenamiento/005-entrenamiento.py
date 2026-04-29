import os
import json
import random
from pathlib import Path

import torch
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig

# =========================================================
# CONFIGURATION
# =========================================================
MODEL_NAME = "Qwen/Qwen3.5-4B"
DATA_DIR = "materiales"
OUTPUT_DIR = "boe-qwen35-4b-lora"

SEED = 42
VAL_RATIO = 0.05

MAX_LENGTH = 768

PER_DEVICE_TRAIN_BATCH_SIZE = 1
PER_DEVICE_EVAL_BATCH_SIZE = 1
GRADIENT_ACCUMULATION_STEPS = 8
NUM_TRAIN_EPOCHS = 6
LEARNING_RATE = 2e-5
WEIGHT_DECAY = 0.01
WARMUP_RATIO = 0.03
LOGGING_STEPS = 10
SAVE_TOTAL_LIMIT = 2

PROMPT_PREFIX = "### Pregunta:\n"
PROMPT_MIDDLE = "\n\n### Respuesta:\n"


# =========================================================
# HELPERS
# =========================================================
def set_seed(seed: int) -> None:
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def find_jsonl_files(folder: str):
    base = Path(folder)
    if not base.exists():
        raise FileNotFoundError(f"No existe la carpeta de datos: {folder}")

    files = sorted(base.rglob("*.jsonl"))
    if not files:
        raise FileNotFoundError(f"No se encontraron archivos .jsonl dentro de: {folder}")

    return files


def build_text(question: str, answer: str) -> str:
    question = question.strip()
    answer = answer.strip()
    return f"{PROMPT_PREFIX}{question}{PROMPT_MIDDLE}{answer}"


def load_all_jsonl(folder: str):
    files = find_jsonl_files(folder)
    rows = []

    for filepath in files:
        print(f"Cargando: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    item = json.loads(line)
                except json.JSONDecodeError as e:
                    print(f"[AVISO] JSON inválido en {filepath} línea {line_number}: {e}")
                    continue

                question = str(item.get("question", "")).strip()
                answer = str(item.get("answer", "")).strip()

                if not question or not answer:
                    print(f"[AVISO] Registro incompleto en {filepath} línea {line_number}")
                    continue

                rows.append({
                    "text": build_text(question, answer),
                    "question": question,
                    "answer": answer,
                    "source_file": str(filepath),
                })

    if not rows:
        raise ValueError("No se cargó ningún ejemplo válido desde los archivos JSONL.")

    return rows, files


def split_dataset(rows, val_ratio=0.05, seed=42):
    rng = random.Random(seed)
    rows = rows[:]
    rng.shuffle(rows)

    if len(rows) < 20:
        val_size = 1
    else:
        val_size = max(1, int(len(rows) * val_ratio))

    eval_rows = rows[:val_size]
    train_rows = rows[val_size:]

    if not train_rows:
        raise ValueError("El conjunto de entrenamiento ha quedado vacío tras la partición.")

    return train_rows, eval_rows


def print_dataset_report(rows, files):
    print("=" * 60)
    print("RESUMEN DEL DATASET")
    print("=" * 60)
    print(f"Archivos JSONL encontrados: {len(files)}")
    for f in files:
        print(f" - {f}")
    print(f"Ejemplos válidos cargados: {len(rows)}")
    print("=" * 60)


# =========================================================
# MAIN
# =========================================================
def main():
    set_seed(SEED)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    rows, files = load_all_jsonl(DATA_DIR)
    print_dataset_report(rows, files)

    train_rows, eval_rows = split_dataset(rows, val_ratio=VAL_RATIO, seed=SEED)

    train_dataset = Dataset.from_list(train_rows)
    eval_dataset = Dataset.from_list(eval_rows)

    print(f"Train examples: {len(train_dataset)}")
    print(f"Eval examples : {len(eval_dataset)}")

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading model...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        trust_remote_code=True,
    )

    model.config.use_cache = False

    print("Preparing LoRA...")
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    )

    print("Preparing training config...")
    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        do_train=True,
        do_eval=True,
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_strategy="steps",
        logging_steps=LOGGING_STEPS,
        save_total_limit=SAVE_TOTAL_LIMIT,
        per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
        per_device_eval_batch_size=PER_DEVICE_EVAL_BATCH_SIZE,
        gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
        num_train_epochs=NUM_TRAIN_EPOCHS,
        learning_rate=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY,
        warmup_ratio=WARMUP_RATIO,
        lr_scheduler_type="cosine",
        fp16=torch.cuda.is_available(),
        bf16=False,
        report_to="none",
        max_length=MAX_LENGTH,
        completion_only_loss=False,
        dataset_text_field="text",
        packing=False,
        seed=SEED,
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        greater_is_better=False,
    )

    print("Creating trainer...")
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
        processing_class=tokenizer,
        peft_config=lora_config,
    )

    print("Starting training...")
    trainer.train()

    print("Saving adapter and tokenizer...")
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

    print("Done.")
    print(f"Adapter saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
