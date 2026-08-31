from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str
    email: str
    experience: int
    target_role: str