from fastapi import FastAPI
from app.database import Base, engine
from app.models.user import User
from app.routers.auth import router as auth_router
from app.routers.resume import router as resume_router
from app.models.profile import CandidateProfile
from app.routers.profile import router as profile_router
from app.routers.gap import router as gap_router
from app.routers.role import router as role_router
from app.routers.assessment import router as assessment_router
from app.models.selected_role import SelectedRole
from app.models.assessment import AssessmentSession

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-Powered Candidate Intelligence Platform",
    version="1.0.0",
    description="Phase 1 MVP"
)

# Include Authentication Routes
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(profile_router)
app.include_router(gap_router)
app.include_router(role_router)
app.include_router(assessment_router)

@app.get("/")
def home():
    return {
        "project": "AI-Powered Candidate Intelligence Platform",
        "status": "Running"
    }

@app.get("/db-test")
def db_test():
    return {"status": "Database Connected"}