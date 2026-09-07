SITUATION = [
    "situation", "project", "problem", "challenge"
]

TASK = [
    "task", "responsibility", "role", "assigned"
]

ACTION = [
    "build", "built", "develop", "developed",
    "implement", "implemented",
    "create", "created",
    "design", "designed"
]

RESULT = [
    "result", "improve", "improved",
    "achieve", "achieved",
    "increase", "increased",
    "reduce", "reduced"
]


def evaluate_star(transcript: str):
    text = transcript.lower()

    def contains(words):
        return any(word in text for word in words)

    s = contains(SITUATION)
    t = contains(TASK)
    a = contains(ACTION)
    r = contains(RESULT)

    return {
        "situation": s,
        "task": t,
        "action": a,
        "result": r,
        "star_score": sum([s, t, a, r]),
        "max_score": 4
    }