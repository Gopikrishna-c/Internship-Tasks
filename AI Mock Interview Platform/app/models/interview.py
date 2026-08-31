from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id")
    )

    job_id = Column(
        Integer,
        ForeignKey("jobs.id")
    )

    status = Column(String, default="CREATED")

    mode = Column(String, default="text")