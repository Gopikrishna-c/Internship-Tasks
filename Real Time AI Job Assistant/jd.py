import os

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from pypdf import PdfReader

from models.database import get_db

from models.job_description import JobDescription

from services.jd_service import clean_jd_text

from services.jd_embedding_service import (
    create_jd_embeddings
)

from services.jd_vector_service import (
    store_jd_embeddings
)

from services.jd_retriever_service import (
    retrieve_jd_chunks
)

from services.jd_rag_service import (
    answer_jd_question
)


router = APIRouter()


# ==================================================
# Upload Directory
# ==================================================

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


# ==================================================
# Upload Job Description
# ==================================================

@router.post("/upload-jd")
async def upload_jd(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # ------------------------------------------
    # Check PDF
    # ------------------------------------------

    if not file.filename.lower().endswith(".pdf"):

        raise HTTPException(

            status_code=400,

            detail="Only PDF files are allowed"

        )


    # ------------------------------------------
    # File Path
    # ------------------------------------------

    file_path = os.path.join(

        UPLOAD_DIR,

        file.filename

    )


    # ------------------------------------------
    # Save PDF
    # ------------------------------------------

    with open(
        file_path,
        "wb"
    ) as buffer:

        buffer.write(
            await file.read()
        )


    # ------------------------------------------
    # Extract Text
    # ------------------------------------------

    reader = PdfReader(
        file_path
    )

    text = ""


    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"


    # ------------------------------------------
    # Validate Text
    # ------------------------------------------

    if not text.strip():

        raise HTTPException(

            status_code=400,

            detail="Could not extract text from the PDF"

        )


    # ------------------------------------------
    # Create Job Record
    # ------------------------------------------

    job = JobDescription(
    title="string",
    filename=file.filename,
    content=text
)


    db.add(job)

    db.commit()

    db.refresh(job)


    # ------------------------------------------
    # Response
    # ------------------------------------------

    return {

        "message":
        "Job Description uploaded successfully",

        "job_id":
        job.id,

        "title":
        job.title,

        "filename":
        file.filename,

        "text_length":
        len(text)

    }


# ==================================================
# Get All Jobs
# ==================================================

@router.get("/jobs")
def get_jobs(
    db: Session = Depends(get_db)
):

    jobs = db.query(
        JobDescription
    ).all()


    return {

        "total_jobs":
        len(jobs),

        "jobs": [

            {

                "job_id":
                job.id,

                "title":
                job.title,

                "filename":
                job.filename

            }

            for job in jobs

        ]

    }


# ==================================================
# Get Single Job
# ==================================================

@router.get("/jobs/{job_id}")
def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = db.query(
        JobDescription
    ).filter(
        JobDescription.id == job_id
    ).first()


    if not job:

        raise HTTPException(

            status_code=404,

            detail="Job not found"

        )


    return {

        "job_id":
        job.id,

        "title":
        job.title,

        "filename":
        job.filename

    }


# ==================================================
# Extract + Embed + Store JD
# ==================================================

@router.get("/extract-jd")
def extract_jd(
    job_id: int,
    db: Session = Depends(get_db)
):

    # ------------------------------------------
    # Get Job
    # ------------------------------------------

    job = db.query(
        JobDescription
    ).filter(
        JobDescription.id == job_id
    ).first()


    if not job:

        raise HTTPException(

            status_code=404,

            detail="Job not found"

        )


    # ------------------------------------------
    # File Path
    # ------------------------------------------

    file_path = os.path.join(

        UPLOAD_DIR,

        job.filename

    )


    if not os.path.exists(file_path):

        raise HTTPException(

            status_code=404,

            detail="Job Description PDF not found"

        )


    # ------------------------------------------
    # Read PDF
    # ------------------------------------------

    reader = PdfReader(
        file_path
    )

    text = ""


    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"


    # ------------------------------------------
    # Validate Text
    # ------------------------------------------

    if not text.strip():

        raise HTTPException(

            status_code=400,

            detail="Could not extract text from PDF"

        )


    # ------------------------------------------
    # Clean JD
    # ------------------------------------------

    cleaned_text = clean_jd_text(
        text
    )


    # ------------------------------------------
    # Create Embeddings
    # ------------------------------------------

    chunks, embeddings = create_jd_embeddings(

        cleaned_text

    )


    # ------------------------------------------
    # Store in ChromaDB
    # ------------------------------------------

    stored_chunks = store_jd_embeddings(

        chunks,

        embeddings,

        job_id=job.id

    )


    # ------------------------------------------
    # Return Result
    # ------------------------------------------

    return {

        "message":
        "JD processed and stored successfully",

        "job_id":
        job.id,

        "total_chunks":
        len(chunks),

        "stored_chunks":
        stored_chunks,

        "embedding_dimension":
        len(embeddings[0])

    }


# ==================================================
# Search Selected JD
# ==================================================

@router.get("/search-jd")
def search_jd(
    question: str,
    job_id: int
):

    results = retrieve_jd_chunks(

        question=question,

        job_id=job_id,

        top_k=2

    )


    return {

        "job_id":
        job_id,

        "question":
        question,

        "results":
        results

    }


# ==================================================
# Ask JD
# ==================================================

@router.get("/ask-jd")
def ask_jd(
    question: str
):

    answer = answer_jd_question(
        question
    )


    return {

        "question":
        question,

        "answer":
        answer

    }