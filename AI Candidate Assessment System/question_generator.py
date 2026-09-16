from app.rag_engine import build_candidate_context
from app.chat_memory import add_message, get_chat_history


def generate_questions(context: str):

    questions = []

    if "FastAPI" in context:
        questions.append(
            "How did you use FastAPI in your AI Recruitment System?"
        )

    if "Scikit-learn" in context:
        questions.append(
            "How did you use Scikit-learn for candidate matching?"
        )

    if "CountVectorizer" in context:
        questions.append(
            "Why did you use CountVectorizer in your project?"
        )

    if "Cosine Similarity" in context:
        questions.append(
            "How does Cosine Similarity help in your candidate recommendation system?"
        )

    return questions


def get_next_question(candidate_id: int, questions: list):

    history = get_chat_history(candidate_id)

    asked_questions = [
        message["content"]
        for message in history
        if message["role"] == "assistant"
    ]

    for question in questions:

        if question not in asked_questions:

            add_message(
                candidate_id,
                "assistant",
                question
            )

            return question

    return None


if __name__ == "__main__":

    education = {
        "degree": "B.Sc. Computer Science",
        "college": "Rajapalayam Rajus' College"
    }

    skills = {
        "programming_languages": ["Python", "SQL"],
        "frameworks": ["FastAPI"],
        "libraries": ["NumPy", "Pandas", "Scikit-learn"]
    }

    experience = {
        "job_title": "Documentation Executive",
        "company": "PrimaSoft Technologies"
    }

    projects = """
    AI Recruitment System using Python, FastAPI,
    Scikit-learn, CountVectorizer and Cosine Similarity.
    """

    context = build_candidate_context(
        education,
        skills,
        experience,
        projects
    )

    questions = generate_questions(context)

    candidate_id = 1

    print("Generated Questions:")

    for i, question in enumerate(questions, start=1):
        print(f"{i}. {question}")

    print("\nNext Question:")

    next_question = get_next_question(
        candidate_id,
        questions
    )

    print(next_question)