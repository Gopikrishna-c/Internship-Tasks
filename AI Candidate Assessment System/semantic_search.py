import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Candidate resume
candidate_resume = """
Python developer with experience in FastAPI,
NumPy, Pandas, Scikit-learn and Machine Learning.
Developed an AI Recruitment System using Python
and FastAPI with candidate matching.
"""


# Job requirement
job_requirement = """
Looking for a Python Developer with experience
in FastAPI, Machine Learning, Scikit-learn,
NumPy and Pandas.
"""


# Convert resume and job requirement into embeddings
resume_embedding = model.encode(
    [candidate_resume]
).astype("float32")

job_embedding = model.encode(
    [job_requirement]
).astype("float32")


# Create FAISS index
dimension = resume_embedding.shape[1]

index = faiss.IndexFlatL2(dimension)

# Add candidate resume vector
index.add(resume_embedding)


# Search using job requirement
distances, indices = index.search(
    job_embedding,
    k=1
)


print("Candidate vector found at index:", indices[0][0])

print("Distance:", distances[0][0])