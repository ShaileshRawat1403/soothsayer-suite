# ollama/model_runner.py

import os
import requests
from tools.hf_inference import query_huggingface

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = os.getenv("MODEL_NAME", "mistral")  # fallback to mistral

def run_llm(prompt: str, context: list[str] = None) -> str:
    # Build the prompt
    full_prompt = ""
    if context:
        full_prompt += "Context:\n" + "\n---\n".join(context) + "\n\n"
    full_prompt += f"Query:\n{prompt}\n\nAnswer:"

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False
    }

    # === Try Ollama First ===
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()["response"].strip()

    # === Fallback to Hugging Face if Ollama fails ===
    except Exception as ollama_error:
        print(f"[WARN] Ollama not available. Falling back to Hugging Face. Reason: {str(ollama_error)}")
        try:
            return query_huggingface(full_prompt, model_name="gpt2")
        except Exception as hf_error:
            return f"[FATAL] Both Ollama and Hugging Face failed:\n{str(hf_error)}"
