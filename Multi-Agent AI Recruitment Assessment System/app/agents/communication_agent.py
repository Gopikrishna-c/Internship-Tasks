import re

FILLER_WORDS = [
    "um", "uh", "ah", "like", "you know"
]

def analyze_communication(transcript: str):
    words = transcript.split()
    total_words = len(words)

    filler_count = 0

    for word in words:
        if word.lower().strip(".,!?") in FILLER_WORDS:
            filler_count += 1

    clarity = max(
        0,
        round(10 - (filler_count * 0.5), 2)
    )

    return {
        "word_count": total_words,
        "filler_words": filler_count,
        "communication_score": clarity
    }