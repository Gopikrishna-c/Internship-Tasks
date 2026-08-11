import chromadb


# ==========================================
# ChromaDB Client
# ==========================================

client = chromadb.PersistentClient(
    path="./rag_chroma_db"
)


# ==========================================
# Collection
# ==========================================

collection = client.get_or_create_collection(
    name="general_rag"
)


# ==========================================
# Store Documents
# ==========================================

def store_documents(
    chunks: list[str],
    embeddings: list[list[float]]
):

    ids = [
        f"doc_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return {
        "message": "Documents stored successfully",
        "count": len(chunks)
    }