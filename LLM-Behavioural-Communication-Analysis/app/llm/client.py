from ollama import chat
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")


def ask_llm(system_prompt: str, user_prompt: str):
    response = chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    format="json"
)

    return response.message.content