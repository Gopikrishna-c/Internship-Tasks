def recommend_roles(profile: dict):

    skills = [s.lower() for s in profile["skills"]]

    roles = []

    if "python" in skills:
        roles.append("Python Developer")

    if "fastapi" in skills:
        roles.append("Backend Developer")

    if "scikit-learn" in skills:
        roles.append("Machine Learning Engineer")

    if "pandas" in skills:
        roles.append("Data Analyst")

    if "git" in skills:
        roles.append("Software Engineer")

    return roles[:5]