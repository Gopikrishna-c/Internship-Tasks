def calculate_final_score(scores: list):

    if not scores:
        return 0

    average_score = sum(scores) / len(scores)

    return round(average_score, 2)


if __name__ == "__main__":

    scores = [3, 3, 3]

    final_score = calculate_final_score(scores)

    print("Individual Scores:", scores)
    print("Final Assessment Score:", final_score)