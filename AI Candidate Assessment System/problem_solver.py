import os
from dotenv import load_dotenv
from google import genai
from app.evaluator import evaluate_answer

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_problem_scenario(candidate_context: str):

    prompt = f"""
You are an AI technical interviewer.

Candidate Context:
{candidate_context}

Create ONE practical programming/problem-solving scenario
based on the candidate's project experience.

Rules:
1. The scenario must be related to the candidate's project.
2. It should test practical problem-solving ability.
3. Do not ask a theoretical definition question.
4. Keep it simple and interview-friendly.
5. Return ONLY the scenario question.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()


if __name__ == "__main__":

    candidate_context = """
    Candidate Project:
    AI Recruitment System

    Technologies:
    Python, FastAPI, Scikit-learn,
    CountVectorizer and Cosine Similarity.

    The system recommends suitable candidates
    based on skill similarity.
    """

    question = generate_problem_scenario(
        candidate_context
    )

    print("Problem-Solving Scenario:")
    print(question)

    candidate_answer = """
    I would normalize the skills before using CountVectorizer.
    For example, I can convert "React.js" and "ReactJS" into
    the same standard term like "ReactJS". I can also use
    lowercase conversion, punctuation removal and a skill
    mapping dictionary to improve matching accuracy.
    """

    evaluation = evaluate_answer(
        question,
        candidate_answer
    )

    print("\nProblem-Solving Evaluation:")
    print(evaluation)