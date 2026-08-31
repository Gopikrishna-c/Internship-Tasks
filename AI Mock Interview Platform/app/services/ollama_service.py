import ollama
import json

MODEL = "llama3.2:3b"


# -----------------------------
# Generate First Interview Question
# -----------------------------
def generate_question(job_title, job_description, candidate_name, experience):

    prompt = f"""
You are a professional technical interviewer.

Candidate Name: {candidate_name}
Experience: {experience} year

Target Role:
{job_title}

Job Description:
{job_description}

Instructions:
- Ask only ONE interview question.
- Make it relevant to the job.
- Maximum 35 words.
- Do not provide the answer.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an AI technical interviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# -----------------------------
# Evaluate Candidate Answer
# -----------------------------
def evaluate_answer(question, answer):

    prompt = f"""
You are an AI technical interviewer.

Previous Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and generate the NEXT interview question.

Return ONLY this JSON.

{{
  "feedback": "short feedback",
  "follow_up": true,
  "next_question": "next interview question"
}}

Rules:
- Output only JSON.
- Do not use markdown.
- Never return null.
- The next question must depend on the candidate answer.
"""

    response = ollama.chat(
        model=MODEL,
        format="json",
        messages=[
            {
                "role": "system",
                "content": "Return only valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]
    print("OLLAMA OUTPUT:", content)

    return json.loads(content)