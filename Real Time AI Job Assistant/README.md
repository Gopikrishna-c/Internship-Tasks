# 🤖 Real-Time AI Job Assistant

## 📌 Project Description

Real-Time AI Job Assistant is an AI-powered recruitment and career assistance system built using **Python** and **FastAPI**.

The system allows companies to upload Job Descriptions, processes and stores JD information using embeddings and a vector database, and allows candidates to interact with an AI assistant through text or voice.

The AI assistant combines:

- Conversation Memory
- Long-Term User Memory
- Interview Progress
- Resume / Document RAG
- Job Description Context
- Vector Search
- AI Response Generation
- Speech-to-Text
- Text-to-Speech

to provide personalized and job-specific responses.

---

# 🚀 Project Workflow

```text
Company
   ↓
Upload Job Description
   ↓
Extract PDF Text
   ↓
Clean & Preprocess JD
   ↓
Create Chunks
   ↓
Generate Embeddings
   ↓
Store in ChromaDB
   ↓
Candidate Login
   ↓
Candidate Selects Job
   ↓
Text / Voice Conversation
   ↓
AI Orchestrator
   ├── Conversation Memory
   ├── User Memory
   ├── Interview Progress
   ├── Resume / Document RAG
   └── Selected Job Description Context
   ↓
AI Response
   ├── Text Response
   └── Voice Response
   ↓
Save Conversation
```

---

# ✨ Features

## 🔐 Authentication

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- Protected User Profile
- Current User Retrieval

## 📄 Resume Management

- Resume Upload
- PDF / DOCX Processing
- Resume Text Extraction
- Resume Analysis
- Resume History
- Resume-based RAG Retrieval

## 💼 Job Description Management

- Job Description PDF Upload
- PDF Text Extraction
- JD Cleaning and Preprocessing
- Text Chunking
- Embedding Generation
- ChromaDB Vector Storage
- Job ID Creation
- Job Listing
- Job Details Retrieval
- JD Vector Search
- JD-based Question Answering

## 🧠 Memory System

The project maintains multiple types of context:

### Conversation Memory

Stores previous user and assistant messages.

### Long-Term User Memory

Stores useful user preferences and information.

Example:

```text
Preferred Language → Python
Preferred Technology → FastAPI
Job Role → AI Engineer
```

### Interview Progress

Tracks the candidate's learning and interview preparation progress.

Example:

```text
Python Basics → Completed
Python OOP → Completed
```

---

# 🧠 RAG System

The project uses Retrieval-Augmented Generation to retrieve relevant information before generating an AI response.

## General RAG Workflow

```text
Document
   ↓
Text Extraction
   ↓
Text Cleaning
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Answer
```

## 💼 Job-Specific RAG

Each Job Description is associated with a unique `job_id`.

Example:

```text
job_id = 1
```

The candidate selects a job and the selected job ID is used to retrieve relevant Job Description context.

```text
Candidate
   ↓
Select Job
   ↓
job_id = 1
   ↓
Ask Question
   ↓
JD Vector Search
   ↓
Relevant JD Chunks
   ↓
AI Orchestrator
   ↓
AI Response
```

---

# 🧠 AI Orchestrator

The AI Orchestrator coordinates different information sources before generating the final response.

It can retrieve:

1. Conversation Memory
2. Long-Term User Memory
3. Interview Progress
4. Resume / Document RAG Context
5. Job Description Context

The retrieved information is combined and passed to the AI model.

Example:

```text
User Message
      ↓
Conversation History
      ↓
User Memory
      ↓
Interview Progress
      ↓
Resume / RAG Context
      ↓
Job Description Context
      ↓
AI Orchestrator
      ↓
Gemini / LLM
      ↓
Final Response
```

---

# 💬 Text Chat

Candidates can interact with the AI assistant through text.

### Endpoint

```text
POST /api/chat
```

Example request:

```json
{
    "message": "What skills are required for this job?",
    "job_id": 1
}
```

The system retrieves relevant context and generates an intelligent response.

---

# 🎙️ Voice Assistant

The project supports voice-based interaction.

