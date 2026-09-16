import re

FILLERS = [
    "um", "uh", "actually", "basically",
    "like", "you know", "i mean"
]

def analyze_fillers(answer: str):
    text = answer.lower()

    found = {}
    total = 0

    for word in FILLERS:
        count = len(re.findall(rf"\b{re.escape(word)}\b", text))
        if count > 0:
            found[word] = count
            total += count

    return {
        "total_fillers": total,
        "filler_words": found
    }