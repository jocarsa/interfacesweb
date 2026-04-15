import os
import json
import torch
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig

MODEL_NAME = "Qwen/Qwen3.5-0.8B"
DATA_FILE = "materiales/menor.jsonl"
OUTPUT_DIR = "boe-qwen35-08b-lora"

def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            item = json.loads(line)
            question = item["question"].strip()
            answer = item["answer"].strip()

            rows.append({
                "prompt": f"### Pregunta:\n{question}\n\n### Respuesta:\n",
                "completion": answer
            })
    return rows

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    data = load_jsonl(DATA_FILE)
    dataset = Dataset.from_list(data)

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        trust_remote_code=True
    )

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None,
        trust_remote_code=True,
    )

    lora_config = LoraConfig(
        r=8,
        lora_alpha=16,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    )

    training_args = SFTConfig(
        output_dir=OUTPUT_DIR,
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        num_train_epochs=4,
        learning_rate=5e-5,
        logging_steps=1,
        save_strategy="epoch",
        save_total_limit=2,
        fp16=torch.cuda.is_available(),
        bf16=False,
        report_to="none",
        max_length=256,
        completion_only_loss=True,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=lora_config,
    )

    trainer.train()
    trainer.model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)

if __name__ == "__main__":
    main()