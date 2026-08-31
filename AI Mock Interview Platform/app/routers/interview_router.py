from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.interview import InterviewSession
from app.models.candidate import Candidate
from app.models.job import Job
from app.schemas.interview import InterviewCreate
from app.services.ollama_service import generate_question
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate
from app.services.ollama_service import evaluate_answer
from app.services.report_service import generate_report

TOTAL_QUESTIONS = 10
# Router create பண்ணணும்
router = APIRouter(
    prefix="/mock-interviews",
    tags=["Mock Interview"]
)

# Step 4 - Create Interview Session
@router.post("/")
def create_session(data: InterviewCreate,
                   db: Session = Depends(get_db)):

    candidate = db.query(Candidate).filter(
        Candidate.id == data.candidate_id
    ).first()

    if not candidate:
        raise HTTPException(404, "Candidate not found")

    job = db.query(Job).filter(
        Job.id == data.job_id
    ).first()

    if not job:
        raise HTTPException(404, "Job not found")

    session = InterviewSession(
        candidate_id=data.candidate_id,
        job_id=data.job_id,
        status="CREATED",
        mode=data.mode
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return {
        "interview_id": session.id,
        "status": session.status
    }

# Step 5 - Start Interview
@router.post("/{interview_id}/start")
def start_interview(interview_id: int,
                    db: Session = Depends(get_db)):

    session = db.query(InterviewSession).filter(
        InterviewSession.id == interview_id
    ).first()

    if not session:
        raise HTTPException(404, "Interview not found")

    candidate = db.query(Candidate).get(session.candidate_id)
    job = db.query(Job).get(session.job_id)

    question = generate_question(
        job.title,
        job.description,
        candidate.name,
        candidate.experience
    )

    session.status = "QUESTIONING"
    db.commit()

    return {
    "interview_id": session.id,
    "status": session.status,
    "question_number": 1,
    "question": question
}

@router.post("/{interview_id}/answers")
def submit_answer(
    interview_id: int,
    data: AnswerCreate,
    db: Session = Depends(get_db)
):
    session = db.query(InterviewSession).filter(
        InterviewSession.id == interview_id
    ).first()

    if not session:
        raise HTTPException(404, "Interview not found")

    # Save candidate answer
    new_answer = Answer(
        interview_id=interview_id,
        question=data.question,
        answer=data.answer
    )

    db.add(new_answer)
    db.commit()

    # Count answered questions
    answer_count = db.query(Answer).filter(
        Answer.interview_id == interview_id
    ).count()

    # Evaluate current answer
    result = evaluate_answer(
        data.question,
        data.answer
    )

    # End interview after 10 questions
    if answer_count >= TOTAL_QUESTIONS:
        session.status = "COMPLETED"
        db.commit()

        candidate = db.query(Candidate).filter(
            Candidate.id == session.candidate_id
        ).first()

        return {
            "interview_id": interview_id,
            "status": "COMPLETED",
            "question_number": answer_count,
            "feedback": result.get("feedback", ""),
            "message": f"Thank you, {candidate.name}! Your AI Mock Interview has been completed successfully.",
            "report_available": True
        }

    # Continue interview
    return {
        "interview_id": interview_id,
        "status": "QUESTIONING",
        "question_number": answer_count,
        "feedback": result.get("feedback", ""),
        "follow_up": result.get("follow_up", False),
        "next_question": result.get("next_question", "")
    }
@router.get("/{interview_id}/report")
def interview_report(
    interview_id: int,
    db: Session = Depends(get_db)
):

    answers = db.query(Answer).filter(
        Answer.interview_id == interview_id
    ).all()

    if not answers:
        raise HTTPException(404, "No answers found")

    transcript = ""

    for item in answers:
        transcript += f"""
Question: {item.question}
Answer: {item.answer}

"""

    report = generate_report(transcript)

    return report