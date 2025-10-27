import openai
import httpx
import traceback

# Read API key from file
with open("openai/openai_api_key.txt", "r") as f:
    api_key = f.read().strip()

# Disable SSL certificate verification (for testing only)
client = openai.OpenAI(
    api_key=api_key,
    http_client=httpx.Client(verify=False)
)

try:
    models = client.models.list()
    print("Successfully connected to OpenAI API.")
    print("Available models:")
    for model in models.data:
        print(model.id)
except Exception as e:
    print("Failed to connect to OpenAI API.")
    print(f"Exception type: {type(e).__name__}")
    print("Error:", e)
    print("Traceback:")
    traceback.print_exc()
