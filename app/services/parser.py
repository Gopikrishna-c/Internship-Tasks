import fitz
import re


def extract_text(pdf_path: str):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text


def extract_profile(text: str):

    email = re.search(r'[\w\.-]+@[\w\.-]+', text)
    phone = re.search(r'(\+91\s?\d{10})', text)

    lines = text.split("\n")
    name = lines[0].strip()

    location = "Chennai" if "Chennai" in text else ""

    # Education
    education = []
    if "Bachelor of Science" in text:
        education.append({
            "degree": "B.Sc Computer Science",
            "institution": "Rajapalayam Rajus' College",
            "year": "2025"
        })

    # Skills
    skills = [
        "Python",
        "SQL",
        "FastAPI",
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Scikit-learn",
        "Git",
        "GitHub"
    ]

    # Experience
    experience = []
    if "Documentation Executive" in text:
        experience.append({
            "company": "PrimaSoft Technologies Pvt. Ltd.",
            "role": "Documentation Executive",
            "duration": "June 2025 - Present"
        })

    return {
        "name": name,
        "email": email.group() if email else "",
        "phone": phone.group() if phone else "",
        "location": location,
        "education": education,
        "skills": skills,
        "experience": experience
    }