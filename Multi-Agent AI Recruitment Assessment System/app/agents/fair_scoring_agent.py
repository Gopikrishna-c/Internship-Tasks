def generate_fair_report(candidate, metrics):
    return {
        "candidate_id": candidate.id,

        # Personal details removed
        "masked": True,

        # Merit only
        "technical_score": metrics["score"],
        "skill_match": metrics["skill_match"],
        "edge_case_score": metrics["edge_case_score"],
        "complexity": metrics["grade"],

        "overall_score": round(
            (
                metrics["score"] +
                metrics["edge_case_score"] +
                metrics["skill_match"] / 10
            ) / 3,
            2
        )
    }