from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import os

from app.database import get_db
from app.models import Candidate
from app.parser.resume_parser import extract_resume_data

router = APIRouter(prefix="/resume", tags=["Resume"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Parse resume
    data = extract_resume_data(file_path)

    # Check if candidate already exists
    result = await db.execute(
        select(Candidate).where(Candidate.email == data["email"])
    )
    candidate = result.scalar_one_or_none()

    if candidate:
        # Update existing candidate
        candidate.name = data["name"]
        candidate.phone = data["phone"]
        candidate.education = data["education"]
        candidate.experience = data["experience"]
        candidate.skills = data["skills"]
        candidate.projects = data["projects"]
        candidate.raw_text = data["raw_text"]

    else:
        # Create new candidate
        candidate = Candidate(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            education=data["education"],
            experience=data["experience"],
            skills=data["skills"],
            projects=data["projects"],
            raw_text=data["raw_text"]
        )
        db.add(candidate)

    await db.commit()
    await db.refresh(candidate)

    return {
        "candidate_id": candidate.id,
        "message": "Resume parsed and saved successfully",
        "data": data
    }