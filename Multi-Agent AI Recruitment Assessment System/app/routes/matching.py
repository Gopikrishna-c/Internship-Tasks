from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Candidate, JobDescription
from app.schemas import (
    SkillGapRequest,
    SkillGapResponse,
    AutoMatchRequest,
)
from app.agents.matching_agent import semantic_skill_match

router = APIRouter(prefix="/matching", tags=["Matching"])


@router.post("/skill-gap", response_model=SkillGapResponse)
async def match_skills(
    request: SkillGapRequest,
    db: AsyncSession = Depends(get_db)
):
    candidate = await db.get(Candidate, request.candidate_id)

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return semantic_skill_match(
        candidate.skills,
        request.jd_skills
    )


@router.post("/auto-match", response_model=SkillGapResponse)
async def auto_match(
    request: AutoMatchRequest,
    db: AsyncSession = Depends(get_db)
):
    candidate = await db.get(Candidate, request.candidate_id)
    jd = await db.get(JobDescription, request.jd_id)

    if not candidate or not jd:
        raise HTTPException(status_code=404, detail="Data not found")

    return semantic_skill_match(
        candidate.skills,
        jd.required_skills
    )