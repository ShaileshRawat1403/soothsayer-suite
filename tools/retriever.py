# tools/retriever.py

from tools.vectorstore import create_vectorstore
from embeddings.embed_model import get_embedder, embed_texts
from rag.md_loader import load_markdown_chunks
from typing import Optional, List, Dict, Any


def build_retriever_from_md(
    markdown_path: str,
    persist_path: Optional[str] = None,
    test_mode: bool = False
) -> Dict[str, Any]:
    """
    Converts a markdown file into a searchable vectorstore (FAISS).
    If test_mode is enabled, it returns only cleaned chunks.

    Args:
        markdown_path (str): Path to markdown (.md) file.
        persist_path (str, optional): Path to save/reuse FAISS index.
        test_mode (bool): If True, skips embedding and returns only chunks.

    Returns:
        dict: {
            "vectorstore": FAISS object or None,
            "chunks": List of cleaned markdown chunks
        }
    """
    # Load raw chunks from markdown
    raw_chunks = load_markdown_chunks(markdown_path)

    # Clean and deduplicate chunks
    seen = set()
    clean_chunks: List[str] = []
    for chunk in raw_chunks:
        chunk = chunk.strip()
        if len(chunk) < 30 or chunk in seen:
            continue
        seen.add(chunk)
        clean_chunks.append(chunk)

    # If dry run, skip vectorstore creation
    if test_mode:
        return {
            "vectorstore": None,
            "chunks": clean_chunks
        }

    # Embed and store
    embedder = get_embedder()
    vectorstore = create_vectorstore(embedder, clean_chunks, persist_path)

    return {
        "vectorstore": vectorstore,
        "chunks": clean_chunks
    }
