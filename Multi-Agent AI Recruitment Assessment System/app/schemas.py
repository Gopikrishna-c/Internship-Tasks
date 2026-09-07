from pydantic import BaseModel, EmailStr
from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class CandidateCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    education: List[str] = []
    experience: List[str] = []
    skills: List[str] = []
    projects: List[str] = []

class SkillGapRequest(BaseModel):
    candidate_id: int
    jd_skills: list[str]

class SkillGapResponse(BaseModel):
    match_percentage: float
    matched_skills: list[str]
    missing_skills: list[str]

class MatchedSkill(BaseModel):
    jd_skill: str
    resume_skill: str
    similarity: float


class SkillGapResponse(BaseModel):
    match_percentage: float
    matched_skills: list[MatchedSkill]
    missing_skills: list[str]

class AutoMatchRequest(BaseModel):
    candidate_id: int
    jd_id: int

class CodingQuestionCreate(BaseModel):
    title: str
    difficulty: str
    problem_statement: str
    starter_code: str
    test_cases: list
    expected_output: list


class CodingQuestionResponse(CodingQuestionCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

class CodeSubmissionCreate(BaseModel):
    candidate_id: int
    question_id: int
    source_code: str


class CodeSubmissionResponse(CodeSubmissionCreate):
    id: int
    language: str
    status: str

    model_config = ConfigDict(from_attributes=True)

class FairReportResponse(BaseModel):
    candidate_id: int
    masked: bool
    technical_score: float
    skill_match: float
    edge_case_score: float
    complexity: str
    overall_score: float

class CandidateResponse(CandidateCreate):
    id: int
    raw_text: str | None = None

    class Config:
        from_attributes = True

        