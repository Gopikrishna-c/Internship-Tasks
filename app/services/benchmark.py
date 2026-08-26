def final_benchmark(results):

    scores = [r["score"] for r in results]

    average = round(sum(scores) / len(scores), 1)

    if average >= 9:
        readiness = "Strong Entry-Level"
    elif average >= 7:
        readiness = "Entry-Level Ready"
    elif average >= 5:
        readiness = "Foundation"
    else:
        readiness = "Needs Improvement"

    improvement = []

    if average < 7:
        improvement = [
            "Strengthen Python fundamentals",
            "Practice FastAPI REST APIs",
            "Build more backend projects"
        ]

    return {
        "individual_scores": scores,
        "average_score": average,
        "readiness": readiness,
        "improvement_areas": improvement
    }