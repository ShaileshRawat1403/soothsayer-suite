# embeddings/vector_store.py

import faiss
import numpy as np
from typing import List

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
