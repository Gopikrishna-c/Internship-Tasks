import chromadb

# Create Chroma Database
client = chromadb.PersistentClient(path="chroma_db")

# Create Collection
collection = client.get_or_create_collection(
    name="candidate_profiles"
)