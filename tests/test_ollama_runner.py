from ollama.model_runner import run_llm

output = run_llm("What is LangGraph?", context=["LangGraph is a modular AI agent system."])
print(output)
