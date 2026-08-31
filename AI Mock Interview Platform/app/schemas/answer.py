from pydantic import BaseModel

class AnswerCreate(BaseModel):
    question: str
    answer: str