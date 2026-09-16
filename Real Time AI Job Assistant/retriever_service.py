from services.rag.vector_service import collection
from services.rag.embedding_service import embedding_model


# ==========================================
# Retrieve Relevant Documents
# ==========================================

def retrieve_documents(
    question: str,
    top_k: int = 3
):

    # --------------------------------------
    # Convert question into embedding
    # --------------------------------------

    question_embedding = embedding_model.encode(
        question
    ).tolist()

    # --------------------------------------
    # Similarity Search in ChromaDB
    # --------------------------------------

    results = collection.query(
        query_embeddings=[
            question_embedding
        ],
        n_results=top_k
    )

    # --------------------------------------
    # Get retrieved documents
    # --------------------------------------

    documents = results.get(
        "documents",
        [[]]
    )[0]

    return documents