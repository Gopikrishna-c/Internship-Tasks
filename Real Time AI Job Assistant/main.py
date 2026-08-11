from fastapi import FastAPI

from models.database import Base, engine

from models.user import User
from models.user_memory import UserMemory
from models.resume_analysis import ResumeAnalysis
from models.job_description import JobDescription


from routes.auth import router as auth_router
from routes.chat import router as chat_router
from routes.resume import router as resume_router
from routes.jd import router as jd_router
from routes.voice_router import router as voice_router
from routes.rag_router import router as rag_router


# ==================================================
# Create FastAPI Application
# ==================================================

app = FastAPI(

    title="Real-Time AI Job Assistant",

    description=(
        "AI-powered job assistant with "
        "conversational AI, memory, "
        "resume analysis, JD intelligence "
        "and voice assistant"
    ),

    version="1.0.0"
)


# ==================================================
# Create Database Tables
# ==================================================

Base.metadata.create_all(
    bind=engine
)


# ==================================================
# Authentication
# ==================================================

app.include_router(

    auth_router,

    prefix="/auth",

    tags=["Authentication"]

)


# ==================================================
# AI Chat
# ==================================================

app.include_router(

    chat_router,

    prefix="/api",

    tags=["Chat"]

)


# ==================================================
# Resume
# ==================================================

app.include_router(

    resume_router,

    prefix="/resume",

    tags=["Resume"]

)


# ==================================================
# Job Description
# ==================================================

app.include_router(

    jd_router,

    prefix="/jd",

    tags=["Job Description"]

)


# ==================================================
# Voice Assistant
# ==================================================

app.include_router(

    voice_router,

    prefix="/voice",

    tags=["Voice Assistant"]

)

app.include_router(
    rag_router
)

# ==================================================
# Home
# ==================================================

@app.get("/")
def home():

    return {

        "message":
        "Welcome to Real-Time AI Job Assistant"

    }