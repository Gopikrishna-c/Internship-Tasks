from pydantic import BaseModel
from typing import List

class AssessmentRequest(BaseModel):
    email: str

class QuestionAnswer(BaseModel):
    question: str
    answer: str

class AssessmentSubmission(BaseModel):
    email: str
    answers: List[QuestionAnswer]

from pydantic import BaseModel

class AnswerRequest(BaseModel):
    email: str
    answer: str