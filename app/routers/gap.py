from fastapi import APIRouter
from app.services.gemini_service import ask_gemini

router = APIRouter(
    prefix="/gap",
    tags=["Gap Filling"]
)

@router.post("/question")
def generate_question():

    prompt = """
    Candidate profile is missing:
    - Certifications
    - Career Preference

    Ask only ONE short professional question.
    """

    question = ask_gemini(prompt)

    return {
        "question": question
    }