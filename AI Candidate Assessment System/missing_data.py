def find_missing_data(education, skills):

    missing_data = []

    if not education:
        missing_data.append("education")

    if not skills:
        missing_data.append("skills")

    return missing_data

if __name__ == "__main__":

    education = {
        "degree": "B.Sc Computer Science"
    }

    skills = {}

    result = find_missing_data(education, skills)

    print(result)