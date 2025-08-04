from sentence_transformers import SentenceTransformer
from typing import List

# Load the InstructorXL model (from HuggingFace)
def get_embedder(model_name: str = "hkunlp/instructor-xl") -> SentenceTransformer:
    return SentenceTransformer(model_name, device='cpu') 

# Embed a list of strings (like markdown chunks)
def embed_texts(model: SentenceTransformer, texts: List[str], task: str = "Represent for retrieval") -> List[List[float]]:
    # InstructorXL expects input format: [task, text]
    formatted_inputs = [[task, text] for text in texts]
    return model.encode(formatted_inputs, convert_to_numpy=True).tolist()
