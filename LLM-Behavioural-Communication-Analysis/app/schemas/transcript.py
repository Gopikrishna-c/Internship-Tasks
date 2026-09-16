from pydantic import BaseModel

class TranscriptInput(BaseModel):
    transcript: str

class QAPair(BaseModel):
    question_id: str
    question: str
    answer_id: str
    answer: str