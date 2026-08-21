import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_score(candidate_resume, job_requirement):

    resume_embedding = model.encode(
        [candidate_resume]
    ).astype("float32")

    job_embedding = model.encode(
        [job_requirement]
    ).astype("float32")

    dimension = resume_embedding.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(resume_embedding)

    distances, indices = index.search(
        job_embedding,
        k=1
    )

    distance = float(distances[0][0])

    # Convert L2 distance into a simple similarity score
    semantic_score = 100 / (1 + distance)

    return round(semantic_score, 2), distance


def calculate_final_ranking(
    semantic_score,
    assessment_score
):

    final_score = (
        semantic_score * 0.5
        + (assessment_score * 10) * 0.5
    )

    return round(final_score, 2)


if __name__ == "__main__":

    candidate_resume = """
    Python developer with experience in FastAPI,
    NumPy, Pandas, Scikit-learn and Machine Learning.
    Developed an AI Recruitment System using Python
    and FastAPI with candidate matching.
    """

    job_requirement = """
    Looking for a Python Developer with experience
    in FastAPI, Machine Learning, Scikit-learn,
    NumPy and Pandas.
    """

    # Our Phase 4 assessment score
    assessment_score = 3.0

    semantic_score, distance = calculate_semantic_score(
        candidate_resume,
        job_requirement
    )

    final_score = calculate_final_ranking(
        semantic_score,
        assessment_score
    )

    print("Semantic Distance:", distance)
    print("Semantic Score:", semantic_score)
    print("Assessment Score:", assessment_score)
    print("Final Ranking Score:", final_score)