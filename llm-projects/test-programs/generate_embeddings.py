
import openai
import httpx
import json
import os

# Read API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

client = openai.OpenAI(
    api_key=api_key,
    http_client=httpx.Client(verify=False)  # Disable SSL verification for testing
)

input_path = "openai/input.txt"
output_path = "openai/embeddings.json"

if not os.path.exists(input_path):
    print(f"Input file '{input_path}' not found.")
    exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

# Prompt user for model size
model_choice = input("Choose embedding model size ('small' or 'large'): ").strip().lower()
if model_choice == "large":
    model_name = "text-embedding-3-large"
else:
    model_name = "text-embedding-3-small"

try:
    response = client.embeddings.create(
        input=text,
        model=model_name
    )
    embedding = response.data[0].embedding
    with open(output_path, "w", encoding="utf-8") as out:
        json.dump({"embedding": embedding, "model": model_name}, out, indent=2)
    print(f"Embedding saved to '{output_path}' using model '{model_name}'.")
except Exception as e:
    print("Failed to generate embedding.")
    print("Error:", e)
