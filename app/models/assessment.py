from sqlalchemy import Column, Integer, String, Boolean, JSON
from app.database import Base

class AssessmentSession(Base):
    __tablename__ = "assessment_sessions"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, index=True)
    role = Column(String)

    current_question = Column(Integer, default=0)

    questions = Column(JSON)
    scores = Column(JSON, default=[])
    feedback = Column(JSON, default=[])

    completed = Column(Boolean, default=False)