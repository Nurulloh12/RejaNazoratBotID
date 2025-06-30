import json
from pathlib import Path

def load_motivatsiyalar():
    file_path = Path("data/motivatsiyalar.json")
    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("motivatsiyalar", [])