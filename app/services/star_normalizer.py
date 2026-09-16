def normalize_star(data: dict):
    missing = []

    if not data["situation"]:
        missing.append("Situation")
    if not data["task"]:
        missing.append("Task")
    if not data["action"]:
        missing.append("Action")
    if not data["result"]:
        missing.append("Result")

    data["missing_components"] = missing
    return data