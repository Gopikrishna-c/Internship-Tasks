import chromadb


# ==================================================
# Create ChromaDB Client
# ==================================================

client = chromadb.PersistentClient(
    path="chroma_db"
)


# ==================================================
# Create / Get JD Collection
# ==================================================

collection = client.get_or_create_collection(
    name="job_descriptions"
)


# ==================================================
# Store JD Embeddings
# ==================================================

def store_jd_embeddings(
    chunks,
    embeddings,
    job_id: int
):

    ids = []

    metadatas = []


    # ------------------------------------------
    # Create IDs and Metadata
    # ------------------------------------------

    for index in range(len(chunks)):

        ids.append(
            f"job_{job_id}_jd_chunk_{index}"
        )

        metadatas.append({

            "job_id": job_id,

            "chunk_index": index

        })


    # ------------------------------------------
    # Store Chunks + Embeddings
    # ------------------------------------------

    collection.add(

        ids=ids,

        documents=chunks,

        embeddings=embeddings.tolist(),

        metadatas=metadatas

    )


    return len(chunks)