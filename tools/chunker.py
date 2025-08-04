# tools/chunker.py

import re
from typing import List

def chunk_markdown(text: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    """
    Splits markdown text into semantically meaningful, overlapping chunks using headers and list markers.
    Deduplicates and filters out very short or repeated segments.

    Args:
        text (str): Full markdown content as a string.
        chunk_size (int): Maximum characters per chunk.
        overlap (int): Number of characters to overlap between chunks.

    Returns:
        List[str]: Cleaned and chunked markdown segments.
    """
    # First split on semantic anchors (headers or list items)
    raw_chunks = re.split(r'(?=\n*#+\s|\n*\d+\.\s)', text)

    cleaned = []
    seen = set()

    for chunk in raw_chunks:
        chunk = chunk.strip()
        if len(chunk) >= 30 and chunk not in seen:
            cleaned.append(chunk)
            seen.add(chunk)

    # Second layer: break large chunks into overlapping windows
    final_chunks = []
    for chunk in cleaned:
        start = 0
        while start < len(chunk):
            end = min(start + chunk_size, len(chunk))
            segment = chunk[start:end].strip()
            if len(segment) > 30 and segment not in seen:
                final_chunks.append(segment)
                seen.add(segment)
            start += chunk_size - overlap

    return final_chunks
