from sentence_transformers import SentenceTransformer

from services.jd_vector_service import collection


# ==================================================
# Load Embedding Model
# ==================================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ==================================================
# Retrieve JD Chunks
# ==================================================

def retrieve_jd_chunks(
    question: str,
    job_id: int,
    top_k: int = 2
):

    # ------------------------------------------
    # Convert Question into Embedding
    # ------------------------------------------

    question_embedding = embedding_model.encode(
        question
    ).tolist()


    # ------------------------------------------
    # Search Selected Job Only
    # ------------------------------------------

    results = collection.query(

        query_embeddings=[
            question_embedding
        ],

        n_results=top_k,

        where={
            "job_id": job_id
        }

    )


    # ------------------------------------------
    # Get Relevant Documents
    # ------------------------------------------

    documents = results.get(
        "documents",
        [[]]
    )[0]


    return documents