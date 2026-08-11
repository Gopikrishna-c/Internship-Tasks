import os

from dotenv import load_dotenv
from google import genai

from services.rag.document_loader import load_document
from services.rag.chunking_service import chunk_text
from services.rag.embedding_service import generate_embeddings
from services.rag.vector_service import store_documents
from services.rag.retriever_service import retrieve_documents


# ==========================================
# Environment
# ==========================================

load_dotenv()

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ==========================================
# Index Document
# ==========================================

def index_document(
    file_path: str
):

    # --------------------------------------
    # 1. Load Document
    # --------------------------------------

    text = load_document(
        file_path
    )

    if not text:
        raise ValueError(
            "Document is empty"
        )

    # --------------------------------------
    # 2. Chunk Text
    # --------------------------------------

    chunks = chunk_text(
        text
    )

    if not chunks:
        raise ValueError(
            "No chunks generated"
        )

    # --------------------------------------
    # 3. Generate Embeddings
    # --------------------------------------

    embeddings = generate_embeddings(
        chunks
    )

    # --------------------------------------
    # 4. Store in ChromaDB
    # --------------------------------------

    result = store_documents(
        chunks,
        embeddings
    )

    return {
        "file": os.path.basename(
            file_path
        ),
        "total_characters": len(text),
        "total_chunks": len(chunks),
        "message": result["message"]
    }


# ==========================================
# RAG Question Answering
# ==========================================

def answer_question(
    question: str,
    top_k: int = 3
):

    # --------------------------------------
    # 1. Retrieve Relevant Chunks
    # --------------------------------------

    documents = retrieve_documents(
        question,
        top_k=top_k
    )

    if not documents:

        return (
            "I could not find relevant "
            "information in the uploaded documents."
        )

    # --------------------------------------
    # 2. Build Context
    # --------------------------------------

    context = "\n\n".join(
        documents
    )

    # --------------------------------------
    # 3. Build Prompt
    # --------------------------------------

    prompt = f"""
You are a document-based AI assistant.

Answer the user's question using ONLY
the retrieved document context below.

Do not invent information.

If the answer is not available in the
context, clearly say that the information
is not mentioned in the document.

Retrieved Context:

{context}

User Question:

{question}

Give a clear and concise answer.
"""

    # --------------------------------------
    # 4. Generate Gemini Response
    # --------------------------------------

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text