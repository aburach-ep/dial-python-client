import requests
from urllib.parse import urlencode
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
print(os.environ)

API_URL = "https://ai-proxy.lab.epam.com/openai/deployments/"
FOUNDATION_MODEL = "o3-mini-2025-01-31"
CHAT_COMPLETIONS_URL = "/chat/completions"
API_KEY = os.getenv('API_KEY')
API_VERSION = "2024-12-01-preview"

HEADERS = {
    "Api-Key": f"{API_KEY}",
    "Content-Type": "application/json"
}

def ask_dial(question):
    payload = {
        "model": "gpt-3.5-turbo",  # or the model specified by DIAL, check docs if different
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    params = {"api-version": API_VERSION}

    compoundUrl = f"{API_URL}{FOUNDATION_MODEL}{CHAT_COMPLETIONS_URL}?{urlencode(params)}"
    response = requests.post(compoundUrl, headers=HEADERS, json=payload)
    response.raise_for_status()
    data = response.json()
    # The structure may vary; adjust as per actual API response
    return data["choices"][0]["message"]["content"]

def main():
    print("Ask me anything! (Ctrl+C to exit)")
    while True:
        try:
            question = input("You: ")
            if not question.strip():
                continue
            answer = ask_dial(question)
            print("DIAL:", answer)
        except KeyboardInterrupt:
            print("\nExiting.")
            break
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()