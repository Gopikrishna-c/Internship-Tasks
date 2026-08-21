# AI Candidate Assessment System

## Overview

The **AI Candidate Assessment System** is an AI-powered recruitment application that automates resume parsing, candidate profile creation, technical assessment, answer evaluation, and candidate scoring.

The system uses **FastAPI, PostgreSQL, Gemini AI, FAISS, Sentence Transformers, PyMuPDF, Scikit-learn, SQLAlchemy, and Pydantic** to provide an end-to-end candidate assessment workflow.

---

## Project Objectives

The main objectives of this project are:

- Parse candidate resumes automatically.
- Extract education, skills, experience, and project information.
- Convert resume information into structured JSON.
- Detect missing candidate information.
- Store candidate and assessment information in PostgreSQL.
- Generate vector embeddings for semantic matching.
- Store and search vectors using FAISS.
- Generate candidate-specific technical questions.
- Validate skills and project knowledge.
- Use contextual candidate information during assessment.
- Evaluate candidate answers using Gemini AI.
- Generate 1–10 scores, feedback, and logical explanations.
- Calculate final assessment scores.
- Support semantic candidate ranking.

---

# System Architecture

```text
                    Candidate Resume
                           │
                           ▼
                  Resume Upload API
                           │
                           ▼
                    PDF Resume Parser
                        (PyMuPDF)
                           │
                           ▼
             Structured Candidate Information
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Education         Skills          Experience
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                 Missing Data Detection
                           │
                           ▼
                    PostgreSQL DB
                           │
                           ▼
                  Candidate Profile
                           │
                           ▼
                 Sentence Transformer
                     Embeddings
                           │
                           ▼
                    FAISS Vector Store
                           │
                           ▼
                 Semantic Search/Ranking
                           │
                           ▼
                 Assessment Initialization
                           │
                           ▼
              Dynamic Question Generation
                           │
                           ▼
                    Candidate Answers
                           │
                           ▼
                    Gemini AI Evaluator
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
        Score           Feedback      Logical Explanation
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                  Evaluation Database
                           │
                           ▼
                 Final Assessment Result
                           │
                           ▼
                   Candidate Ranking
```

---

# Phase 1 – Resume Parsing

## 1. Resume Upload

The candidate uploads a resume in PDF format through the FastAPI resume upload endpoint.

### Endpoint

```text
POST /resume/upload
```

## 2. PDF Parsing

The system uses **PyMuPDF** to extract text from the uploaded PDF.

The extracted text is processed to identify relevant resume sections such as education, skills, experience, and projects.

## 3. Resume Information Extraction

The system extracts:

- Education
- Work Experience
- Technical Skills
- Projects
- Relevant resume sections

The extracted information is converted into structured JSON.

### Example Education JSON

```json
{
  "degree": "Bachelor of Science (B.Sc.) in Computer Science",
  "college": "Rajapalayam Rajus' College",
  "university": "Madurai Kamaraj University",
  "graduation": "Graduated: May 2025"
}
```

### Example Skills JSON

```json
{
  "programming_languages": [
    "Python",
    "SQL (Basics)"
  ],
  "frameworks": [
    "FastAPI"
  ],
  "libraries": [
    "NumPy",
    "Pandas",
    "Matplotlib",
    "Scikit-learn"
  ],
  "tools": [
    "Git",
    "GitHub",
    "Jupyter Notebook",
    "Visual Studio Code"
  ],
  "core_concepts": [
    "Object-Oriented Programming (OOP)",
    "File Handling",
    "REST APIs",
    "Machine Learning"
  ]
}
```

### Example Experience JSON

```json
{
  "job_title": "Documentation Executive",
  "company": "PrimaSoft Technologies Pvt. Ltd.",
  "location_duration": "Chennai June 2025 – Present",
  "responsibilities": [
    "Performed KYC verification and document validation to ensure regulatory compliance.",
    "Managed merchant onboarding by verifying customer documents and information.",
    "Maintained accurate customer records through data validation and verification.",
    "Processed customer applications within defined Turnaround Time (TAT) while maintaining quality standards.",
    "Coordinated with internal teams to resolve documentation discrepancies efficiently."
  ]
}
```

