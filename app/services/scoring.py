def communication_score(comm: dict):
    values = [
        comm["clarity"],
        comm["relevance"],
        comm["structure"],
        comm["conciseness"],
        comm["professional_communication"]
    ]

    score = round(sum(values) / len(values), 1)

    if score >= 9:
        level = "Excellent"
    elif score >= 7:
        level = "Good"
    elif score >= 5:
        level = "Average"
    else:
        level = "Needs Improvement"

    return {"score": score, "level": level}