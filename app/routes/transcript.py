from fastapi import APIRouter
from app.schemas.transcript import TranscriptInput
from app.services.transcript_processor import clean_transcript
from app.services.qa_extractor import extract_qa
from app.services.communication import analyze_communication
from app.services.behaviour import analyze_behaviour
from app.services.star import analyze_star
from app.services.filler import analyze_fillers
from app.services.scoring import communication_score
from app.services.report import generate_candidate_report
from app.services.report import (
    generate_candidate_report,
    generate_recruiter_report
)

router = APIRouter(prefix="/transcript", tags=["Transcript"])

@router.post("/process")
async def process_transcript(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)

    return {
        "original": data.transcript,
        "cleaned": cleaned
    }

@router.post("/extract-qa")
async def qa_extraction(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa = extract_qa(cleaned)

    return {"qa_pairs": qa}


@router.post("/communication")
async def communication_analysis(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa_pairs = extract_qa(cleaned)

    results = []

    for qa in qa_pairs:
        score = analyze_communication(qa["answer"])
        results.append({
            **qa,
            "communication": score
        })

    return {"analysis": results}

@router.post("/behaviour")
async def behaviour_analysis(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa_pairs = extract_qa(cleaned)

    results = []

    for qa in qa_pairs:
        behaviour = analyze_behaviour(qa["answer"])

        results.append({
            **qa,
            "behaviour": behaviour
        })

    return {"analysis": results}

@router.post("/star")
async def star_analysis(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa_pairs = extract_qa(cleaned)

    results = []

    for qa in qa_pairs:
        results.append({
            **qa,
            "star": analyze_star(qa["answer"])
        })

    return {"analysis": results}

@router.post("/fillers")
async def filler_analysis(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa_pairs = extract_qa(cleaned)

    results = []

    for qa in qa_pairs:
        results.append({
            **qa,
            "fillers": analyze_fillers(qa["answer"])
        })

    return {"analysis": results}
@router.post("/full-analysis")
async def full_analysis(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa_pairs = extract_qa(cleaned)

    results = []

    for qa in qa_pairs:
        comm = analyze_communication(qa["answer"])

        results.append({
            **qa,
            "communication": comm,
            "communication_summary": communication_score(comm),
            "behaviour": analyze_behaviour(qa["answer"]),
            "star": analyze_star(qa["answer"]),
            "fillers": analyze_fillers(qa["answer"])
        })

    return {
        "total_questions": len(results),
        "analysis": results
    }

@router.post("/candidate-report")
async def candidate_report(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa_pairs = extract_qa(cleaned)

    results = []

    for qa in qa_pairs:
        comm = analyze_communication(qa["answer"])

        results.append({
            **qa,
            "communication_summary": communication_score(comm),
            "behaviour": analyze_behaviour(qa["answer"]),
            "fillers": analyze_fillers(qa["answer"])
        })

    report = generate_candidate_report(results)

    return {
        "candidate_report": report
    }

@router.post("/recruiter-report")
async def recruiter_report(data: TranscriptInput):
    cleaned = clean_transcript(data.transcript)
    qa_pairs = extract_qa(cleaned)

    results = []

    for qa in qa_pairs:
        comm = analyze_communication(qa["answer"])

        results.append({
            **qa,
            "communication_summary": communication_score(comm),
            "behaviour": analyze_behaviour(qa["answer"])
        })

    report = generate_recruiter_report(results)

    return {
        "recruiter_report": report
    }