from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_jd_embeddings(text: str):

    # Create text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # Split JD text into chunks
    chunks = text_splitter.split_text(text)

    # Generate embeddings
    embeddings = embedding_model.encode(chunks)

    return chunks, embeddings