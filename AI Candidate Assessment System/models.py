from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(150), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    profile = relationship("Profile", back_populates="candidate", uselist=False)
    resumes = relationship("Resume", back_populates="candidate")
    assessments = relationship("Assessment", back_populates="candidate")


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))

    education_json = Column(JSON)
    skills_json = Column(JSON)
    experience_json = Column(JSON)

    candidate = relationship("Candidate", back_populates="profile")


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))

    filename = Column(String(255))
    raw_text = Column(Text)
    resume_json = Column(JSON)

    candidate = relationship("Candidate", back_populates="resumes")


class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"))

    score = Column(Integer)
    feedback = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    candidate = relationship("Candidate", back_populates="assessments")
    evaluations = relationship("Evaluation", back_populates="assessment")


class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    assessment_id = Column(Integer, ForeignKey("assessments.id"))

    question = Column(Text)
    answer = Column(Text)
    logical_explanation = Column(Text)
    score = Column(Integer)

    assessment = relationship("Assessment", back_populates="evaluations")