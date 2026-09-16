import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_best_candidate(company_name):

    # Load candidates
    with open("candidate.json", "r") as file:
        candidates = json.load(file)

    # Load companies
    with open("company.json", "r") as file:
        companies = json.load(file)

    # Find selected company
    company = None
    for c in companies:
        if c["company"].lower() == company_name.lower():
            company = c
            break

    if company is None:
        return {"error": "Company not found"}

    company_text = " ".join(company["required_skills"])

    best_candidate = None
    best_score = 0

    for candidate in candidates:

        candidate_text = " ".join(candidate["skills"])

        vectorizer = CountVectorizer()

        vectors = vectorizer.fit_transform(
            [company_text, candidate_text]
        )

        score = cosine_similarity(vectors)[0][1]

        if (
            score > best_score
            and candidate["experience"] >= company["experience"]
        ):
            best_score = score
            best_candidate = candidate

    return {
        "company": company["company"],
        "recommended_candidate": best_candidate,
        "similarity_score": round(float(best_score), 2)
    }