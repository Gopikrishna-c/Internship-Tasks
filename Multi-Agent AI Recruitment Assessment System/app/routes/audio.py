from fastapi import APIRouter, UploadFile, File
import os

from app.agents.whisper_agent import transcribe_audio
from app.agents.communication_agent import analyze_communication
from app.agents.star_agent import evaluate_star

router = APIRouter(prefix="/audio", tags=["Audio Screening"])

UPLOAD_DIR = "uploads/audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    result = transcribe_audio(file_path)

    communication = analyze_communication(
        result["transcript"]
    )

    star = evaluate_star(
        result["transcript"]
    )

    return {
        "filename": file.filename,
        **result,
        **communication,
        **star
    }