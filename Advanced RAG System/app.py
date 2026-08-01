from loaders.pdf_loader import load_pdf
from chunking.splitter import split_documents
from embeddings.embedding import get_embedding_model
from vectorstore.chroma_db import create_vector_store
from retriever.retriever import get_retriever
from llm.gemini import ask_gemini

# Load PDF
file_path = "data/resume.pdf"
documents = load_pdf(file_path)

# Split Documents
chunks = split_documents(documents)
print(f"Total Chunks: {len(chunks)}")

# Load Embedding Model
embedding_model = get_embedding_model()
print("Embedding Model Loaded Successfully!")

# Create Vector Database
vector_db = create_vector_store(chunks, embedding_model)
print("Vector Database Created Successfully!")

# Create Retriever
retriever = get_retriever(vector_db)
print("Retriever Created Successfully!")

print("\n" + "=" * 60)

while True:

    query = input("\nAsk a Question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    # Retrieve Relevant Chunks
    results = retriever.invoke(query)

    # Combine retrieved chunks into one context
    context = "\n\n".join([doc.page_content for doc in results])

    # Send to Gemini
    answer = ask_gemini(context, query)

    print("\n" + "=" * 60)
    print("AI Answer")
    print("=" * 60)
    print(answer)