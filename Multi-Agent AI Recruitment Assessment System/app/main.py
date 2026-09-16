from fastapi import FastAPI

from app.database import engine, Base
from app import models

from app.routes.candidate import router as candidate_router
from app.routes.resume import router as resume_router
from app.routes.job_description import router as jd_router
from app.routes.matching import router as matching_router
from app.routes.coding import router as coding_router
from app.routes.code_submission import router as submission_router
from app.routes.code_execution import router as execution_router
from app.routes.fair_scoring import router as fair_router
from app.routes.audio import router as audio_router
from app.routes.hr import router as hr_router

app = FastAPI(title="Multi-Agent AI Recruitment Assessment System")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(candidate_router)
app.include_router(resume_router)
app.include_router(jd_router)
app.include_router(matching_router)
app.include_router(coding_router)
app.include_router(submission_router)
app.include_router(execution_router)
app.include_router(fair_router)
app.include_router(audio_router)
app.include_router(hr_router)

@app.get("/")
async def root():
    return {"message": "API Running Successfully"}
