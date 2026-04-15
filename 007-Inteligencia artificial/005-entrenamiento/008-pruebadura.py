import json
import difflib

# -----------------------------
# CONFIGURATION
# -----------------------------
DATA_FILE = "materiales/BOE-A-2023-13221.jsonl"
MIN_SIMILARITY = 0.90   # raise to 0.95 or 0.98 if you want it even stricter

def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            q = item["question"].strip()
            a = item["answer"].strip()
            rows.append({
                "question": q,
                "answer": a
            })
    return rows

def normalize(text):
    return " ".join(text.strip().lower().split())

def find_best_match(user_question, dataset):
    user_q = normalize(user_question)

    best_item = None
    best_score = 0.0

    for item in dataset:
        trained_q = normalize(item["question"])
        score = difflib.SequenceMatcher(None, user_q, trained_q).ratio()

        if score > best_score:
            best_score = score
            best_item = item

    return best_item, best_score

def main():
    dataset = load_jsonl(DATA_FILE)

    print("Dataset loaded.")
    print("This system answers only with trained questions and answers.")
    print("Write 'salir' to exit.\n")

    while True:
        pregunta = input("Tú: ").strip()
        if pregunta.lower() in ["salir", "exit", "quit"]:
            break

        item, score = find_best_match(pregunta, dataset)

        if item is not None and score >= MIN_SIMILARITY:
            print("\nModelo:", item["answer"])
            print(f"(matched trained question with similarity {score:.4f})\n")
        else:
            print("\nModelo: No lo sé según el material entrenado.\n")

if __name__ == "__main__":
    main()