def get_retriever(vector_db):

    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 3,
            "fetch_k": 5
        }
    )

    return retriever