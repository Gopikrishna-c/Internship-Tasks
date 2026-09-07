import pymupdf
import re

KNOWN_SKILLS = [
    "Python",
    "FastAPI",
    "SQL",
    "NumPy",
    "Pandas",
    "Matplotlib",
    "Scikit-learn",
    "Git",
    "GitHub",
    "Jupyter Notebook",
    "REST APIs",
    "Object-Oriented Programming",
    "OOP"
]


def extract_resume_data(pdf_path: str):
    doc = pymupdf.open(pdf_path)

    text = ""
    for page in doc:
        text += page.get_text()

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Name
    name = lines[0] if lines else None

    # Email
    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    # Phone
    phone = re.search(r'(\+91[- ]?)?[6-9]\d{9}', text)

    # Location
    location = None
    loc_match = re.search(r'Location:\s*(.*)', text)
    if loc_match:
        location = loc_match.group(1).strip()

    # Education
    education = []
    if "Bachelor of Science" in text:
        education.append("B.Sc Computer Science")

    # Experience
    experience = []
    if "Documentation Executive" in text:
        experience.append("Documentation Executive")

    # Projects
    projects = []
    if "AI Recruitment System" in text:
        projects.append("AI Recruitment System")

    # Skills
    skills = []
    for skill in KNOWN_SKILLS:
        if skill.lower() in text.lower():
            skills.append(skill)

    return {
        "name": name,
        "email": email.group() if email else None,
        "phone": phone.group() if phone else None,
        "location": location,
        "education": education,
        "experience": experience,
        "skills": skills,
        "projects": projects,
        "raw_text": text
    }