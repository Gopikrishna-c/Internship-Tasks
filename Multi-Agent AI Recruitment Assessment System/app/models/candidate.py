from sqlalchemy import Column, Integer, String, JSON, Text
from app.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String, nullable=True)

    education = Column(JSON)
    experience = Column(JSON)
    skills = Column(JSON)
    projects = Column(JSON)
    raw_text = Column(Text)