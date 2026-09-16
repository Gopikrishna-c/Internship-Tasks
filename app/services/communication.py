import json
from app.llm.client import ask_llm
from app.llm.prompts import COMMUNICATION_PROMPT

def analyze_communication(answer: str):
    result = ask_llm(COMMUNICATION_PROMPT, f"Candidate Answer:\n{answer}")

    try:
        data = json.loads(result)

        # Convert all scores to int
        for key in data:
            data[key] = int(data[key])

        return data

    except:
        return {
            "clarity": 0,
            "relevance": 0,
            "structure": 0,
            "conciseness": 0,
            "professional_communication": 0
        }