def rank_candidates(candidates):

    ranked_candidates = sorted(
        candidates,
        key=lambda candidate: candidate["final_score"],
        reverse=True
    )

    for rank, candidate in enumerate(ranked_candidates, start=1):
        candidate["rank"] = rank

    return ranked_candidates


if __name__ == "__main__":

    candidates = [
        {
            "candidate_id": 1,
            "name": "Gopikrishna",
            "semantic_score": 65.4,
            "assessment_score": 3.0,
            "final_score": 47.7
        },
        {
            "candidate_id": 2,
            "name": "Candidate B",
            "semantic_score": 80.0,
            "assessment_score": 8.0,
            "final_score": 80.0
        },
        {
            "candidate_id": 3,
            "name": "Candidate C",
            "semantic_score": 70.0,
            "assessment_score": 6.0,
            "final_score": 65.0
        }
    ]

    ranked = rank_candidates(candidates)

    print("Candidate Ranking:")

    for candidate in ranked:
        print(
            f"Rank {candidate['rank']}: "
            f"{candidate['name']} - "
            f"Final Score: {candidate['final_score']}"
        )