import os
from dotenv import load_dotenv
from google import genai
import argparse


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("API key not found.")

    client = genai.Client(api_key=api_key)
    print("Hello from ai-agent!")
    print(f"API key: {api_key}")
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    prompt = args.user_prompt
    print(f"User prompt: {prompt}")

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    usage = response.usage_metadata 
    if not usage:
        raise RuntimeError("Failed API request.")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")

    print(f"Response: \n {response.text}")


if __name__ == "__main__":
    main()
