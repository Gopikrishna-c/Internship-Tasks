import ollama
import json

MODEL = "llama3.2:3b"

def generate_report(answers_text):

    prompt = f"""
You are an AI interview evaluator.

Interview Transcript:
{answers_text}

Return ONLY valid JSON.

{{
  "overall_score": 85,
  "strengths": [
    "..."
  ],
  "gaps": [
    "..."
  ],
  "recommendations": [
    "..."
  ]
}}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "Return only JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response["message"]["content"]
    content = content.replace("```json","").replace("```","").strip()

    return json.loads(content)