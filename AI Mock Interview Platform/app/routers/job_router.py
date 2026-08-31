from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.job import Job
from app.schemas.job import JobCreate

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/")
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    new_job = Job(
        title=job.title,
        description=job.description,
        required_skills=job.required_skills
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job


@router.get("/")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()