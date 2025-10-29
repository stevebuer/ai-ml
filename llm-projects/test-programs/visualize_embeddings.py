import json
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load embeddings from a JSON file
input_path = "openai/embeddings.json"
if not os.path.exists(input_path):
    print(f"Embedding file '{input_path}' not found.")
    exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Support both single and multiple embeddings
if isinstance(data, dict) and "embedding" in data:
    embeddings = [data["embedding"]]
    labels = [data.get("model", "embedding")]
elif isinstance(data, list):
    embeddings = [item["embedding"] for item in data]
    labels = [item.get("label", f"embedding_{i}") for i, item in enumerate(data)]
else:
    print("Invalid embedding file format.")
    exit(1)

embeddings = np.array(embeddings)

# Reduce to 2D using PCA
pca = PCA(n_components=2)
embeddings_2d = pca.fit_transform(embeddings)

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], c='blue', label='Embeddings')
for i, label in enumerate(labels):
    plt.annotate(label, (embeddings_2d[i, 0], embeddings_2d[i, 1]))
plt.title('2D Visualization of Embeddings (PCA)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
