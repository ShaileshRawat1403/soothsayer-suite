# rag/md_loader.py

from pathlib import Path
from typing import List
import re
from tools.chunker import chunk_markdown  # unified chunking logic

def load_markdown_chunks(file_path: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    """
    Load and split a markdown file into semantically meaningful and overlapping chunks
    using markdown headers and list structure.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    content = path.read_text(encoding='utf-8')

    # Split by headers and numbered list items (anchors)
    raw_chunks = re.split(r'(?=^\s*(#{1,6}\s|\d+\.\s))', content, flags=re.MULTILINE)

    # Clean and filter
    chunks = []
    seen = set()
    for chunk in raw_chunks:
        chunk = chunk.strip()
        if len(chunk) >= 30 and chunk not in seen:
            # Further split large blocks if needed
            if len(chunk) > chunk_size:
                sub_chunks = chunk_markdown(chunk, chunk_size, overlap)
                for sub in sub_chunks:
                    if sub not in seen:
                        chunks.append(sub)
                        seen.add(sub)
            else:
                chunks.append(chunk)
                seen.add(chunk)

    return chunks
