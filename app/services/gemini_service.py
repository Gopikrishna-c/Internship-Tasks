import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(prompt: str):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


def generate_interview_questions(role: str):

    prompt = f"""
You are a technical interviewer.

Target Role: {role}

Generate exactly 5 beginner to intermediate interview questions.

Return ONLY valid JSON.

{{
  "questions": [
    "Question 1",
    "Question 2",
    "Question 3",
    "Question 4",
    "Question 5"
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
def evaluate_single_answer(role: str, question: str, answer: str):

    prompt = f"""
You are a technical interviewer.

Role: {role}

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and return ONLY valid JSON.

{{
  "score": 8,
  "level": "Strong",
  "feedback": "Good understanding with clear explanation."
}}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)

def evaluate_five_answers(role: str, answers: list):

    prompt = f"""
You are a technical interviewer.

Role: {role}

Evaluate these 5 answers.

Answers:
{json.dumps(answers, indent=2)}

Return ONLY valid JSON.

{{
  "results":[
    {{
      "question":"...",
      "score":8,
      "feedback":"..."
    }}
  ]
}}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)

def final_benchmark(results):

    scores = [r["score"] for r in results]

    average = round(sum(scores) / len(scores), 1)

    if average >= 9:
        readiness = "Strong Entry-Level"
    elif average >= 7:
        readiness = "Entry-Level Ready"
    elif average >= 5:
        readiness = "Foundation"
    else:
        readiness = "Needs Improvement"

    return {
        "individual_scores": scores,
        "average_score": average,
        "readiness": readiness
    }

def generate_next_question(
    role: str,
    previous_question: str,
    previous_answer: str,
    previous_score: int,
    question_number: int
):
    prompt = f"""
You are an adaptive technical interviewer.

Target Role: {role}

Previous Question:
{previous_question}

Candidate Answer:
{previous_answer}

Score: {previous_score}/10

Generate ONLY the next interview question.

Rules:
- If score is 8-10: Increase difficulty.
- If score is 5-7: Keep medium difficulty.
- If score is 0-4: Ask an easier foundational question.
- This is Question {question_number} of 5.

Return JSON only.

{{
  "question":"Next interview question"
}}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)