def generate_candidate_report(results):
    strengths = []
    improvements = []

    for item in results:
        if item["communication_summary"]["score"] >= 7:
            strengths.append(
                f"{item['question_id']}: Good communication"
            )
        else:
            improvements.append(
                f"{item['question_id']}: Improve clarity and structure"
            )

        if item["behaviour"]["problem_solving"]["assessment"] == "Strong":
            strengths.append(
                f"{item['question_id']}: Strong problem solving"
            )

        if item["fillers"]["total_fillers"] > 0:
            improvements.append(
                f"{item['question_id']}: Reduce filler words"
            )

    return {
        "strengths": strengths,
        "improvement_areas": improvements
    }


def generate_recruiter_report(results):
    total_score = 0
    behaviour_evidence = []

    for item in results:
        total_score += item["communication_summary"]["score"]

        for indicator, value in item["behaviour"].items():
            if (
                value["assessment"] != "Limited Evidence"
                and value["evidence"] != ""
            ):
                behaviour_evidence.append({
                    "question_id": item["question_id"],
                    "indicator": indicator.replace("_", " ").title(),
                    "assessment": value["assessment"],
                    "evidence": value["evidence"],
                    "confidence": value["confidence"]
                })

    avg = round(total_score / len(results), 1)

    return {
        "executive_summary": {
            "average_communication_score": avg,
            "total_questions": len(results)
        },
        "behaviour_evidence": behaviour_evidence,
        "recommendation_support":
            "AI-assisted evaluation only. Final hiring decision must be made by authorized recruiters."
    }