## 4. Missing Data Detection

The system checks whether important information such as education or skills is missing.

Example:

```json
{
  "missing_data": []
}
```

If information is missing, the system identifies it so that the assessment workflow can request additional information from the candidate.

## 5. Database Storage

After successful parsing, the candidate profile and parsed resume information are stored in PostgreSQL.

Example response:

```json
{
  "message": "Resume uploaded and saved successfully",
  "candidate_id": 1,
  "filename": "resumee.pdf",
  "database_status": "Saved successfully"
}
```

---

# Phase 2 – Database and Vector Search

## PostgreSQL

PostgreSQL is used as the primary relational database.

The system stores:

- Candidate information
- Profile information
- Parsed resume JSON
- Assessment information
- Questions
- Candidate answers
- Evaluation scores
- Feedback
- Logical explanations

## Vector Embeddings

The project uses **Sentence Transformers** to create vector embeddings.

The embedding model used in the vector store is:

```text
all-MiniLM-L6-v2
```

Example flow:

```text
Candidate / Resume Text
          ↓
Sentence Transformer
          ↓
Vector Embedding
          ↓
FAISS Index
```

## FAISS Vector Store

FAISS is used for vector similarity search.

The vector store creates an embedding and adds it to a FAISS index:

```text
Text
 ↓
Embedding
 ↓
FAISS Index
 ↓
Similarity Search
```

This supports semantic comparison between candidate information and job-related requirements.

## Semantic Search and Ranking

The project contains separate components for:

- Semantic search
- Semantic ranking
- Candidate ranking

These components can be used to identify and rank candidates based on relevance.

---

# Phase 3 – Dynamic AI Technical Assessment

## 1. Assessment Initiation

After the candidate profile is created, the assessment is initiated.

### Endpoint

```text
POST /assessment/start/{candidate_id}
```

Example:

```text
candidate_id = 1
```

Example successful response:

```json
{
  "message": "Assessment started successfully",
  "candidate_id": 1,
  "assessment_id": 4,
  "total_questions": 4,
  "questions": [
    "How did you use FastAPI in your AI Recruitment System?",
    "How did you use Scikit-learn for candidate matching?",
    "Why did you use CountVectorizer in your project?",
    "How does Cosine Similarity help in your candidate recommendation system?"
  ]
}
```

## 2. Dynamic Question Generation

The project includes dynamic question generation components that generate technical questions based on candidate context and project information.

## 3. Gap Filling

The gap-filling component identifies missing candidate information and can generate questions to collect additional information.

## 4. Skill Validation

The system validates whether the candidate understands skills mentioned in the resume.

Example:

```text
Resume Skill:
FastAPI

Question:
How did you use FastAPI in your AI Recruitment System?
```

## 5. Project-Based Validation

The system can generate questions based on projects mentioned by the candidate.

Example:

```text
Project:
AI Recruitment System

Question:
How does Cosine Similarity help in your candidate recommendation system?
```

## 6. Problem-Solving Validation

The project contains a problem-solving component that can be used to validate practical understanding through project-related scenarios.

## 7. Interview Flow and Context

The project includes interview flow and chat-memory components for maintaining candidate context during the assessment.

```text
Candidate Context
      ↓
Interview Flow
      ↓
Question
      ↓
Candidate Answer
      ↓
Context / Chat Memory
      ↓
Next Question
```

---

# Phase 4 – AI Evaluation and Scoring

## 1. Candidate Answer Submission

### Endpoint

```text
POST /assessment/answer/{candidate_id}
```

Example question:

```text
How does Cosine Similarity help in your candidate recommendation system?
```

Example answer:

```text
Cosine Similarity compares the candidate skills vector with the job requirement vector. It gives a similarity score, which helps the system recommend suitable candidates.
```

## 2. Gemini AI Evaluation

The candidate's answer is sent to the AI evaluation component.

The evaluator generates:

- Score
- Feedback
- Logical explanation

## 3. 1–10 Scoring

The project uses a 1–10 scoring system to evaluate candidate answers.

Example:

```text
Score: 6/10
```

## 4. Feedback

Example:

```text
The answer is conceptually correct but lacks technical depth and elaboration.
```

