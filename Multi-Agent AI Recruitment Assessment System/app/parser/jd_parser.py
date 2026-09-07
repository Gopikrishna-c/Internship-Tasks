import pymupdf

KNOWN_SKILLS = [
    "Python", "FastAPI", "SQL", "Redis",
    "Celery", "Git", "PostgreSQL",
    "REST APIs", "Docker"
]

def extract_jd_data(pdf_path: str):
    doc = pymupdf.open(pdf_path)

    text = ""
    for page in doc:
        text += page.get_text()

    skills = []

    for skill in KNOWN_SKILLS:
        if skill.lower() in text.lower():
            skills.append(skill)

    return {
        "title": "Python Developer",
        "company": "Unknown",
        "required_skills": skills,
        "raw_text": text
    }