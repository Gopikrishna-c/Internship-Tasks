import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str):

    embedding = model.encode([text])

    return embedding.astype("float32")


def create_faiss_index(embedding):

    dimension = embedding.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embedding)

    return index


if __name__ == "__main__":

    resume_text = """
    Python developer with experience in FastAPI,
    NumPy, Pandas, Scikit-learn and Machine Learning.
    Developed an AI Recruitment System using Python
    and FastAPI with candidate matching.
    """

    embedding = create_embedding(resume_text)

    print("Embedding created successfully!")
    print("Embedding shape:", embedding.shape)

    index = create_faiss_index(embedding)

    print("FAISS index created successfully!")
    print("Number of vectors:", index.ntotal)