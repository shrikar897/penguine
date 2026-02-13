import json
from pathlib import Path

MEMORY_FILE = Path("app/memory/memory.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def add_memory(text: str, category: str = "general"):
    memory = load_memory()
    memory.append({
        "text": text,
        "category": category
    })
    save_memory(memory)


def list_memory():
    return load_memory()


def delete_memory(index: int):
    memory = load_memory()
    if 0 <= index < len(memory):
        memory.pop(index)
        save_memory(memory)
        return True
    return False


def clear_memory():
    save_memory([])


def get_memory_for_prompt():
    memory = load_memory()
    if not memory:
        return ""

    lines = []
    for item in memory:
        lines.append(f"- ({item['category']}) {item['text']}")

    return "Known facts about the user:\n" + "\n".join(lines)
