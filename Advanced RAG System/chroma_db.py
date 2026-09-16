from langchain_chroma import Chroma
import shutil
import os


def create_vector_store(chunks, embedding_model):

    if os.path.exists("chroma_db"):
        shutil.rmtree("chroma_db")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vector_db