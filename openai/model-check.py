from openai import OpenAI

with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

client = OpenAI(api_key=api_key)

models = client.models.list()

for m in models.data[:5]:
    print(m.id)

