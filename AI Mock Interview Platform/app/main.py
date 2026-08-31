from fastapi import FastAPI

from app.database import Base, engine
from app.models import *

from app.routers import (
    job_router,
    candidate_router,
    interview_router
)

app = FastAPI(title="AI Mock Interview Platform")

Base.metadata.create_all(bind=engine)

app.include_router(job_router.router)
app.include_router(candidate_router.router)
app.include_router(interview_router.router)


@app.get("/")
def home():
    return {"message": "Running"}