
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from app.resume_parser import extract_text_from_pdf
from app.section_parser import extract_sections
from app.structured_parser import (
    parse_education,
    parse_skills,
    parse_experience
)
from app.missing_data import find_missing_data
from app.database import SessionLocal
from app.evaluator import evaluate_answer
from app.models import (
    Candidate,
    Profile,
    Resume,
    Assessment,
    Evaluation
)
from app.rag_engine import build_candidate_context
from app.question_generator import generate_questions

import shutil
import os
import re
import json


app = FastAPI()


# ==========================================
# Root Endpoint
# ==========================================

@app.get("/")
async def root():
    return {
        "message": "AI Candidate Assessment System"
    }


# ==========================================
# Answer Request Schema
# ==========================================

class AnswerRequest(BaseModel):
    question: str
    answer: str


# ==========================================
# Phase 1 + Phase 2
# Resume Upload and Processing
# ==========================================

@app.post("/resume/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    upload_folder = "uploads"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(
        upload_folder,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    # --------------------------------------
    # Phase 1 - Resume Parsing
    # --------------------------------------

    extracted_text = extract_text_from_pdf(
        file_path
    )

    sections = extract_sections(
        extracted_text
    )

    education = parse_education(
        sections["education"]
    )

    skills = parse_skills(
        sections["skills"]
    )

    experience = parse_experience(
        sections["experience"]
    )

    missing_data = find_missing_data(
        education,
        skills
    )

    # --------------------------------------
    # Extract Candidate Details
    # --------------------------------------

    lines = [
        line.strip()
        for line in extracted_text.splitlines()
        if line.strip()
    ]

    candidate_name = (
        lines[0]
        if lines
        else "Unknown Candidate"
    )

    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        extracted_text
    )

    candidate_email = (
        email_match.group(0)
        if email_match
        else None
    )

    # --------------------------------------
    # Phase 2 - PostgreSQL
    # --------------------------------------

    db = SessionLocal()

    try:

        # Check existing candidate

        candidate = None

        if candidate_email:

            candidate = (
                db.query(Candidate)
                .filter(
                    Candidate.email == candidate_email
                )
                .first()
            )

        # Create candidate

        if not candidate:

            candidate = Candidate(
                name=candidate_name,
                email=candidate_email
            )

            db.add(candidate)
            db.flush()

        # ----------------------------------
        # Save Profile
        # ----------------------------------

        profile = Profile(
            candidate_id=candidate.id,
            education_json=education,
            skills_json=skills,
            experience_json=experience
        )

        db.add(profile)

        # ----------------------------------
        # Save Resume
        # ----------------------------------

        resume_json = {
            "education": education,
            "skills": skills,
            "experience": experience
        }

        resume = Resume(
            candidate_id=candidate.id,
            filename=file.filename,
            raw_text=extracted_text,
            resume_json=resume_json
        )

        db.add(resume)

        db.commit()

        # ----------------------------------
        # Response
        # ----------------------------------

        return {
            "message": "Resume uploaded and saved successfully",
            "candidate_id": candidate.id,
            "filename": file.filename,
            "education": education,
            "skills": skills,
            "experience": experience,
            "missing_data": missing_data,
            "database_status": "Saved successfully",
            "sections": sections
        }

    except Exception as e:

        db.rollback()

        return {
            "message": "Database save failed",
            "error": str(e)
        }

    finally:

        db.close()


# ==========================================
# Phase 5
# Assessment Initiation
# ==========================================

@app.post("/assessment/start/{candidate_id}")
async def start_assessment(
    candidate_id: int
):

    db = SessionLocal()

    try:

        # ----------------------------------
        # Find Candidate
        # ----------------------------------

        candidate = (
            db.query(Candidate)
            .filter(
                Candidate.id == candidate_id
            )
            .first()
        )

        if not candidate:

            return {
                "message": "Candidate not found"
            }

        # ----------------------------------
        # Get Profile
        # ----------------------------------

        profile = (
            db.query(Profile)
            .filter(
                Profile.candidate_id == candidate_id
            )
            .first()
        )

        # ----------------------------------
        # Get Resume
        # ----------------------------------

        resume = (
            db.query(Resume)
            .filter(
                Resume.candidate_id == candidate_id
            )
            .first()
        )

        if not profile or not resume:

            return {
                "message": "Candidate profile or resume not found"
            }

        # ----------------------------------
        # Build Candidate Context
        # ----------------------------------

        candidate_context = build_candidate_context(
            profile.education_json,
            profile.skills_json,
            profile.experience_json,
            resume.raw_text
        )

        # ----------------------------------
        # Generate Questions
        # ----------------------------------

        questions = generate_questions(
            candidate_context
        )

        if not questions:

            return {
                "message": "No assessment questions generated"
            }

        # ----------------------------------
        # Create Assessment
        # ----------------------------------

        assessment = Assessment(
            candidate_id=candidate_id,
            score=0,
            feedback=""
        )

        db.add(assessment)

        db.commit()

        db.refresh(assessment)

        return {
            "message": "Assessment started successfully",
            "candidate_id": candidate_id,
            "assessment_id": assessment.id,
            "total_questions": len(questions),
            "questions": questions
        }

    finally:

        db.close()


