from openai import OpenAI

# Read your API key from a local text file
# (Make sure the file contains only your key and nothing else)
with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

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

