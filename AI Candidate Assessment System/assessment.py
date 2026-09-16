def create_evaluation(question: str, answer: str):

    return {
        "question": question,
        "answer": answer,
        "status": "pending"
    }


if __name__ == "__main__":

    question = "How did you use FastAPI in your AI Recruitment System?"

    answer = """
    I used FastAPI to build REST APIs for
    candidate recommendation.
    """

    evaluation = create_evaluation(question, answer)

    print("Evaluation:")
    print(evaluation)