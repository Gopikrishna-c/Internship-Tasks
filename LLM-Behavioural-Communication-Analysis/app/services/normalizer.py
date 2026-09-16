def normalize_assessment(value: str):
    mapping = {
        "Good": "Moderate",
        "Strong": "Strong",
        "Moderate": "Moderate",
        "Limited Evidence": "Limited Evidence"
    }
    return mapping.get(value, "Limited Evidence")


def normalize_confidence(value: str):
    mapping = {
        "High": "High",
        "Moderate": "Medium",
        "Medium": "Medium",
        "Low": "Low"
    }
    return mapping.get(value, "Low")