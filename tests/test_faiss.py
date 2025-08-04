from embeddings.embed_model import get_embedder, embed_texts
from tools.vectorstore import SimpleVectorDB

texts = [
    "LangGraph is a graph-based agent framework.",
    "FAISS is used for fast vector search.",
    "InstructorXL provides high-quality embeddings.",
    "Ollama runs local LLMs like Mistral."
]

model = get_embedder()
vectors = embed_texts(model, texts)

db = SimpleVectorDB()
db.add(vectors, texts)

query = "What helps me search similar content fast?"
query_vec = embed_texts(model, [query])[0]

results = db.query(query_vec)
print("Top matches:\n", "\n---\n".join(results))
