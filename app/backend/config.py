import json
from pathlib import Path


__config_path = Path(__file__).parent.parent.parent / "config.json"

with open(__config_path, "r") as file:
    configuration: dict[str, str | int | None] = json.load(file)
    print(configuration)
