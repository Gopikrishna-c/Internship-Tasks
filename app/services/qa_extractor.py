import re

def extract_qa(transcript: str):
    lines = transcript.split("\n")
    qa_pairs = []

    question = None
    q_count = 1

    for line in lines:
        if line.startswith("Interviewer:"):
            question = line.replace("Interviewer:", "").strip()

        elif line.startswith("Candidate:") and question:
            answer = line.replace("Candidate:", "").strip()

            qa_pairs.append({
                "question_id": f"Q{q_count:02}",
                "question": question,
                "answer_id": f"A{q_count:02}",
                "answer": answer
            })

            q_count += 1
            question = None

    return qa_pairs