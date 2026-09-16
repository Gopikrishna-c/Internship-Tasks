from google import genai
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Create Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_candidate(candidate, company):

    prompt = f"""
You are an AI Recruitment Assistant.

Company Requirements:
{company}

Candidate Details:
{candidate}

Analyze the candidate and provide:

1. Match Percentage
2. Strengths
3. Weaknesses
4. Final Recommendation

Give the answer in a professional format.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text