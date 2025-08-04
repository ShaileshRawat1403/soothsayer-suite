# tools/hf_inference.py

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEFAULT_MODEL = "gpt2"  # Fallback to a known-safe model

def query_huggingface(prompt: str, model_name: str = None) -> str:
    """
    Queries the Hugging Face Inference API with the given prompt and model.
    
    Args:
        prompt (str): The user prompt to send.
        model_name (str): Optional model name override.

    Returns:
        str: The generated response from the model.
    """

    model_to_use = model_name or os.getenv("HF_MODEL", DEFAULT_MODEL)
    api_url = f"https://api-inference.huggingface.co/models/{model_to_use}"
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    if not hf_token:
        raise EnvironmentError("HUGGINGFACEHUB_API_TOKEN not found in environment variables.")

    headers = {
        "Authorization": f"Bearer {hf_token}"
    }

    payload = {"inputs": prompt}

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"[HF API ERROR] Status: {response.status_code}")
        print(f"[HF API ERROR] Response: {response.text}")
        raise RuntimeError(f"Hugging Face API failed: {response.status_code} – {response.text}")

    result = response.json()

    # Handle possible response shapes
    if isinstance(result, list):
        for r in result:
            if "generated_text" in r:
                return r["generated_text"]
    elif isinstance(result, dict) and "generated_text" in result:
        return result["generated_text"]

    raise ValueError(f"Unexpected response format from Hugging Face API: {result}")
