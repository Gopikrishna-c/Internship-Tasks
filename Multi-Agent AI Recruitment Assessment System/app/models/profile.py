from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class CandidateProfile(Base):
    __tablename__ = "candidate_profiles"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    location = Column(String)

    education = Column(JSON)
    skills = Column(JSON)
    experience = Column(JSON)