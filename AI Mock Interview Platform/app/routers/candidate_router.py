from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate

router = APIRouter(prefix="/candidates", tags=["Candidates"])


@router.post("/")
def create_candidate(candidate: CandidateCreate,
                     db: Session = Depends(get_db)):

    new_candidate = Candidate(
        name=candidate.name,
        email=candidate.email,
        experience=candidate.experience,
        target_role=candidate.target_role
    )

    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)

    return new_candidate