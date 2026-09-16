import os
import time

from dotenv import load_dotenv
from google import genai

from app.chat_memory import get_chat_history


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def generate_followup_question(candidate_id: int, candidate_context: str):

    history = get_chat_history(candidate_id)

    conversation = ""

    for message in history:
        conversation += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    prompt = f"""
You are an AI technical interviewer.

Candidate Context:
{candidate_context}

Previous Conversation:
{conversation}

Generate ONE relevant follow-up technical question.

Rules:
1. Use the candidate's previous answer.
2. Ask a deeper question related to the same technical topic.
3. Do not repeat the previous question.
4. Keep the question clear and interview-friendly.
5. Return ONLY the question.
"""

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:

            if "503" in str(e) and attempt < 2:
                print("Gemini temporarily unavailable. Retrying...")
                time.sleep(5)

            else:
                raise


if __name__ == "__main__":

    candidate_id = 1

    candidate_context = """
    Candidate Project:
    AI Recruitment System

    Technologies:
    Python, FastAPI, Scikit-learn,
    CountVectorizer and Cosine Similarity.
    """

    question = generate_followup_question(
        candidate_id,
        candidate_context
    )

    print("Dynamic Follow-up Question:")
    print(question)