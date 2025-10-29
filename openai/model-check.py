
import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable not set.")

client = OpenAI(api_key=api_key)

models = client.models.list()

for m in models.data[:5]:
    print(m.id)

