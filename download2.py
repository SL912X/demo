from huggingface_hub import hf_hub_download

model_name = "bartowski/Llama-3.2-1B-Instruct-GGUF"
model_path = hf_hub_download(repo_id=model_name, filename="Llama-3.2-1B-Instruct-GGUF.Q4_K_M.gguf")  # Specifying a common GGUF file name
print(f"Model downloaded to: {model_path}")
