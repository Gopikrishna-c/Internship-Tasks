from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)

    interview_id = Column(
        Integer,
        ForeignKey("interview_sessions.id")
    )

    competency = Column(String)
    question_type = Column(String)
    text = Column(Text)