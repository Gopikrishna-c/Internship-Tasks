# Multi-Agent AI Recruitment Assessment System

An AI-powered recruitment platform that automates the complete hiring workflow using multiple intelligent AI agents. The system helps recruiters screen resumes, compare candidates with job descriptions, conduct technical coding assessments, analyze interview audio, generate unbiased evaluation scores, and automatically shortlist candidates for HR.

## Project Overview

Traditional recruitment involves multiple manual steps such as resume screening, skill verification, technical evaluation, interview assessment, and candidate ranking. This project combines these stages into a single FastAPI application powered by specialized AI agents.

The platform follows a modular architecture where each recruitment responsibility is implemented as an independent AI agent, making the system scalable, maintainable, and easy to extend.

## Key Features

### Resume Parsing Agent

* Upload Resume PDF
* Extracts Name, Email, Phone
* Parses Education, Experience, Skills & Projects
* Stores structured data in PostgreSQL

### Job Description Parser

* Upload JD PDF
* Extracts Job Title, Company Name
* Identifies Required Skills automatically

### Semantic Skill Matching Agent

* Compares Resume vs Job Description
* Uses Sentence Transformers for semantic similarity
* Returns Match Percentage, Matched Skills & Missing Skills

### Coding Assessment Agent

* Create coding questions dynamically
* Candidate submits Python code
* Executes code securely using **E2B Isolated Sandbox**
* Validates against multiple test cases
* Generates technical score

### Code Quality Agents

* Cyclomatic Complexity Analysis
* Edge Case Evaluation
* Runtime Test Validation

### Audio Interview Analysis

* Upload interview audio
* Converts speech to text using **Whisper**
* Measures communication quality
* Evaluates STAR (Situation, Task, Action, Result) responses

### Fair Scoring Agent

Combines multiple evaluation metrics into one unbiased score:

* Technical Score
* Skill Match Score
* Edge Case Score
* Code Complexity
* Communication Score

Personal identity is ignored to ensure merit-based evaluation.

### HR Shortlisting Agent

Automatically generates recruitment decisions:

| Overall Score | Decision    |
| ------------- | ----------- |
| **8.5 – 10**  | Shortlisted |
| **7 – 8.49**  | Review      |
| **Below 7**   | Rejected    |

## Tech Stack

| Technology            | Purpose                 |
| --------------------- | ----------------------- |
| Python 3.13           | Programming Language    |
| FastAPI               | REST API Framework      |
| Uvicorn               | ASGI Server             |
| PostgreSQL            | Database                |
| SQLAlchemy            | ORM                     |
| AsyncPG               | Async Database Driver   |
| PyMuPDF               | Resume & JD Parsing     |
| Sentence Transformers | Semantic Skill Matching |
| Whisper               | Speech-to-Text          |
| E2B                   | Secure Code Execution   |

## Project Structure

```text
Multi-Agent AI Recruitment Assessment System
│
├── app
│   ├── agents          # AI Agents
│   ├── models          # Database Models
│   ├── parser          # Resume & JD Parsing
│   ├── rag             # Embeddings
│   ├── routes          # FastAPI Endpoints
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── uploads
├── requirements.txt
└── README.md
```

## API Endpoints

| Module           | Endpoint                   |
| ---------------- | -------------------------- |
| Candidate        | `/candidates`              |
| Resume Upload    | `/resume/upload`           |
| JD Upload        | `/jd/upload`               |
| Skill Gap        | `/matching/skill-gap`      |
| Auto Match       | `/matching/auto-match`     |
| Coding Questions | `/coding/questions`        |
| Code Submission  | `/submission`              |
| Execute Code     | `/submission/{id}/execute` |
| Audio Analysis   | `/audio/upload`            |
| Fair Report      | `/assessment/fair-report`  |
| HR Shortlist     | `/hr/shortlist`            |

## System Workflow

1. Recruiter uploads Resume PDF.
2. Resume Parser extracts candidate information.
3. Recruiter uploads Job Description.
4. Semantic Matching Agent calculates skill compatibility.
5. Candidate completes coding assessment.
6. E2B Sandbox securely executes submitted code.
7. Complexity & Edge Case Agents evaluate code quality.
8. Candidate uploads interview audio.
9. Whisper converts speech into text.
10. Communication & STAR Agents analyze interview quality.
11. Fair Scoring Agent generates overall score.
12. HR Shortlisting Agent produces the final recruitment decision.

## Sample Fair Report

```json
{
  "candidate_id": 3,
  "technical_score": 10,
  "skill_match": 55.56,
  "edge_case_score": 10,
  "complexity": "Easy",
  "overall_score": 8.52,
  "status": "SHORTLISTED"
}
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd Multi-Agent-AI-Recruitment-Assessment-System
```

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/multi_agent_db
E2B_API_KEY=your_e2b_api_key
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Future Enhancements

* JWT Authentication
* Redis + Celery Background Tasks
* Docker Deployment
* Email Notification to HR
* AI Interview Question Generation
* Candidate Performance Dashboard

## Author

**Gopikrishna C**


