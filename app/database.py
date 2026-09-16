from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create Async Engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

# Session Factory
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session