## 5. Logical Explanation

Example:

```text
The candidate correctly states that Cosine Similarity compares
candidate skill vectors with job requirement vectors to produce
a similarity score. However, the response is very brief and does
not explain how the vectors are created or why Cosine Similarity
is preferred.
```

## 6. Successful Evaluation Example

```json
{
  "message": "Answer evaluated and saved successfully",
  "candidate_id": 1,
  "assessment_id": 4,
  "evaluation_id": 7,
  "question": "How does Cosine Similarity help in your candidate recommendation system?",
  "answer": "Cosine Similarity compares the candidate skills vector with the job requirement vector. It gives a similarity score, which helps the system recommend suitable candidates.",
  "score": 6,
  "feedback": "The answer is conceptually correct but lacks technical depth and elaboration.",
  "logical_explanation": "The candidate correctly states that Cosine Similarity compares candidate skill vectors with job requirement vectors to produce a similarity score. However, the response is very brief. It fails to explain key technical aspects such as how the vectors are created, why Cosine Similarity is preferred, and how the output is utilized to rank candidates."
}
```

---

# Phase 5 – API Integration and Testing

The complete workflow was tested using FastAPI Swagger documentation.

## Swagger

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Health Check |
| POST | `/resume/upload` | Upload and Parse Resume |
| POST | `/assessment/start/{candidate_id}` | Start Candidate Assessment |
| POST | `/assessment/answer/{candidate_id}` | Evaluate Candidate Answer |
| GET | `/assessment/result/{candidate_id}` | Fetch Final Assessment Result |

---

# End-to-End Testing Workflow

```text
1. Health Check
       ↓
2. Resume Upload
       ↓
3. Resume Parsing
       ↓
4. Candidate Profile Creation
       ↓
5. Missing Data Detection
       ↓
6. PostgreSQL Storage
       ↓
7. Assessment Initiation
       ↓
8. Dynamic Question Generation
       ↓
9. Candidate Answer Submission
       ↓
10. Gemini AI Evaluation
       ↓
11. Score + Feedback + Logical Explanation
       ↓
12. Evaluation Database Save
       ↓
13. Final Assessment Result
       ↓
14. Candidate Ranking
```

---

# Final Assessment Result

### Endpoint

```text
GET /assessment/result/{candidate_id}
```

Example:

```text
candidate_id = 1
```

The API returns:

- Candidate ID
- Candidate Name
- Assessment ID
- Total Questions
- Final Score
- Individual Evaluations
- Candidate Answers
- Evaluation Scores
- Logical Explanations

Example:

```json
{
  "message": "Assessment result fetched successfully",
  "candidate_id": 1,
  "candidate_name": "GOPIKRISHNA C",
  "assessment_id": 4,
  "total_questions": 4,
  "final_score": 7.5,
  "evaluations": []
}
```

The actual final score depends on the answers evaluated in the assessment.

---

# Candidate Ranking

The project includes semantic ranking and candidate ranking components.

The conceptual flow is:

```text
Candidate Resume
       ↓
Candidate Skills
       ↓
Vector Embedding
       ↓
Semantic Search
       ↓
Job Requirement Match
       ↓
Assessment Score
       ↓
Candidate Ranking
```

This allows candidate relevance and assessment performance to be considered during recruitment evaluation.

---

# Actual Project Structure

The following structure reflects the current project shown in the VS Code workspace:

```text
AI Candidate Assessment System/
│
├── app/
│   ├── __pycache__/
│   │
│   ├── assessment.py
│   ├── candidate_ranking.py
│   ├── chat_memory.py
│   ├── database.py
│   ├── dynamic_question.py
│   ├── evaluator.py
│   ├── gap_filling.py
│   ├── interview_engine.py
│   ├── interview_flow.py
│   ├── main.py
│   ├── missing_data.py
│   ├── models.py
│   ├── problem_solver.py
│   ├── question_generator.py
│   ├── rag_engine.py
│   ├── resume_parser.py
│   ├── score_calculator.py
│   ├── section_parser.py
│   ├── semantic_ranking.py
│   ├── semantic_search.py
│   ├── structured_parser.py
│   └── vector_store.py
│
├── uploads/
│   └── resumee.pdf
│
├── venv/
│
├── .env
├── create_tables.py
├── test_db.py
├── requirements.txt
└── README.md
```

