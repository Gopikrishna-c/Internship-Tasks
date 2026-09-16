import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY LOADED:", bool(api_key))

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(
    api_key=api_key
)


def evaluate_answer(question: str, answer: str):

    prompt = f"""
You are an AI candidate assessment evaluator.

Evaluate the candidate's answer.

Question:
{question}

Candidate Answer:
{answer}

Return only JSON in this format:

{{
    "score": 1,
    "accuracy": "Good",
    "feedback": "Short feedback",
    "logical_explanation": "Explain why this score was given"
}}

Score must be between 1 and 10.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":

    question = "How did you use FastAPI in your AI Recruitment System?"

    answer = """
    I used FastAPI to build REST APIs for
    candidate recommendation.
    """

    result = evaluate_answer(question, answer)

    print("AI Evaluation:")
    print(result)