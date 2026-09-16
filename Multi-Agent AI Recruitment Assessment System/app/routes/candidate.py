from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Candidate
from app.schemas import CandidateCreate, CandidateResponse

router = APIRouter(prefix="/candidates", tags=["Candidates"])


@router.post("/", response_model=CandidateResponse)
async def create_candidate(
    candidate: CandidateCreate,
    db: AsyncSession = Depends(get_db)
):
    new_candidate = Candidate(
        name=candidate.name,
        email=candidate.email,
        phone=candidate.phone,
        education=candidate.education,
        experience=candidate.experience,
        skills=candidate.skills,
        projects=candidate.projects
    )

    db.add(new_candidate)
    await db.commit()
    await db.refresh(new_candidate)

    return new_candidate


@router.get("/", response_model=list[CandidateResponse])
async def get_candidates(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Candidate))
    candidates = result.scalars().all()
    return candidates