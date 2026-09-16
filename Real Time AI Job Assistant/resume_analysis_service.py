from sqlalchemy.orm import Session

from models.resume_analysis import ResumeAnalysis


def save_resume_analysis(
    db: Session,
    user_id: int,
    analysis_type: str,
    analysis_result: str
):
    analysis = ResumeAnalysis(
        user_id=user_id,
        analysis_type=analysis_type,
        analysis_result=analysis_result
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return analysis


def get_resume_analysis_history(
    db: Session,
    user_id: int
):
    return (
        db.query(ResumeAnalysis)
        .filter(
            ResumeAnalysis.user_id == user_id
        )
        .order_by(ResumeAnalysis.id.desc())
        .all()
    )