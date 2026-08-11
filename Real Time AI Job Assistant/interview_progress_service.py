from sqlalchemy.orm import Session

from models.interview_progress import InterviewProgress


def save_interview_progress(
    db: Session,
    user_id: int,
    topic: str,
    status: str
):
    existing = (
        db.query(InterviewProgress)
        .filter(
            InterviewProgress.user_id == user_id,
            InterviewProgress.topic == topic
        )
        .first()
    )

    if existing:
        existing.status = status
    else:
        progress = InterviewProgress(
            user_id=user_id,
            topic=topic,
            status=status
        )

        db.add(progress)

    db.commit()

    return existing if existing else progress


def get_interview_progress(
    db: Session,
    user_id: int
):
    return (
        db.query(InterviewProgress)
        .filter(
            InterviewProgress.user_id == user_id
        )
        .all()
    )