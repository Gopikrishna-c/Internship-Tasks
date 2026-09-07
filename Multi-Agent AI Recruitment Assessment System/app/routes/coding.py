from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import CodingQuestion
from app.schemas import CodingQuestionCreate, CodingQuestionResponse

router = APIRouter(prefix="/coding", tags=["Coding Assessment"])


@router.post("/questions", response_model=CodingQuestionResponse)
async def create_question(
    request: CodingQuestionCreate,
    db: AsyncSession = Depends(get_db)
):
    question = CodingQuestion(**request.model_dump())

    db.add(question)
    await db.commit()
    await db.refresh(question)

    return question


@router.get("/questions")
async def get_questions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(CodingQuestion))
    return result.scalars().all()