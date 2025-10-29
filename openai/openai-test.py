
import os
from openai import OpenAI

# Read your API key from environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

# Create an OpenAI client
client = OpenAI(api_key=api_key)

# Send a simple test message
response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4o" if you have access
    messages=[
        {"role": "user", "content": "Hello! How are you today?"}
    ]
)

# Print the model’s reply
print(response.choices[0].message.content)