## Voice Workflow

```text
Audio Input
    ↓
Speech-to-Text
    ↓
User Message
    ↓
AI Orchestrator
    ↓
AI Response
    ↓
Text-to-Speech
    ↓
Audio Response
```

### Endpoint

```text
POST /voice/voice-chat
```

---

# 🗄️ Database

The project uses **SQLite** with **SQLAlchemy**.

The database stores application data such as:

- Users
- Job Descriptions
- User Memory
- Resume Analysis
- Interview Progress
- Conversation-related data

### Database

```text
job_assistant.db
```

---

# 🔎 Vector Database

The project uses **ChromaDB** to store and retrieve document embeddings.

### Vector Database

```text
ChromaDB
```

### Embedding Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Embedding Dimension

```text
384
```

### JD Vector Search Flow

```text
Job Description
      ↓
Clean Text
      ↓
Create Chunks
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
      ↓
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Relevant JD Chunks
```

---

# 📁 Project Structure

```text
Real_Time_AI_Job_Assistant/
│
├── main.py
│
├── models/
│   ├── database.py
│   ├── user.py
│   ├── job_description.py
│   ├── user_memory.py
│   └── resume_analysis.py
│
├── routes/
│   ├── auth.py
│   ├── chat.py
│   ├── resume.py
│   ├── jd.py
│   ├── voice_router.py
│   └── rag_router.py
│
├── services/
│   ├── ai_orchestrator.py
│   ├── chat_service.py
│   ├── chat_memory.py
│   ├── user_memory_service.py
│   ├── interview_progress_service.py
│   │
│   ├── stt_service.py
│   ├── tts_service.py
│   │
│   ├── jd_service.py
│   ├── jd_embedding_service.py
│   ├── jd_vector_service.py
│   ├── jd_retriever_service.py
│   ├── jd_rag_service.py
│   │
│   └──rag/
       ├── chunking_service.py
       ├── document_loader.py
       ├── embedding_service.py
       ├── rag_service.py
       ├── retriever.py
       └── vector_service.py    
│
├── uploads/
├── chroma_db/
├── job_assistant.db
├── requirements.txt
└── README.md
```

---

# 🌐 API Endpoints

The current Swagger API groups include:

## 🔐 Authentication

```text
GET  /auth/
POST /auth/register
POST /auth/login
GET  /auth/profile
```

Authentication provides:

- User registration
- User login
- JWT-based authentication
- Protected profile access

---

## 💬 Chat

```text
POST /api/chat
```

The Chat API connects the candidate's message with:

- Conversation Memory
- Long-Term User Memory
- Interview Progress
- Resume / Document RAG
- Job Description Context
- AI Response Generation

---

## 📄 Resume

```text
POST /resume/upload-resume
GET  /resume/extract-resume
GET  /resume/analyze-resume
GET  /resume/resume-history
```

These APIs handle:

- Resume upload
- Text extraction
- Resume analysis
- Resume history

---

## 💼 Job Description

```text
POST /jd/upload-jd
GET  /jd/jobs
GET  /jd/jobs/{job_id}
GET  /jd/extract-jd
GET  /jd/search-jd
GET  /jd/ask-jd
```

The Job Description APIs provide:

- JD upload
- Job ID creation
- Job listing
- Job details retrieval
- JD text extraction
- JD vector search
- JD-based question answering

### Job-Specific RAG Flow

```text
Candidate Selects Job
        ↓
     job_id
        ↓
JD Vector Search
        ↓
Relevant JD Context
        ↓
AI Orchestrator
        ↓
AI Response
```

---

## 🎙️ Voice Assistant

```text
POST /voice/voice-chat
```

The Voice Assistant supports:

```text
Audio Input
     ↓
Speech-to-Text
     ↓
AI Orchestrator
     ↓
AI Response
     ↓
Text-to-Speech
     ↓
Audio Response
```

---

# 🧪 Example Job Description

### Position

```text
AI/ML Engineer
```

### Company

```text
ABC AI Technologies
```

### Location

```text
Chennai, Tamil Nadu
```

