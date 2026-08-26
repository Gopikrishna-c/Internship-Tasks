from app.rag.vector_db import collection

def ingest_profile(profile: dict):

    document = f"""
    Candidate Name: {profile['name']}

    Skills:
    {", ".join(profile['skills'])}

    Education:
    {profile['education']}

    Experience:
    {profile['experience']}
    """

    collection.add(
        documents=[document],
        ids=[profile["email"]]
    )

    return True