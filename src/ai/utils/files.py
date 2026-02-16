from pathlib import Path


def read_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"{path} not found")
    return p.read_text()
