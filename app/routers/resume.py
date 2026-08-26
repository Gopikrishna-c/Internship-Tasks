from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os
import shutil

from app.database import get_db
from app.models.profile import CandidateProfile
from app.services.parser import extract_text, extract_profile
from app.services.rag import ingest_profile

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Save PDF
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract Resume
    resume_text = extract_text(file_path)
    profile = extract_profile(resume_text)

    # Check existing profile
    existing = db.query(CandidateProfile).filter(
        CandidateProfile.email == profile["email"]
    ).first()

    # Save to PostgreSQL
    if not existing:
        candidate = CandidateProfile(
            name=profile["name"],
            email=profile["email"],
            phone=profile["phone"],
            location=profile["location"],
            education=profile["education"],
            skills=profile["skills"],
            experience=profile["experience"]
        )

        db.add(candidate)
        db.commit()

    # Save to ChromaDB (RAG)
    ingest_profile(profile)

    return {
        "message": "Resume parsed & profile saved",
        "profile": profile
    }