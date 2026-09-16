from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine
from app.routes.transcript import router as transcript_router

app = FastAPI(title="LLM Behaviour Analysis API")

app.include_router(transcript_router)


@app.get("/")
async def home():
    return {"message": "API is Running"}


@app.get("/db-test")
async def db_test():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"status": "Database Connected"}