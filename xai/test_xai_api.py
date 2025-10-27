import requests
import warnings

# Suppress SSL warnings for testing purposes
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

# Read the API key from the file
with open('xai_api_key.txt', 'r') as f:
    api_key = f.read().strip()

# Set up headers with the API key
headers = {'Authorization': f'Bearer {api_key}'}

# Test the API key by listing models
try:
    response = requests.get('https://api.x.ai/v1/models', headers=headers, verify=False)
    if response.status_code == 200:
        print("API key is valid.")
        models = response.json()
        print("Available models:", models)
    else:
        print(f"API key is invalid. Status code: {response.status_code}")
        print("Response:", response.text)
except Exception as e:
    print(f"An error occurred: {e}")