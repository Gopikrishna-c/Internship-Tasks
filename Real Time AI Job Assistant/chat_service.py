import os

from dotenv import load_dotenv
from google import genai

from services.prompt_builder import build_prompt


# ==================================================
# Environment
# ==================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# ==================================================
# Gemini Client
# ==================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ==================================================
# Generate Response
# ==================================================

async def generate_response(
    user_message: str,
    conversation_history=None,
    long_term_memories=None,
    interview_progress=None,
    vector_context=None
):

    # ----------------------------------------------
    # Build Final Prompt
    # ----------------------------------------------

    prompt = build_prompt(
        user_message=user_message,
        conversation_history=conversation_history,
        long_term_memories=long_term_memories,
        interview_progress=interview_progress,
        vector_context=vector_context
    )

    # ----------------------------------------------
    # Send Prompt to Gemini
    # ----------------------------------------------

    response = await client.aio.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    # ----------------------------------------------
    # Return AI Response
    # ----------------------------------------------

    return response.text