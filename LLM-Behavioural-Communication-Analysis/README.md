# LLM-Based Behavioural & Communication Analysis System

### Vellei AI Interview Assessment Module

An AI-powered interview assessment system that analyzes interview transcripts and generates structured behavioural and communication insights using **FastAPI** and **Ollama (Llama 3.2)**.

> **Note:** This system analyzes interview transcripts only. It does not conduct interviews or make hiring decisions.

---

## Features

- Transcript Cleaning & Normalization
- Question–Answer Extraction
- Communication Analysis
- Behavioural Analysis with Evidence
- STAR Framework Analysis
- Filler Word Detection
- Communication Scoring
- Candidate Report Generation
- Recruiter Report Generation
- Hallucination Control

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API |
| Ollama (Llama 3.2) | LLM |
| PostgreSQL | Database |
| Pydantic | Data Validation |
| Uvicorn | API Server |

---

## Project Structure

```text
LLM-Behavioural-Communication-Analysis/
│
├── app/
│   ├── llm/
│   │   ├── client.py
│   │   └── prompts.py
│   │
│   ├── routes/
│   │   └── transcript.py
│   │
│   ├── schemas/
│   │   └── transcript.py
│   │
│   ├── services/
│   │   ├── behaviour.py
│   │   ├── communication.py
│   │   ├── filler.py
│   │   ├── normalizer.py
│   │   ├── qa_extractor.py
│   │   ├── report.py
│   │   ├── scoring.py
│   │   ├── star.py
│   │   ├── star_normalizer.py
│   │   └── transcript_processor.py
│   │
│   ├── database.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## System Workflow

```text
Interview Transcript
        │
        ▼
Transcript Processing
        │
        ▼
Question–Answer Extraction
        │
        ▼
Communication Analysis
        │
        ▼
Behaviour Analysis
        │
        ▼
STAR Analysis + Filler Detection
        │
        ▼
Scoring Engine
        │
        ▼
Candidate Report & Recruiter Report
```

---

## System Architecture

```text
                 User / Recruiter
                        │
                        ▼
              Transcript Upload
                        │
                        ▼
            Transcript Processor
                        │
                        ▼
          Question–Answer Extractor
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
Communication Analysis          Behaviour Analysis
        │                               │
        └───────────────┬───────────────┘
                        ▼
               Evidence Extraction
                        ▼
                Confidence Layer
                        ▼
                 Scoring Engine
                        ▼
                Report Generator
                ┌─────────────┐
                ▼             ▼
        Candidate Report  Recruiter Report
```

---

## Installation

### 1. Create Virtual Environment

```bash
py -m venv venv
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file:

```env
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/behaviour_analysis_db
OLLAMA_MODEL=llama3.2:3b
```

### 4. Start Ollama

```bash
ollama serve
```

### 5. Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/transcript/process` | Clean transcript |
| POST | `/transcript/extract-qa` | Extract Q&A pairs |
| POST | `/transcript/communication` | Communication analysis |
| POST | `/transcript/behaviour` | Behaviour analysis |
| POST | `/transcript/star` | STAR framework analysis |
| POST | `/transcript/fillers` | Filler word detection |
| POST | `/transcript/full-analysis` | Complete interview analysis |
| POST | `/transcript/candidate-report` | Generate candidate report |
| POST | `/transcript/recruiter-report` | Generate recruiter report |

---

## Sample Input

```json
{
  "transcript": "Interviewer: Tell me about yourself.\nCandidate: I am a Python developer.\nInterviewer: Describe a challenging project.\nCandidate: I optimized API performance by improving database queries."
}
```

---

## Core Modules

### Transcript Processor

- Clean and normalize interview transcripts
- Preserve speaker labels
- Handle formatting inconsistencies

### Q&A Extractor

- Map interviewer questions to candidate answers
- Generate Question IDs and Answer IDs

### Communication Analysis

Evaluates:

- Clarity
- Relevance
- Structure
- Conciseness
- Professional Communication

### Behaviour Analysis

Evidence-based evaluation of:

- Problem Solving
- Ownership
- Learning Attitude

Returns **Strong**, **Moderate**, or **Limited Evidence** with confidence.

### STAR Analysis

Detects:

- Situation
- Task
- Action
- Result

Returns missing STAR components when information is insufficient.

### Filler Detection

Detects common filler words:

- Um
- Uh
- Actually
- Basically
- Like
- You know
- I mean

### Scoring Engine

Calculates an overall communication score using a documented scoring methodology.

---

## Scoring Methodology

| Score Range | Level |
|-------------|-------|
| **9.0 – 10.0** | Excellent |
| **7.0 – 8.9** | Good |
| **5.0 – 6.9** | Average |
| **0.0 – 4.9** | Needs Improvement |

The overall communication score is calculated from the average of:

- Clarity
- Relevance
- Structure
- Conciseness
- Professional Communication

This ensures consistent scoring across all interview transcripts.

---

## Candidate Report

The candidate report provides:

- Strengths
- Improvement Areas
- Communication Feedback
- Learning Guidance

---

## Recruiter Report

The recruiter report provides:

- Executive Summary
- Average Communication Score
- Behavioural Evidence
- Confidence Levels
- Recommendation Support

> **AI-assisted evaluation only. Final hiring decisions must be made by authorized human recruiters.**

---

## Hallucination Control

- Uses only the supplied interview transcript
- Never invents candidate experiences
- Returns **Limited Evidence** when information is insufficient
- Every behavioural assessment includes confidence and supporting evidence

---

## Test Results

| Test Case | Status |
|-----------|--------|
| Strong Candidate | ✅ PASS |
| Average Candidate | ✅ PASS |
| Weak Candidate | ✅ PASS |
| Insufficient Evidence | ✅ PASS |
| Teamwork / Conflict | ✅ PASS |
| Consistency Test | ✅ PASS |

**Overall Result:** **6/6 Test Cases Passed**

---

## Future Enhancements

- PostgreSQL Persistence
- PDF Report Generation
- Multi-Agent Architecture
- Authentication & User Management
- Streamlit Dashboard
- Audio-to-Transcript Integration

---

## Author

**Gopikrishna C**
