chat_history = {}


def add_message(candidate_id: int, role: str, content: str):

    if candidate_id not in chat_history:
        chat_history[candidate_id] = []

    chat_history[candidate_id].append({
        "role": role,
        "content": content
    })


def get_chat_history(candidate_id: int):

    return chat_history.get(candidate_id, [])

if __name__ == "__main__":

    candidate_id = 1

    add_message(
        candidate_id,
        "assistant",
        "How did you use FastAPI in your AI Recruitment System?"
    )

    add_message(
        candidate_id,
        "candidate",
        "I used FastAPI to build REST APIs for candidate recommendation."
    )

    print("Chat History:")
    print(get_chat_history(candidate_id))