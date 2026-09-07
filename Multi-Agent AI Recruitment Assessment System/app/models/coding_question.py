from sqlalchemy import Column, Integer, String, JSON, Text
from app.database import Base

class CodingQuestion(Base):
    __tablename__ = "coding_questions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)

    problem_statement = Column(Text, nullable=False)
    starter_code = Column(Text)

    test_cases = Column(JSON)
    expected_output = Column(JSON)