from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Candidate, JobDescription, CodeSubmission
from app.agents.matching_agent import semantic_skill_match
from app.agents.code_execution_agent import execute_solution
from app.agents.complexity_agent import calculate_complexity
from app.agents.edge_case_agent import evaluate_edge_cases
from app.agents.fair_scoring_agent import generate_fair_report

router = APIRouter(prefix="/assessment", tags=["Fair Scoring"])


@router.get(
    "/fair-report/{candidate_id}/{jd_id}"
)
async def fair_report(
    candidate_id: int,
    jd_id: int,
    db: AsyncSession = Depends(get_db)
):
    candidate = await db.get(Candidate, candidate_id)
    jd = await db.get(JobDescription, jd_id)

    if not candidate or not jd:
        raise HTTPException(404, "Data not found")

    submission = await db.get(CodeSubmission, 1)

    if not submission:
        raise HTTPException(404, "Submission not found")

    skill = semantic_skill_match(
        candidate.skills,
        jd.required_skills
    )

    execution = execute_solution(
        submission.source_code,
        ["hello", "python"],
        ["olleh", "nohtyp"]
    )

    complexity = calculate_complexity(
        submission.source_code
    )

    edge = evaluate_edge_cases(
        submission.source_code
    )

    metrics = {
        "score": execution["score"],
        "skill_match": skill["match_percentage"],
        "edge_case_score": edge["edge_case_score"],
        "grade": complexity["grade"]
    }

    return generate_fair_report(candidate, metrics)