from sentence_transformers import SentenceTransformer


# ==========================================
# Load Embedding Model
# ==========================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ==========================================
# Generate Embeddings
# ==========================================

def generate_embeddings(chunks: list[str]):

    embeddings = embedding_model.encode(
        chunks
    )

    return embeddings.tolist()