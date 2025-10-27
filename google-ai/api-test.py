import os
from google import genai
from google.genai.errors import APIError

# --- Configuration ---
# The Client() constructor automatically looks for the GEMINI_API_KEY environment variable.
# To set it manually in the code for testing, uncomment the line below and replace 'YOUR_API_KEY_HERE'
# with your actual key. It is generally safer to use environment variables.
# client = genai.Client(api_key="YOUR_API_KEY_HERE")

def run_api_test():
    """
    Initializes the Gemini Client and attempts to run a simple text generation task.
    """
    print("--- Starting Gemini API Key Test ---")

    # 1. Initialize Client
    try:
        # Client will automatically pick up the GEMINI_API_KEY environment variable.
        client = genai.Client()
        print("Client initialized successfully.")
    except Exception as e:
        print(f"Error during client initialization. Is the 'google-genai' package installed?")
        print(f"Details: {e}")
        print("\nInstall with: pip install google-genai")
        return

    # Check if the API Key was effectively provided
    if not client.api_key:
        print("\nAPI Key not found!")
        print("Please ensure you have set the GEMINI_API_KEY environment variable.")
        print("  - On Linux/macOS: export GEMINI_API_KEY='YOUR_KEY'")
        print("  - On Windows (CMD): set GEMINI_API_KEY=YOUR_KEY")
        print("Or uncomment and modify the 'client = genai.Client(api_key=...)' line in the script.")
        return

    # 2. Define Test Prompt and Model
    model = 'gemini-2.5-flash'
    prompt = "Why is testing an API key important? Respond in one concise sentence."

    print(f"\nAttempting to call model '{model}' with prompt: '{prompt}'")

    # 3. Make API Call
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )

        # 4. Print Results
        print("\n--- API Call Successful! ---")
        print("✅ Your API Key is working correctly.")
        print("\nGenerated Response:")
        print(response.text.strip())

    except APIError as e:
        print("\n--- API Call Failed! ---")
        print(f"❌ An API Error occurred (Likely due to an invalid key or permissions).")
        print(f"Error Details: {e}")
        print("\nPlease check that your API key is correct and active.")

    except Exception as e:
        print("\n--- An Unexpected Error Occurred! ---")
        print(f"Error Details: {e}")

if __name__ == "__main__":
    run_api_test()
