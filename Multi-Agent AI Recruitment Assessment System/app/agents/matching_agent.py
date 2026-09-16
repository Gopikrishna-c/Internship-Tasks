from sklearn.metrics.pairwise import cosine_similarity
from app.rag.embeddings import embed_text

def semantic_skill_match(resume_skills: list[str], jd_skills: list[str]):
    resume_embeddings = embed_text(resume_skills)
    jd_embeddings = embed_text(jd_skills)

    matched = []
    missing = []

    for i, jd in enumerate(jd_skills):
        similarities = cosine_similarity(
            [jd_embeddings[i]],
            resume_embeddings
        )[0]

        best_score = similarities.max()
        best_index = similarities.argmax()

        if best_score >= 0.70:
            matched.append({
                "jd_skill": jd,
                "resume_skill": resume_skills[best_index],
                "similarity": round(float(best_score), 2)
            })
        else:
            missing.append(jd)

    percentage = round((len(matched) / len(jd_skills)) * 100, 2)

    return {
        "match_percentage": percentage,
        "matched_skills": matched,
        "missing_skills": missing
    }