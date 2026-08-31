# AI Mock Interview Platform

## Overview

The **AI Mock Interview Platform** is a text-based Generative AI application that simulates real technical interviews. It allows candidates to attend an AI-driven interview where technical questions are generated dynamically using **Ollama (Llama 3.2)**.

The platform evaluates each answer, asks adaptive follow-up questions based on the candidate's previous response, automatically completes the interview after **10 questions**, and generates a detailed AI diagnostic report.

---

## Key Features

* Create and manage technical job roles
* Register candidates for interviews
* Create interview sessions
* Generate AI-powered technical questions using Ollama
* Adaptive follow-up questions based on candidate answers
* AI feedback for every response
* Automatic interview completion after 10 questions
* Professional thank-you message at the end of the interview
* AI performance report with score, strengths, gaps, and recommendations

---

## Tech Stack

| **Technology**     | **Purpose**                         |
| ------------------ | ----------------------------------- |
| FastAPI            | REST API Backend                    |
| PostgreSQL         | Database                            |
| SQLAlchemy         | ORM                                 |
| Pydantic           | Request & Response Validation       |
| Ollama (Llama 3.2) | AI Question Generation & Evaluation |

---

## Project Structure

```text
AI Mock Interview Platform/
│
├── app/
│   ├── models/
│   │   ├── answer.py
│   │   ├── candidate.py
│   │   ├── interview.py
│   │   ├── job.py
│   │   └── question.py
│   │
│   ├── routers/
│   │   ├── candidate_router.py
│   │   ├── interview_router.py
│   │   └── job_router.py
│   │
│   ├── schemas/
│   │   ├── answer.py
│   │   ├── candidate.py
│   │   ├── interview.py
│   │   └── job.py
│   │
│   ├── services/
│   │   ├── ollama_service.py
│   │   └── report_service.py
│   │
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── venv/
├── .env
└── README.md
```

### Folder Description

| **Folder/File** | **Description**                       |
| --------------- | ------------------------------------- |
| `models/`       | SQLAlchemy database models            |
| `routers/`      | FastAPI API endpoints                 |
| `schemas/`      | Pydantic request and response models  |
| `services/`     | Ollama AI and report generation logic |
| `database.py`   | PostgreSQL database connection        |
| `main.py`       | FastAPI application entry point       |

---

## Workflow

1. Create a Job role
2. Register a Candidate
3. Create an Interview Session
4. Start the Interview
5. AI generates the first technical question
6. Candidate submits an answer
7. AI evaluates the answer and generates the next question
8. Interview continues for **10 adaptive questions**
9. AI displays a Thank You message
10. Generate the final AI diagnostic report

---

## API Endpoints

### Job APIs

| **Method** | **Endpoint** | **Description**  |
| ---------- | ------------ | ---------------- |
| POST       | `/jobs`      | Create a new job |
| GET        | `/jobs`      | View all jobs    |

### Candidate APIs

| **Method** | **Endpoint**  | **Description**      |
| ---------- | ------------- | -------------------- |
| POST       | `/candidates` | Register a candidate |

### Interview APIs

| **Method** | **Endpoint**                    | **Description**                       |
| ---------- | ------------------------------- | ------------------------------------- |
| POST       | `/mock-interviews`              | Create interview session              |
| POST       | `/mock-interviews/{id}/start`   | Start interview & generate Question 1 |
| POST       | `/mock-interviews/{id}/answers` | Submit answer & receive next question |
| GET        | `/mock-interviews/{id}/report`  | Generate final AI report              |

---

## Adaptive Interview Logic

Unlike a fixed questionnaire, the platform generates the **next interview question based on the candidate's previous answer**.

### Interview Flow

```text
Question 1
     ↓
Candidate Answer
     ↓
AI Evaluation
     ↓
Feedback
     ↓
Next Adaptive Question
```

This creates a personalized technical interview experience.

---

## Final AI Report

After completing **10 questions**, the system generates:

* Overall Score
* Strengths
* Knowledge Gaps
* Learning Recommendations

### Sample Report

```text
Overall Score : 85/100

Strengths
- FastAPI
- SQLAlchemy
- Redis Caching

Gaps
- Cache Invalidation
- Scalability

Recommendations
- Practice Redis Production Architecture
- Learn Advanced Concurrency
```

---

## Future Improvements

* JWT Authentication
* Redis Session Storage
* HTML/CSS Frontend
* Interview History Dashboard
* PDF Report Export

---

## Author

**Gopikrishna C**
