from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import CodeSubmission
from app.schemas import (
    CodeSubmissionCreate,
    CodeSubmissionResponse
)

router = APIRouter(prefix="/submission", tags=["Code Submission"])


@router.post("", response_model=CodeSubmissionResponse)
async def submit_code(
    request: CodeSubmissionCreate,
    db: AsyncSession = Depends(get_db)
):
    submission = CodeSubmission(
        candidate_id=request.candidate_id,
        question_id=request.question_id,
        source_code=request.source_code
    )

    db.add(submission)
    await db.commit()
    await db.refresh(submission)

    return submission