# ==========================================
# Phase 5
# Candidate Answer + AI Evaluation
# ==========================================



@app.post("/assessment/answer/{candidate_id}")
async def submit_answer(
    candidate_id: int,
    request: AnswerRequest
):

    db = SessionLocal()

    try:

        # Check Candidate
        candidate = (
            db.query(Candidate)
            .filter(
                Candidate.id == candidate_id
            )
            .first()
        )

        if not candidate:
            return {
                "message": "Candidate not found"
            }

        # Get Latest Assessment
        assessment = (
            db.query(Assessment)
            .filter(
                Assessment.candidate_id == candidate_id
            )
            .order_by(
                Assessment.id.desc()
            )
            .first()
        )

        if not assessment:
            return {
                "message": "Assessment not started"
            }

        # AI Evaluation
        evaluation_result = evaluate_answer(
            request.question,
            request.answer
        )

        # Convert Gemini response to JSON
        try:

            cleaned_result = evaluation_result.strip()

            # Remove Markdown code fences
            if cleaned_result.startswith("```"):

                cleaned_result = cleaned_result.replace(
                    "```json",
                    ""
                )

                cleaned_result = cleaned_result.replace(
                    "```",
                    ""
                )

                cleaned_result = cleaned_result.strip()

            evaluation_data = json.loads(
                cleaned_result
            )

        except json.JSONDecodeError:

            return {
                "message": "Invalid evaluation response",
                "evaluation": evaluation_result
            }

        # Extract evaluation values
        score = int(
            evaluation_data.get(
                "score",
                0
            )
        )

        feedback = evaluation_data.get(
            "feedback",
            ""
        )

        logical_explanation = evaluation_data.get(
            "logical_explanation",
            ""
        )

        # Save Evaluation
        evaluation = Evaluation(
            assessment_id=assessment.id,
            question=request.question,
            answer=request.answer,
            logical_explanation=logical_explanation,
            score=score
        )

        db.add(evaluation)

        # Save latest score
        assessment.score = score
        assessment.feedback = feedback

        db.commit()

        db.refresh(evaluation)

        return {
            "message": "Answer evaluated and saved successfully",
            "candidate_id": candidate_id,
            "assessment_id": assessment.id,
            "evaluation_id": evaluation.id,
            "question": request.question,
            "answer": request.answer,
            "score": score,
            "feedback": feedback,
            "logical_explanation":
                logical_explanation
        }

    except Exception as e:

        db.rollback()

        return {
            "message": "Answer evaluation failed",
            "error": str(e)
        }

    finally:

        db.close()



@app.get("/assessment/result/{candidate_id}")
async def get_assessment_result(candidate_id: int):

    db = SessionLocal()

    try:

        # Find Candidate
        candidate = (
            db.query(Candidate)
            .filter(
                Candidate.id == candidate_id
            )
            .first()
        )

        if not candidate:
            return {
                "message": "Candidate not found"
            }

        # Get Latest Assessment
        assessment = (
            db.query(Assessment)
            .filter(
                Assessment.candidate_id == candidate_id
            )
            .order_by(
                Assessment.id.desc()
            )
            .first()
        )

        if not assessment:
            return {
                "message": "Assessment not found"
            }

        # Get All Evaluations
        evaluations = (
            db.query(Evaluation)
            .filter(
                Evaluation.assessment_id == assessment.id
            )
            .all()
        )

        if not evaluations:
            return {
                "message": "No evaluations found"
            }

        # Calculate Final Score
        total_score = sum(
            evaluation.score
            for evaluation in evaluations
        )

        final_score = round(
            total_score / len(evaluations),
            2
        )

        # Prepare Evaluation Details
        evaluation_details = []

        for evaluation in evaluations:

            evaluation_details.append({
                "evaluation_id": evaluation.id,
                "question": evaluation.question,
                "answer": evaluation.answer,
                "score": evaluation.score,
                "logical_explanation":
                    evaluation.logical_explanation
            })

        # Update Assessment Final Score
        assessment.score = final_score

        db.commit()

        return {
            "message": "Assessment result fetched successfully",
            "candidate_id": candidate_id,
            "candidate_name": candidate.name,
            "assessment_id": assessment.id,
            "total_questions": len(evaluations),
            "final_score": final_score,
            "evaluations": evaluation_details
        }

    except Exception as e:

        db.rollback()

        return {
            "message": "Failed to fetch assessment result",
            "error": str(e)
        }

    finally:

        db.close()



