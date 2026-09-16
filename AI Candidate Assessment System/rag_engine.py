def build_candidate_context(
    education,
    skills,
    experience,
    projects
):
    context = f"""
Candidate Education:
{education}

Candidate Skills:
{skills}

Candidate Experience:
{experience}

Candidate Projects:
{projects}
"""

    return context

if __name__ == "__main__":

    education = {
        "degree": "B.Sc. Computer Science",
        "college": "Rajapalayam Rajus' College"
    }

    skills = {
        "programming_languages": ["Python", "SQL"],
        "frameworks": ["FastAPI"],
        "libraries": ["NumPy", "Pandas", "Scikit-learn"]
    }

    experience = {
        "job_title": "Documentation Executive",
        "company": "PrimaSoft Technologies"
    }

    projects = """
    AI Recruitment System using Python, FastAPI,
    Scikit-learn, CountVectorizer and Cosine Similarity.
    """

    context = build_candidate_context(
        education,
        skills,
        experience,
        projects
    )

    print(context)