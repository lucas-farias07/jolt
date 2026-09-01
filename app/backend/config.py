import json
from pathlib import Path

#abs path
ROOT_DIR = Path(__file__).resolve().parents[2]

BASE_DIR = Path(__file__).resolve().parent

with open(ROOT_DIR / "config.json") as f:
    configuration = json.load(f)
