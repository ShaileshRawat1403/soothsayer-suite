from langgraph.graph import StateGraph
from typing import Dict

# === STATE SCHEMA ===
state_schema = Dict[str, object]

# === LANGGRAPH NODE FUNCTIONS ===

def input_parser(state: state_schema) -> state_schema:
    # Basic pass-through
    return state

def chunk_loader(state: state_schema) -> state_schema:
    from rag.md_loader import load_markdown_chunks
    path = state["file_path"]
    chunks = load_markdown_chunks(path, chunk_size=state.get("chunk_size", 300))
    state["chunks"] = chunks
    return state

def embedder(state: state_schema) -> state_schema:
    from embeddings.embed_model import get_embedder, embed_texts
    embed_model = get_embedder()
    embeddings = embed_texts(embed_model, state["chunks"])
    state["embeddings"] = embeddings
    return state

def retriever(state: state_schema) -> state_schema:
    import re
    from tools.vectorstore import SimpleVectorDB
    from embeddings.embed_model import get_embedder, embed_texts

    # Initialize in-memory vector DB
    db = SimpleVectorDB()
    db.add(state["embeddings"], state["chunks"])

    # Embed query
    query_embed = embed_texts(get_embedder(), [state["query"]])[0]

    # Retrieve top-k
    raw_chunks = db.query(query_embed, top_k=state.get("top_k", 5))

    # Clean and deduplicate
    seen = set()
    clean_chunks = []
    for chunk in raw_chunks:
        chunk = re.sub(r'^\d+\.\s+', '', chunk.strip())  # Clean numbered list headers
        if len(chunk) < 30 or chunk in seen:
            continue
        seen.add(chunk)
        clean_chunks.append(chunk)

    # Fallback if nothing was returned
    if not clean_chunks:
        clean_chunks = ["[No relevant context could be retrieved.]"]

    state["relevant_chunks"] = clean_chunks
    return state

def thinker(state: state_schema) -> state_schema:
    from ollama.model_runner import run_llm
    if state.get("test_mode"):
        state["raw_output"] = "[TEST MODE] Retrieved chunks:\n" + "\n".join(state["relevant_chunks"])
    else:
        state["raw_output"] = run_llm(state["query"], context=state["relevant_chunks"])
    return state

def formatter(state: state_schema) -> state_schema:
    answer = state["raw_output"]
    state["formatted_output"] = f"### 🧠 Soothsayer’s Response\n\n{answer}"
    return state

def final_responder(state: state_schema) -> state_schema:
    return state  # Let CLI handle final display

# === MAIN FLOW WRAPPER ===

def run_agent_flow(user_input: dict):
    graph = StateGraph(name="soothsayer-graph", state_schema=state_schema)

    # Register steps
    graph.add_node("InputParser", input_parser)
    graph.add_node("ChunkLoader", chunk_loader)
    graph.add_node("Embedder", embedder)
    graph.add_node("Retriever", retriever)
    graph.add_node("Thinker", thinker)
    graph.add_node("Formatter", formatter)
    graph.add_node("FinalResponder", final_responder)

    # Connect nodes
    graph.set_entry_point("InputParser")
    graph.add_edge("InputParser", "ChunkLoader")
    graph.add_edge("ChunkLoader", "Embedder")
    graph.add_edge("Embedder", "Retriever")
    graph.add_edge("Retriever", "Thinker")
    graph.add_edge("Thinker", "Formatter")
    graph.add_edge("Formatter", "FinalResponder")
    graph.set_finish_point("FinalResponder")

    # Run
    app = graph.compile()
    return app.invoke(user_input)
