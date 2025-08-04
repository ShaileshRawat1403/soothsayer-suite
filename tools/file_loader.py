# tools/file_loader.py

from pathlib import Path

def load_markdown(file_path: str) -> str:
    """
    Load a markdown (.md) file and return its content as a string.

    Args:
        file_path (str): Path to the markdown file.

    Returns:
        str: Contents of the file as plain text.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    if path.suffix != ".md":
        raise ValueError("Only markdown (.md) files are supported.")

    return path.read_text(encoding="utf-8")
