from sqlalchemy import Column, Integer, Text, ForeignKey
from app.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)

    interview_id = Column(
        Integer,
        ForeignKey("interview_sessions.id")
    )

    question = Column(Text)
    answer = Column(Text)