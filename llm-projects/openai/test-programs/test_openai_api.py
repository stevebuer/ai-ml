
import openai
import httpx
import traceback
import os

# Read API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

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
