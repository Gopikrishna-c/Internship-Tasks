def calculate_completeness(profile: dict):

    score = 0
    missing = []

    # Basic Details
    if profile["name"]:
        score += 10
    else:
        missing.append("name")

    if profile["email"]:
        score += 10
    else:
        missing.append("email")

    if profile["phone"]:
        score += 10
    else:
        missing.append("phone")

    if profile["location"]:
        score += 10
    else:
        missing.append("location")

    # Education
    if profile["education"]:
        score += 20
    else:
        missing.append("education")

    # Skills
    if profile["skills"]:
        score += 20
    else:
        missing.append("skills")

    # Experience
    if profile["experience"]:
        score += 20
    else:
        missing.append("experience")

    return {
        "completeness_score": score,
        "missing_fields": missing
    }