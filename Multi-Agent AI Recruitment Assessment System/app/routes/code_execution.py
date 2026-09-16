from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import CodeSubmission, CodingQuestion
from app.agents.code_execution_agent import execute_solution
from app.agents.complexity_agent import calculate_complexity
from app.agents.edge_case_agent import evaluate_edge_cases

router = APIRouter(prefix="/submission", tags=["Code Execution"])


@router.post("/{submission_id}/execute")
async def execute_code(
    submission_id: int,
    db: AsyncSession = Depends(get_db)
):
    submission = await db.get(CodeSubmission, submission_id)

    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    question = await db.get(CodingQuestion, submission.question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    # Functional Testing
    execution = execute_solution(
        submission.source_code,
        question.test_cases,
        question.expected_output
    )

    # Code Quality
    complexity = calculate_complexity(
        submission.source_code
    )

    # Hidden Edge Cases
    edge = evaluate_edge_cases(
        submission.source_code
    )

    submission.status = (
        "passed" if execution["score"] == 10 else "evaluated"
    )

    await db.commit()

    return {
        **execution,
        **complexity,
        **edge
    }