> **Note:** `venv/`, `__pycache__/`, uploaded PDFs, and `.env` are local/runtime files. They normally should not be committed to GitHub.

---

# Important Project Modules

| File | Purpose |
|---|---|
| `main.py` | FastAPI application and API routes |
| `database.py` | PostgreSQL database connection |
| `models.py` | Database models |
| `resume_parser.py` | Resume PDF text extraction |
| `section_parser.py` | Resume section extraction |
| `structured_parser.py` | Structured resume information |
| `missing_data.py` | Missing information detection |
| `rag_engine.py` | Candidate-context/RAG processing |
| `question_generator.py` | Technical question generation |
| `dynamic_question.py` | Dynamic assessment questions |
| `evaluator.py` | AI answer evaluation |
| `score_calculator.py` | Score calculation |
| `semantic_search.py` | Semantic search |
| `semantic_ranking.py` | Semantic candidate ranking |
| `candidate_ranking.py` | Candidate ranking |
| `vector_store.py` | Sentence Transformer embeddings and FAISS |
| `chat_memory.py` | Assessment conversation context |
| `gap_filling.py` | Missing-information question handling |
| `problem_solver.py` | Problem-solving assessment |
| `interview_engine.py` | Interview processing |
| `interview_flow.py` | Assessment/interview flow |
| `assessment.py` | Assessment-related logic |

---

# Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend application development |
| FastAPI | REST API development |
| PostgreSQL | Relational database |
| SQLAlchemy | Database ORM |
| Pydantic | Request/response validation |
| Gemini AI | Question generation and answer evaluation |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Vector embedding generation |
| FAISS | Vector similarity search |
| Scikit-learn | Text vectorization and similarity |
| JSON | Structured candidate data |
| Swagger | API testing and documentation |

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
```

## 2. Navigate to Project

Use the actual project folder name:

```bash
cd "AI Candidate Assessment System"
```

> If your actual folder name is different, use that exact folder name.

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 6. Configure Environment Variables

Create a `.env` file and configure the required database and Gemini API settings.

Example:

```env
DATABASE_URL=<your_postgresql_connection_string>
GEMINI_API_KEY=<your_gemini_api_key>
```

Do not commit actual API keys or passwords to GitHub.

## 7. Start FastAPI

```bash
uvicorn app.main:app --reload
```

## 8. Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

# Swagger Testing Sequence

For the project demonstration, use the following sequence.

## Step 1 – Health Check

```text
GET /
```

Verify that the API server is running.

## Step 2 – Resume Upload

```text
POST /resume/upload
```

Upload the candidate PDF.

Verify:

```text
Education
Skills
Experience
Projects
Missing Data
Database Status
```

## Step 3 – Start Assessment

```text
POST /assessment/start/1
```

Verify:

```text
Assessment ID
Total Questions
Generated Questions
```

## Step 4 – Submit Candidate Answer

```text
POST /assessment/answer/1
```

Submit the answer to one of the generated questions.

Verify:

```text
Evaluation ID
Score
Feedback
Logical Explanation
```

## Step 5 – Repeat Evaluation

Submit the remaining candidate answers as required by the assessment.

## Step 6 – Fetch Final Result

```text
GET /assessment/result/1
```

Verify:

```text
Candidate Name
Assessment ID
Total Questions
Final Score
Individual Evaluations
```

---

---

# Conclusion

The **AI Candidate Assessment System** provides an end-to-end AI-assisted recruitment assessment workflow.

```text
Resume Parsing
      +
Candidate Profile
      +
PostgreSQL
      +
Vector Embeddings
      +
FAISS Semantic Search
      +
Dynamic Technical Assessment
      +
Gemini AI Evaluation
      +
Scoring and Feedback
      +
Candidate Ranking
```

The project demonstrates how **Generative AI, vector databases, semantic search, relational databases, resume parsing, and REST APIs** can be combined to build an automated candidate assessment and recruitment platform.

---

# Author

**Gopikrishna C**