### Experience

```text
0–2 years
```

### Required Skills

```text
Python
Machine Learning
NumPy
Pandas
Scikit-learn
SQL
REST APIs
Git
GitHub
FastAPI
```

### Preferred Qualifications

```text
Bachelor's degree in Computer Science or a related field
Generative AI / Large Language Models knowledge
Good problem-solving skills
Good communication skills
```

---

# 🧪 Job-Specific Chat Test

Candidate selects:

```text
job_id = 1
```

Then asks:

```text
What skills are required for this job?
```

Example response metadata:

```json
{
    "user_id": 1,
    "job_id": 1,
    "user_message": "What skills are required for this job?",
    "jd_search_used": true
}
```

This confirms that the selected Job Description context is being used.

---

# 🛠️ Technologies Used

## Backend

- Python
- FastAPI
- Uvicorn

## Database

- SQLite
- SQLAlchemy

## AI / LLM

- Google Gemini
- Generative AI

## RAG & Vector Search

- ChromaDB
- Sentence Transformers
- Embeddings
- Vector Search

## Machine Learning

- NumPy
- Pandas
- Scikit-learn

## Document Processing

- PyPDF
- DOCX Processing

## Authentication

- JWT
- bcrypt

## Voice

- Speech-to-Text
- Text-to-Speech

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

On Windows PowerShell:

```powershell
venv\Scriptsctivate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key
```

Do not commit the `.env` file to GitHub.

---

# 22. Running the Project

## 1. Activate the Virtual Environment

```powershell
venv\Scriptsctivate
```

## 2. Start the FastAPI Server

```powershell
uvicorn main:app --reload
```

If the server starts successfully, you should see:

```text
Application startup complete.
```

## 3. Open the Application

```text
http://127.0.0.1:8000
```

## 4. Open Swagger API Documentation

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test all available API endpoints interactively.

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Example API Testing Flow

## Step 1 — Register

```text
POST /auth/register
```

## Step 2 — Login

```text
POST /auth/login
```

## Step 3 — Upload Resume

```text
POST /resume/upload-resume
```

## Step 4 — Upload Job Description

```text
POST /jd/upload-jd
```

## Step 5 — View Available Jobs

```text
GET /jd/jobs
```

## Step 6 — Select a Job

Example:

```text
job_id = 1
```

## Step 7 — Search Job Description

```text
GET /jd/search-jd
```

Example question:

```text
What skills are required for this job?
```

## Step 8 — Start AI Chat

```text
POST /api/chat
```

The AI uses the available memory and relevant job context to generate the response.

## Step 9 — Voice Conversation

```text
POST /voice/voice-chat
```

---

# ✅ Project Status

The core Real-Time AI Job Assistant workflow has been implemented successfully.

### Completed Features

- User Registration
- User Login
- JWT Authentication
- Protected User Profile
- Resume Upload
- Resume Text Extraction
- Resume Analysis
- Resume History
- Conversation Memory
- Long-Term User Memory
- Interview Progress Tracking
- Job Description Upload
- Job ID Creation
- Job Listing
- Job Details Retrieval
- JD Text Extraction
- JD Cleaning and Preprocessing
- JD Chunking
- JD Embedding Generation
- ChromaDB Vector Storage
- JD Vector Search
- Job-Specific JD Retrieval
- AI Orchestration
- Context-Aware AI Responses
- Text Chat
- Voice Chat
- Speech-to-Text
- Text-to-Speech
- Conversation Saving
- Swagger API Testing

---

# 🎯 Project Objective

The main objective of this project is to build an intelligent AI Job Assistant that can understand:

- Candidate information
- Resume content
- Previous conversations
- User preferences
- Interview preparation progress
- Selected Job Description

The system combines **Memory, RAG, Vector Search, and Generative AI** to provide personalized and job-specific assistance.

---

# 👨‍💻 Developer

**Gopikrishna**

AI / Generative AI Engineer

### Core Technologies

```text
Python
FastAPI
Machine Learning
Generative AI
RAG
ChromaDB
SQLAlchemy
Git & GitHub
```
