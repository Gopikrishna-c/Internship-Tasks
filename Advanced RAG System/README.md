# 📄 Advanced RAG (Retrieval-Augmented Generation) System

## 📌 Overview

The Advanced RAG System is an AI-powered Question Answering application that retrieves relevant information from a PDF document and generates accurate answers using Google Gemini.

The system uses Retrieval-Augmented Generation (RAG), where the relevant document content is first retrieved from a vector database and then passed to the Gemini Large Language Model (LLM) to generate context-aware responses.

---

## 🚀 Features

- Load PDF documents
- Extract text from PDF
- Split text into chunks
- Generate embeddings using HuggingFace
- Store embeddings in ChromaDB
- Retrieve relevant document chunks
- Generate answers using Google Gemini
- Interactive command-line question answering

---

## 🛠️ Technologies Used

- Python
- LangChain
- PyPDFLoader
- RecursiveCharacterTextSplitter
- HuggingFace Embeddings
- ChromaDB
- Google Gemini API

---

## 📂 Project Structure

```
Advanced_RAG_System/
│
├── chunking/
├── data/
├── embeddings/
├── llm/
├── loaders/
├── retriever/
├── vectorstore/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Advanced_RAG_System.git
```

```bash
cd Advanced_RAG_System
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Project

```bash
python app.py
```

---

## 💬 Example Questions

- What are Gopikrishna's technical skills?
- What projects has Gopikrishna completed?
- What is Gopikrishna's work experience?
- Which programming languages does Gopikrishna know?

---

## 🔄 Workflow

1. Load PDF document
2. Extract text
3. Split text into chunks
4. Generate embeddings
5. Store embeddings in ChromaDB
6. Retrieve relevant chunks
7. Send context to Gemini
8. Generate final answer

---

## 📷 Sample Output

```
Ask a Question:
What are Gopikrishna's technical skills?

AI Answer:

• Python
• FastAPI
• NumPy
• Pandas
• Scikit-learn
• REST APIs
• CountVectorizer
• Cosine Similarity
• JSON
```

---

## 👨‍💻 Author

**Gopikrishna C**

GitHub: https://github.com/Gopikrishna-c

LinkedIn: https://www.linkedin.com/in/gopikrishna-c

---
