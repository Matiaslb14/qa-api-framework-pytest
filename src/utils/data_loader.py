import json
from pathlib import Path


def load_json(relative_path: str) -> dict:
    base_dir = Path(__file__).resolve().parents[2]  # project root
    file_path = base_dir / relative_path
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
