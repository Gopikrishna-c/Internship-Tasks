AI-Powered Candidate Intelligence

An AI-powered recruitment platform that transforms an unstructured resume into a structured candidate profile, recommends suitable job roles, conducts an adaptive AI interview, and generates a job readiness benchmark.

Features

* Candidate Registration & Login (JWT Authentication)
* Resume Upload (PDF)
* Resume Parsing using PyMuPDF
* Structured Candidate Profile Generation
* PostgreSQL Database Integration
* RAG Knowledge Layer using ChromaDB
* Profile Completeness Analysis
* AI Gap-Filling Questions (Gemini)
* Top 5 Job Role Recommendation
* Single Role Selection
* Adaptive AI Assessment (5 Dynamic Questions)
* AI Answer Evaluation
* Readiness Benchmark Generation

## Tech Stack

* **Backend:** FastAPI
* **Database:** PostgreSQL
* **AI Model:** Gemini 3.6 Flash
* **RAG:** ChromaDB
* **ORM:** SQLAlchemy
* **Authentication:** JWT
* **PDF Parsing:** PyMuPDF

## Project Structure

```text
AI-Powered-Candidate-Intelligence/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── security.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── profile.py
│   │   ├── selected_role.py
│   │   └── assessment.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── resume.py
│   │   ├── profile.py
│   │   ├── gap.py
│   │   ├── role.py
│   │   └── assessment.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── resume.py
│   │   ├── role.py
│   │   └── assessment.py
│   │
│   ├── services/
│   │   ├── parser.py
│   │   ├── rag.py
│   │   ├── gemini_service.py
│   │   └── benchmark.py
│   │
│   └── rag/
│       └── vector_db.py
│
├── uploads/
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

## Workflow

1. Candidate Registration/Login
2. Resume Upload
3. Resume Parsing
4. Store Profile in PostgreSQL
5. RAG Embedding Creation
6. Profile Completeness Check
7. AI Gap Filling
8. Role Recommendation
9. Candidate Selects One Role
10. Adaptive AI Interview
11. Final Readiness Benchmark

## API Endpoints

| Method | Endpoint                           | Description                              |
| ------ | ---------------------------------- | ---------------------------------------- |
| POST   | `/auth/register`                   | Register candidate                       |
| POST   | `/auth/login`                      | Login                                    |
| POST   | `/resume/upload`                   | Upload & parse resume                    |
| GET    | `/profile/{email}`                 | Get candidate profile                    |
| GET    | `/profile/{email}/completeness`    | Profile completeness                     |
| GET    | `/profile/{email}/recommendations` | Recommended roles                        |
| POST   | `/gap/question`                    | AI gap-filling question                  |
| POST   | `/role/select`                     | Select target role                       |
| GET    | `/role/{email}`                    | View selected role                       |
| POST   | `/assessment/start`                | Start adaptive interview                 |
| POST   | `/assessment/answer`               | Evaluate answer & generate next question |

## Adaptive Assessment

* Only **Question 1** is generated initially.
* Every next question is dynamically generated based on the previous answer and score.
* AI evaluates each response in real time.
* After 5 questions, the system calculates the average score and generates a readiness benchmark.

## Readiness Levels

| Average Score | Level              |
| ------------- | ------------------ |
| 9.0 – 10.0    | Strong Entry-Level |
| 7.0 – 8.9     | Entry-Level Ready  |
| 5.0 – 6.9     | Foundation         |
| Below 5.0     | Needs Improvement  |

## Installation

```bash
git clone <repository-url>
cd AI-Powered-Candidate-Intelligence

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file using `.env.example`, then run:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

**Developed by Gopikrishna C**
