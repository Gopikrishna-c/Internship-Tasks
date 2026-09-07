from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import os

from app.database import get_db
from app.models import JobDescription
from app.parser.jd_parser import extract_jd_data

router = APIRouter(prefix="/jd", tags=["Job Description"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_jd(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    data = extract_jd_data(file_path)

    jd = JobDescription(
        title=data["title"],
        company=data["company"],
        required_skills=data["required_skills"],
        raw_text=data["raw_text"]
    )

    db.add(jd)
    await db.commit()
    await db.refresh(jd)

    return {
        "jd_id": jd.id,
        "message": "Job Description parsed successfully",
        "data": data
    }