from sqlalchemy import Column, Integer, String, Text
from .database import Base


class ResumeAnalysis(Base):
    __tablename__ = "resume_analysis"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False, index=True)

    analysis_type = Column(String, nullable=False)

    analysis_result = Column(Text, nullable=False)