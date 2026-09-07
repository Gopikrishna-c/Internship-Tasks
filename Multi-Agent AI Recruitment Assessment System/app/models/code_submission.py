from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base

class CodeSubmission(Base):
    __tablename__ = "code_submissions"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    question_id = Column(Integer, ForeignKey("coding_questions.id"))

    source_code = Column(Text)
    language = Column(String, default="python")
    status = Column(String, default="submitted")