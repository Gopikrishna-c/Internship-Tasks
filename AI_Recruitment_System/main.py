from fastapi import FastAPI
import json
from recommendation import get_best_candidate
from llm import analyze_candidate

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Recruitment Recommendation System"
    }


@app.get("/candidates")
def get_candidates():
    with open("candidate.json", "r") as file:
        candidates = json.load(file)
    return candidates


@app.get("/company")
def get_company():
    with open("company.json", "r") as file:
        company = json.load(file)
    return company


# Dynamic Recommendation API
@app.get("/recommend/{company_name}")
def recommend(company_name: str):

    result = get_best_candidate(company_name)

    return result


# AI Recommendation API
@app.get("/ai-recommend/{company_name}")
def ai_recommend(company_name: str):

    result = get_best_candidate(company_name)

    if "error" in result:
        return result

    # Load all companies
    with open("company.json", "r") as file:
        companies = json.load(file)

    # Find selected company
    company = None
    for c in companies:
        if c["company"].lower() == company_name.lower():
            company = c
            break

    # Generate AI Report
    report = analyze_candidate(
        result["recommended_candidate"],
        company
    )

    return {
        "company": company["company"],
        "recommended_candidate": result["recommended_candidate"],
        "similarity_score": result["similarity_score"],
        "ai_report": report
    }