from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    required_skills = Column(Text)