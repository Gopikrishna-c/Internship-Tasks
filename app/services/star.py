import json
from app.llm.client import ask_llm
from app.llm.prompts import STAR_PROMPT
from app.services.star_normalizer import normalize_star

def analyze_star(answer: str):
    result = ask_llm(STAR_PROMPT, f"Candidate Answer:\n{answer}")
    data = json.loads(result)
    return normalize_star(data)