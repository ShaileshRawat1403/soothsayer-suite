from tools.hf_inference import query_huggingface

if __name__ == "__main__":
    result = query_huggingface("The future of AI agents is", model_name="gpt2")
    print("📤 Hugging Face says:\n", result)
