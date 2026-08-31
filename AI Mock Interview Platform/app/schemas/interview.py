from pydantic import BaseModel

class InterviewCreate(BaseModel):
    candidate_id: int
    job_id: int
    mode: str = "text"