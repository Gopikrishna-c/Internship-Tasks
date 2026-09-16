def shortlist_candidate(report: dict):
    score = report["overall_score"]

    if score >= 8.5:
        status = "SHORTLISTED"
        notify_hr = True

    elif score >= 7:
        status = "REVIEW"
        notify_hr = False

    else:
        status = "REJECTED"
        notify_hr = False

    return {
        "candidate_id": report["candidate_id"],
        "overall_score": score,
        "status": status,
        "notify_hr": notify_hr
    }