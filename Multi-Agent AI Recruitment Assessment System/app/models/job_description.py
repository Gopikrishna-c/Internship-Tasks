from sqlalchemy import Column, Integer, String, JSON, Text
from app.database import Base

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    company = Column(String, nullable=True)
    required_skills = Column(JSON)
    raw_text = Column(Text)