from fastapi import APIRouter, UploadFile, File
import os
import shutil

from services.resume_service import extract_text_from_pdf
from services.resume_ai_service import analyze_resume

from models.database import SessionLocal

from services.resume_analysis_service import (
    save_resume_analysis,
    get_resume_analysis_history
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload-resume")
def upload_resume(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename
    }


@router.get("/extract-resume")
def extract_resume():

    file_path = "uploads/resumee.pdf"

    text = extract_text_from_pdf(
        file_path
    )

    return {
        "message": "Resume text extracted successfully",
        "text": text
    }


@router.get("/analyze-resume")
def analyze_uploaded_resume(
    user_id: int = 1
):

    db = SessionLocal()

    try:

        file_path = "uploads/resumee.pdf"

        # Extract resume text
        resume_text = extract_text_from_pdf(
            file_path
        )

        # Analyze resume
        analysis = analyze_resume(
            resume_text
        )

        # Save analysis history
        save_resume_analysis(
            db,
            user_id,
            "resume_analysis",
            str(analysis)
        )

        return {
            "message": "Resume analyzed successfully",
            "analysis": analysis
        }

    finally:

        db.close()


@router.get("/resume-history")
def resume_history(
    user_id: int = 1
):

    db = SessionLocal()

    try:

        history = get_resume_analysis_history(
            db,
            user_id
        )

        return {
            "user_id": user_id,
            "total_analysis": len(history),
            "history": [
                {
                    "id": item.id,
                    "type": item.analysis_type,
                    "result": item.analysis_result
                }
                for item in history
            ]
        }

    finally:

        db.close()