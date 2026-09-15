from pathlib import Path
import yaml

CONFIG_DIR = Path.home() / ".src"
CONFIG_FILE = CONFIG_DIR / "config.yaml"

DEFAULT_CONFIG = {
    "provider": "ollama",
    "model": "qwen2:0.5b",
    "temperature": 0.2,
    "max_tokens": 2000,
}


def load_config():
    if not CONFIG_FILE.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            yaml.safe_dump(DEFAULT_CONFIG, f)
        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)
