import re


def clean_jd_text(text: str):

    # Remove unwanted special characters
    text = text.replace("\x7f", "")

    # Replace multiple spaces/tabs with one space
    text = re.sub(r"[ \t]+", " ", text)

    # Remove unnecessary blank lines
    text = re.sub(r"\n\s*\n+", "\n", text)

    # Clean each line
    lines = []

    for line in text.split("\n"):

        line = line.strip()

        if line:
            lines.append(line)

    # Join all cleaned lines
    cleaned_text = "\n".join(lines)

    return cleaned_text