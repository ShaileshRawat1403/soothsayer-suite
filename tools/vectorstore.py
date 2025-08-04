# tools/vectorstore.py

import os
import faiss
import pickle
import numpy as np
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain.embeddings.base import Embeddings

# --- FAISS Vectorstore Functions ---

def create_vectorstore(embeddings: Embeddings, chunks: list[str], persist_path: str = None) -> FAISS:
    """
    Creates a FAISS vectorstore from text chunks.
    """
    vectorstore = FAISS.from_texts(chunks, embeddings)

    if persist_path:
        faiss.write_index(vectorstore.index, f"{persist_path}.index")
        with open(f"{persist_path}_store.pkl", "wb") as f:
            pickle.dump(vectorstore.docstore._dict, f)

    return vectorstore

def load_vectorstore(embeddings: Embeddings, persist_path: str) -> FAISS:
    """
    Loads a saved FAISS vectorstore from disk.
    """
    index = faiss.read_index(f"{persist_path}.index")
    with open(f"{persist_path}_store.pkl", "rb") as f:
        docstore_dict = pickle.load(f)

    docstore = InMemoryDocstore(docstore_dict)
    return FAISS(index, embeddings.embed_query, docstore, {})

# --- SimpleVectorDB (In-Memory, No Persistence) ---

class SimpleVectorDB:
    def __init__(self, dim: int = 768):
        self.index = faiss.IndexFlatL2(dim)
        self.chunks = []  # Store original text for retrieval

    def add(self, embeddings: List[List[float]], texts: List[str]):
        if len(embeddings) != len(texts):
            raise ValueError("Embeddings and text chunks must be the same length.")
        self.index.add(np.array(embeddings).astype("float32"))
        self.chunks.extend(texts)

    def query(self, embedding: List[float], top_k: int = 5) -> List[str]:
        if self.index.ntotal == 0:
            return ["[No data in vector store]"]
        D, I = self.index.search(np.array([embedding]).astype("float32"), top_k)
        return [self.chunks[i] for i in I[0] if i < len(self.chunks)]

    def size(self) -> int:
        return self.index.ntotal
