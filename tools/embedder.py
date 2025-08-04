# tools/embedder.py

from typing import List
from langchain.embeddings import HuggingFaceEmbeddings

def get_embedder():
    """
    Returns a HuggingFace-based embedding model.
    Replace or extend this if switching to InstructorXL or OpenAI.
    """
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def embed_chunks(chunks: List[str]) -> List[List[float]]:
    """
    Converts chunks of text into embeddings.

    Args:
        chunks (List[str]): List of markdown chunks.

    Returns:
        List[List[float]]: List of vector embeddings.
    """
    embedder = get_embedder()
    return embedder.embed_documents(chunks)
