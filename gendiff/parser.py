import yaml
import json
from pathlib import Path


def parse_file(filepath):
    path = Path(filepath)
    suffix = path.suffix.lower()

    with open(filepath) as file:
        if suffix == ".json":
            return json.load(file)
        if suffix in (".yml", ".yaml"):
            return yaml.safe_load(file)

    raise ValueError(f"Unsupported file format: {suffix}")
