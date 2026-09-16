from app.missing_data import find_missing_data


def generate_gap_questions(education, skills):

    missing_data = find_missing_data(
        education,
        skills
    )

    questions = []

    if "education" in missing_data:
        questions.append(
            "Could you provide your highest educational qualification?"
        )

    if "skills" in missing_data:
        questions.append(
            "Could you provide your main technical skills?"
        )

    return questions


def collect_missing_information(education, skills):

    questions = generate_gap_questions(
        education,
        skills
    )

    updated_data = {
        "education": education,
        "skills": skills
    }

    for question in questions:

        print("\nAI Question:")
        print(question)

        answer = input("\nCandidate Answer:\n")

        if "education" in question.lower():
            updated_data["education"] = {
                "qualification": answer
            }

        elif "skills" in question.lower():
            updated_data["skills"] = {
                "technical_skills": answer
            }

    return updated_data


if __name__ == "__main__":

    education = {
        "degree": "B.Sc Computer Science"
    }

    skills = {}

    updated_data = collect_missing_information(
        education,
        skills
    )

    print("\nUpdated Candidate Data:")
    print(updated_data)