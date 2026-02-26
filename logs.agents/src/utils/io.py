"""I/O helpers (placeholder)."""

from pathlib import Path

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)
