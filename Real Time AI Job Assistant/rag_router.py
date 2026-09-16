import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

from services.rag.rag_service import (
    index_document,
    answer_question
)


router = APIRouter()


# ==========================================
# Upload Document
# ==========================================

@router.post("/rag/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    # --------------------------------------
    # Check file type
    # --------------------------------------

    allowed_extensions = {
        ".pdf",
        ".docx",
        ".txt"
    }

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in allowed_extensions:

        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are supported"
        )

    # --------------------------------------
    # Create upload folder
    # --------------------------------------

    upload_folder = "uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    # --------------------------------------
    # Save uploaded file
    # --------------------------------------

    file_path = os.path.join(
        upload_folder,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    # --------------------------------------
    # Index Document
    # --------------------------------------

    try:

        result = index_document(
            file_path
        )

        return {
            "message": "Document uploaded and indexed successfully",
            "filename": file.filename,
            "total_chunks": result["total_chunks"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================
# Question Model
# ==========================================

class RAGQuestion(BaseModel):

    question: str


# ==========================================
# Ask Question
# ==========================================

@router.post("/rag/ask")
async def ask_question(
    request: RAGQuestion
):

    try:

        answer = answer_question(
            request.question
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )