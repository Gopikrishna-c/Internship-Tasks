def extract_sections(text: str):

    sections = {}

    education_start = text.find("EDUCATION")
    projects_start = text.find("PROJECTS")
    experience_start = text.find("PROFESSIONAL EXPERIENCE")
    skills_start = text.find("TECHNICAL SKILLS")

    sections["education"] = text[
        education_start:projects_start
    ]

    sections["projects"] = text[
        projects_start:experience_start
    ]

    sections["experience"] = text[
        experience_start:skills_start
    ]

    sections["skills"] = text[
        skills_start:
    ]

    return sections