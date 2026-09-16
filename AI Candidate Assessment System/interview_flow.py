from app.chat_memory import add_message, get_chat_history
from app.evaluator import evaluate_answer
from app.dynamic_question import generate_followup_question


def run_interview(candidate_id: int, context: str):

    question = "How did you use FastAPI in your AI Recruitment System?"

    for round_number in range(3):

        # Save question
        add_message(
            candidate_id,
            "assistant",
            question
        )

        print(f"\nQuestion {round_number + 1}:")
        print(question)

        # Candidate answer
        answer = input("\nCandidate Answer:\n")

        # Save answer
        add_message(
            candidate_id,
            "candidate",
            answer
        )

        # Evaluate answer
        evaluation = evaluate_answer(
            question,
            answer
        )

        print("\nAI Evaluation:")
        print(evaluation)

        # Generate next question
        if round_number < 2:

            question = generate_followup_question(
                candidate_id,
                context
            )

            print("\nNext Question:")
            print(question)

    print("\n===== FINAL CHAT HISTORY =====")

    for message in get_chat_history(candidate_id):
        print(message)


if __name__ == "__main__":

    candidate_id = 1

    candidate_context = """
    Candidate Education:
    B.Sc. Computer Science

    Candidate Skills:
    Python, SQL, FastAPI, NumPy, Pandas, Scikit-learn

    Candidate Experience:
    Documentation Executive at PrimaSoft Technologies

    Candidate Project:
    AI Recruitment System using Python, FastAPI,
    Scikit-learn, CountVectorizer and Cosine Similarity.
    """

    run_interview(
        candidate_id,
        candidate_context
    )