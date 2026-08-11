import os

from pypdf import PdfReader
from docx import Document


def clean_text(text: str) -> str:

    text = text.replace("\n", " ")

    text = " ".join(
        text.split()
    )

    return text.strip()


def load_document(file_path: str) -> str:

    extension = os.path.splitext(
        file_path
    )[1].lower()

    # ==============================
    # PDF
    # ==============================

    if extension == ".pdf":

        reader = PdfReader(
            file_path
        )

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += (
                    page_text + "\n"
                )

        return clean_text(text)

    # ==============================
    # DOCX
    # ==============================

    elif extension == ".docx":

        document = Document(
            file_path
        )

        text = ""

        for paragraph in document.paragraphs:

            text += (
                paragraph.text + "\n"
            )

        return clean_text(text)

    # ==============================
    # TXT
    # ==============================

    elif extension == ".txt":

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

        return clean_text(text)

    # ==============================
    # Unsupported file
    # ==============================

    else:

        raise ValueError(
            "Only PDF, DOCX and TXT files are supported"
        )