from huggingface_hub import hf_hub_download

model_name = "CompendiumLabs/bge-base-en-v1.5-gguf"
model_path = hf_hub_download(repo_id=model_name, filename="bge-base-en-v1.5.gguf")
print(f"Model downloaded to: {model_path}")
