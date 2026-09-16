import os
import uuid

from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from models.database import get_db
from models.user import User

from routes.auth import get_current_user

from services.stt_service import speech_to_text
from services.tts_service import text_to_speech
from services.ai_orchestrator import orchestrate


# ==================================================
# Router
# ==================================================

router = APIRouter()


# ==================================================
# Voice Chat
# ==================================================

@router.post("/voice-chat")
async def voice_chat(
    audio: UploadFile = File(...),

    current_user: User = Depends(
        get_current_user
    ),

    db: Session = Depends(
        get_db
    )
):

    # ==================================================
    # User ID
    # ==================================================

    user_id = current_user.id


    # ==================================================
    # Temporary Files
    # ==================================================

    file_id = str(uuid.uuid4())

    temp_file = f"temp_{file_id}_{audio.filename}"

    output_file = f"response_{file_id}.mp3"


    try:

        # ==================================================
        # 1. Save Uploaded Audio
        # ==================================================

        with open(
            temp_file,
            "wb"
        ) as buffer:

            buffer.write(
                await audio.read()
            )


        # ==================================================
        # 2. Speech → Text
        # ==================================================

        user_message = speech_to_text(
            temp_file
        )


        # ==================================================
        # 3. AI Orchestration
        # ==================================================

        result = await orchestrate(

            db=db,

            user_id=user_id,

            user_message=user_message

        )


        # ==================================================
        # 4. Get AI Response
        # ==================================================

        response = result["response"]


        # ==================================================
        # 5. Text → Speech
        # ==================================================

        await text_to_speech(

            response,

            output_file

        )


        # ==================================================
        # 6. Return Audio
        # ==================================================

        return FileResponse(

            output_file,

            media_type="audio/mpeg",

            filename="ai_response.mp3"

        )


    finally:

        # ==================================================
        # Delete Temporary Input
        # ==================================================

        if os.path.exists(
            temp_file
        ):

            os.remove(
                temp_file
            )