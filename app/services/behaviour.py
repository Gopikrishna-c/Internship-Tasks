import json
from app.llm.client import ask_llm
from app.llm.prompts import BEHAVIOUR_PROMPT
from app.services.normalizer import (
    normalize_assessment,
    normalize_confidence,
)


def analyze_behaviour(answer: str):
    result = ask_llm(
        BEHAVIOUR_PROMPT,
        f"Candidate Answer:\n{answer}"
    )

    try:
        data = json.loads(result)

        for item in data.values():
            item["assessment"] = normalize_assessment(
                item["assessment"]
            )
            item["confidence"] = normalize_confidence(
                item["confidence"]
            )

        return data

    except:
        return {
            "error": "Invalid JSON",
            "raw_response": result
        }