# AI Candidate Assessment System

## Overview

The **AI Candidate Assessment System** is an AI-powered recruitment application that automates resume parsing, technical assessment, answer evaluation, and candidate scoring. The system uses **FastAPI**, **PostgreSQL**, **Gemini AI**, and **FAISS** to provide an end-to-end candidate assessment workflow.

## Features

### Phase 1 – Resume Parsing

* Upload Resume PDF
* Extract Education, Skills, Experience, and Projects
* Convert resume into structured JSON
* Detect missing candidate information

### Phase 2 – Database & Vector Search

* Store candidate profiles in PostgreSQL
* Store parsed resume JSON
* Store assessments and evaluations
* Semantic search using FAISS embeddings

### Phase 3 – AI Technical Assessment

* Generate resume-based technical questions
* Skill validation using AI
* Project-based problem-solving questions
* Candidate context (RAG)

### Phase 4 – AI Evaluation

* 1–10 scoring system
* Feedback generation
* Logical explanation
* Semantic ranking

### Phase 5 – API Integration

* Resume Upload API
* Assessment Start API
* Answer Evaluation API
* Final Result API

## Tech Stack

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Backend                          |
| FastAPI      | REST APIs                        |
| PostgreSQL   | Database                         |
| Gemini AI    | Question generation & evaluation |
| PyMuPDF      | Resume parsing                   |
| FAISS        | Vector similarity search         |
| Scikit-learn | Candidate matching               |
| SQLAlchemy   | ORM                              |
| Pydantic     | Request validation               |

## Project Structure

```text
AI_Candidate_Assessment/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── resume_parser.py
│   ├── section_parser.py
│   ├── structured_parser.py
│   ├── missing_data.py
│   ├── rag_engine.py
│   ├── question_generator.py
│   ├── evaluator.py
│   ├── semantic_ranking.py
│   └── problem_solver.py
│
├── uploads/
├── requirements.txt
├── .env
└── README.md
```

## API Endpoints

| Method | Endpoint                            | Description               |
| ------ | ----------------------------------- | ------------------------- |
| GET    | `/`                                 | Health Check              |
| POST   | `/resume/upload`                    | Upload & Parse Resume     |
| POST   | `/assessment/start/{candidate_id}`  | Start Assessment          |
| POST   | `/assessment/answer/{candidate_id}` | Evaluate Candidate Answer |
| GET    | `/assessment/result/{candidate_id}` | Fetch Final Score         |

## Workflow

```text
Resume Upload
      ↓
Resume Parsing
      ↓
Education / Skills / Experience JSON
      ↓
Missing Data Detection
      ↓
PostgreSQL Storage
      ↓
AI Question Generation
      ↓
Candidate Answers
      ↓
Gemini AI Evaluation
      ↓
Score + Feedback
      ↓
Final Assessment Result
```

## Sample Assessment Result

| Question          | Score |
| ----------------- | ----: |
| FastAPI           |  6/10 |
| Scikit-learn      |  7/10 |
| CountVectorizer   |  9/10 |
| Cosine Similarity |  8/10 |

**Final Score: 7.5 / 10**

## Installation

```bash
git clone <repository-url>
cd AI_Candidate_Assessment

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

## Swagger Documentation

Open your browser:

```text
http://127.0.0.1:8000/docs
```

## Author

**Gopikrishna C**

Generative AI | FastAPI | PostgreSQL | Machine Learning
