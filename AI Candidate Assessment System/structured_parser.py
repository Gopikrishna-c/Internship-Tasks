def parse_education(education_text: str):

    lines = [
        line.strip()
        for line in education_text.splitlines()
        if line.strip()
    ]

    return {
        "degree": lines[1] if len(lines) > 1 else None,
        "college": lines[2] if len(lines) > 2 else None,
        "university": lines[3] if len(lines) > 3 else None,
        "graduation": lines[4] if len(lines) > 4 else None
    }


def parse_skills(skills_text: str):

    lines = [
        line.strip()
        for line in skills_text.splitlines()
        if line.strip()
    ]

    skills = {
        "programming_languages": [],
        "frameworks": [],
        "libraries": [],
        "tools": [],
        "core_concepts": []
    }

    for line in lines:

        if line.startswith("Programming Languages:"):
            values = line.split(":", 1)[1]
            skills["programming_languages"] = [
                item.strip()
                for item in values.split(",")
            ]

        elif line.startswith("Framework:"):
            values = line.split(":", 1)[1]
            skills["frameworks"] = [
                item.strip()
                for item in values.split(",")
            ]

        elif line.startswith("Libraries:"):
            values = line.split(":", 1)[1]
            skills["libraries"] = [
                item.strip()
                for item in values.split(",")
            ]

        elif line.startswith("Tools:"):
            values = line.split(":", 1)[1]
            skills["tools"] = [
                item.strip()
                for item in values.split(",")
            ]

        elif line.startswith("Core Concepts:"):
            values = line.split(":", 1)[1]
            skills["core_concepts"] = [
                item.strip()
                for item in values.split(",")
            ]

    return skills


def parse_experience(experience_text: str):

    lines = [
        line.strip()
        for line in experience_text.splitlines()
        if line.strip()
    ]

    return {
        "job_title": lines[1] if len(lines) > 1 else None,
        "company": lines[2] if len(lines) > 2 else None,
        "location_duration": lines[3] if len(lines) > 3 else None,
        "responsibilities": lines[4:] if len(lines) > 4 else []
    }


if __name__ == "__main__":

    education_text = """EDUCATION
Bachelor of Science (B.Sc.) in Computer Science
Rajapalayam Rajus' College
Madurai Kamaraj University
Graduated: May 2025
"""

    skills_text = """TECHNICAL SKILLS
Programming Languages: Python, SQL (Basics)
Framework: FastAPI
Libraries: NumPy, Pandas, Matplotlib, Scikit-learn
Tools: Git, GitHub, Jupyter Notebook, Visual Studio Code
Core Concepts: Object-Oriented Programming (OOP), File Handling, REST APIs, Machine Learning
"""

    experience_text = """PROFESSIONAL EXPERIENCE
Documentation Executive
PrimaSoft Technologies Pvt. Ltd.,
ChennaiJune 2025 – Present
Performed KYC verification and document validation to ensure regulatory compliance.
Managed merchant onboarding by verifying customer documents and information.
Maintained accurate customer records through data validation and verification.
Processed customer applications within defined Turnaround Time (TAT) while maintaining quality standards.
Coordinated with internal teams to resolve documentation discrepancies efficiently.
"""

    education_result = parse_education(education_text)
    skills_result = parse_skills(skills_text)
    experience_result = parse_experience(experience_text)

    print("Education:")
    print(education_result)

    print("\nSkills:")
    print(skills_result)

    print("\nExperience:")
    print(experience_result)