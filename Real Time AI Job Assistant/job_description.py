from sqlalchemy import Column, Integer, String, Text
from .database import Base


class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)