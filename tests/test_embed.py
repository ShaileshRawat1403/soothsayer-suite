from embeddings.embed_model import get_embedder, embed_texts

embedder = get_embedder()
chunks = ["LangGraph is a powerful orchestration tool.", "InstructorXL is an embedding model."]
vectors = embed_texts(embedder, chunks)

print(f"Got {len(vectors)} vectors, each with {len(vectors[0])} dimensions.")
