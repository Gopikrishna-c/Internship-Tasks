from app.chat_memory import add_message, get_chat_history


def save_candidate_answer(candidate_id: int, answer: str):

    add_message(
        candidate_id,
        "candidate",
        answer.strip()
    )


def get_conversation(candidate_id: int):

    return get_chat_history(candidate_id)


if __name__ == "__main__":

    candidate_id = 1

    # Previous question
    question = "How did you use FastAPI in your AI Recruitment System?"

    add_message(
        candidate_id,
        "assistant",
        question
    )

    # Candidate answer
    answer = """
    I used FastAPI to build REST APIs for
    candidate recommendation.
    """

    save_candidate_answer(
        candidate_id,
        answer
    )

    print("Conversation:")

    for message in get_conversation(candidate_id):
        print(message)