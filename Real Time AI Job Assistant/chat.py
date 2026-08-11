from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from models.database import get_db
from models.user import User

from routes.auth import get_current_user

from services.ai_orchestrator import orchestrate


# ==================================================
# Router
# ==================================================

router = APIRouter()


# ==================================================
# Request Model
# ==================================================

class ChatRequest(BaseModel):

    message: str
    job_id: int


# ==================================================
# AI Chat
# ==================================================

@router.post("/chat")
async def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    # ------------------------------------------
    # Get logged-in user's ID
    # ------------------------------------------

    user_id = current_user.id

    # ------------------------------------------
    # AI Orchestration
    # ------------------------------------------

    result = await orchestrate(

        db=db,

        user_id=user_id,

        user_message=request.message,

        job_id=request.job_id

    )

    # ------------------------------------------
    # Return Response
    # ------------------------------------------

    return result