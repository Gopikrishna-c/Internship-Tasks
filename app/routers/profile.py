from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.profile import CandidateProfile
from app.services.completeness import calculate_completeness
from app.services.recommendation import recommend_roles

router = APIRouter(
    prefix="/profile",
    tags=["Candidate Profile"]
)

@router.get("/{email}")
def get_profile(email: str, db: Session = Depends(get_db)):

    profile = db.query(CandidateProfile).filter(
        CandidateProfile.email == email
    ).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile
@router.get("/{email}/completeness")
def profile_completeness(
    email: str,
    db: Session = Depends(get_db)
):

    profile = db.query(CandidateProfile).filter(
        CandidateProfile.email == email
    ).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile_data = {
        "name": profile.name,
        "email": profile.email,
        "phone": profile.phone,
        "location": profile.location,
        "education": profile.education,
        "skills": profile.skills,
        "experience": profile.experience
    }

    return calculate_completeness(profile_data)
@router.get("/{email}/recommendations")
def role_recommendations(
    email: str,
    db: Session = Depends(get_db)
):

    profile = db.query(CandidateProfile).filter(
        CandidateProfile.email == email
    ).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile_data = {
        "skills": profile.skills
    }

    roles = recommend_roles(profile_data)

    return {
        "recommended_roles": roles
    }