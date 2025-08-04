from agents.base_flow import run_agent_flow

input_data = {
    "query": "What is the purpose of this repo?",
    "file_path": "docs/sample.md",
    "output_format": "markdown",
    "chunk_size": 300,
    "top_k": 3,
    "test_mode": True
}

result = run_agent_flow(input_data)
print("🧪 Final Output:\n", result.get("formatted_output", "⚠️ No formatted output returned"))
