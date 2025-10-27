# Test Programs for OpenAI API

This folder contains test scripts for learning and verifying OpenAI API functionality.

## Contents
- `test_openai_api.py`: Checks connectivity to the OpenAI API and lists available models.
- `generate_embeddings.py`: Generates embeddings for text files using OpenAI's embedding models.
- `visualize_embeddings.py`: Visualizes embeddings in 2D using PCA.

## Usage

### API Connectivity Test
1. Ensure your API key is saved in `openai/openai_api_key.txt`.
2. Run the script:
   ```powershell
   C:/STEVE/DEV/llm-projects/.venv/Scripts/python.exe openai/test-programs/test_openai_api.py
   ```

**Note:**
- The script disables SSL certificate verification for testing purposes. This is not recommended for production use.
- If you encounter SSL errors, see troubleshooting steps below.

### Troubleshooting SSL Errors
- Upgrade `certifi` and install `python-certifi-win32` to fix most certificate issues.
- If problems persist, you can temporarily disable SSL verification in the script (already applied).
- For production, resolve certificate issues and re-enable verification for security.

### Example Output
```
Successfully connected to OpenAI API.
Available models:
gpt-3.5-turbo
gpt-4o
...etc
```

### Embedding Visualization
1. Generate embeddings with `generate_embeddings.py`.
2. Run the visualization script:
   ```powershell
   C:/STEVE/DEV/llm-projects/.venv/Scripts/python.exe openai/test-programs/visualize_embeddings.py
   ```
3. A 2D scatter plot will be displayed, showing the embeddings projected with PCA.

This helps inspect clustering and relationships between texts.
