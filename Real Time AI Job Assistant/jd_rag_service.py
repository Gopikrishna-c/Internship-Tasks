import os

from dotenv import load_dotenv
from google import genai

from services.jd_retriever_service import retrieve_jd_chunks


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def answer_jd_question(question: str):

    # Retrieve relevant JD chunks
    relevant_chunks = retrieve_jd_chunks(
        question,
        top_k=2
    )

    # Combine retrieved chunks
    context = "\n\n".join(
        relevant_chunks
    )

    prompt = f"""
You are a Job Description Assistant.

Answer the user's question using ONLY the
Job Description context provided below.

If the answer is not available in the
Job Description, clearly say that the
information is not mentioned in the JD.

Do not invent or assume information.

Job Description Context:
{context}

User Question:
{question}

Give a clear and concise answer.
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text