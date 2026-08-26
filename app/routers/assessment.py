from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.attributes import flag_modified

from app.database import get_db
from app.models.selected_role import SelectedRole
from app.models.assessment import AssessmentSession

from app.schemas.assessment import AssessmentRequest, AnswerRequest

from app.services.gemini_service import (
    generate_interview_questions,
    generate_next_question,
    evaluate_single_answer
)
from app.services.benchmark import final_benchmark

router = APIRouter(
    prefix="/assessment",
    tags=["Adaptive Assessment"]
)


# ---------------- START ASSESSMENT ---------------- #

@router.post("/start")
def start_assessment(
    data: AssessmentRequest,
    db: Session = Depends(get_db)
):

    selected = db.query(SelectedRole).filter(
        SelectedRole.email == data.email
    ).first()

    if not selected:
        raise HTTPException(
            status_code=404,
            detail="Please select a role first"
        )

    # Generate only Question 1
    result = generate_interview_questions(selected.role)
    q1 = result["questions"][0]

    # Delete previous unfinished session
    db.query(AssessmentSession).filter(
        AssessmentSession.email == data.email,
        AssessmentSession.completed == False
    ).delete()

    session = AssessmentSession(
        email=data.email,
        role=selected.role,
        current_question=0,
        questions=[q1],
        scores=[],
        feedback=[],
        completed=False
    )

    db.add(session)
    db.commit()

    return {
        "email": data.email,
        "role": selected.role,
        "question_no": 1,
        "question": q1
    }


# ---------------- ANSWER QUESTION ---------------- #

@router.post("/answer")
def submit_answer(
    data: AnswerRequest,
    db: Session = Depends(get_db)
):

    session = db.query(AssessmentSession).filter(
        AssessmentSession.email == data.email,
        AssessmentSession.completed == False
    ).first()

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Assessment not started"
        )

    current = session.current_question

    # Safety check
    if current >= len(session.questions):
        raise HTTPException(
            status_code=400,
            detail="Question not generated. Please restart assessment."
        )

    question = session.questions[current]

    # Evaluate current answer
    result = evaluate_single_answer(
        session.role,
        question,
        data.answer
    )

    # Save score
    scores = list(session.scores)
    scores.append(result["score"])
    session.scores = scores
    flag_modified(session, "scores")

    # Save feedback
    feedback = list(session.feedback)
    feedback.append(result["feedback"])
    session.feedback = feedback
    flag_modified(session, "feedback")

    session.current_question += 1

    # -------- Generate Next Question --------
    if session.current_question < 5:

        next_q = generate_next_question(
            role=session.role,
            previous_question=question,
            previous_answer=data.answer,
            previous_score=result["score"],
            question_number=session.current_question + 1
        )

        questions = list(session.questions)
        questions.append(next_q["question"])
        session.questions = questions
        flag_modified(session, "questions")

        db.commit()

        return {
            "question_no": session.current_question + 1,
            "previous_score": result["score"],
            "feedback": result["feedback"],
            "question": next_q["question"]
        }

    # -------- Final Benchmark --------

    benchmark = final_benchmark([
        {"score": s} for s in session.scores
    ])

    session.completed = True
    db.commit()

    return {
        "completed": True,
        "scores": session.scores,
        "benchmark": benchmark
    }