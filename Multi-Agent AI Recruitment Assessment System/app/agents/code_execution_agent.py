import json
from app.agents.e2b_agent import run_in_sandbox


def execute_solution(source_code, test_cases, expected_output):
    results = []
    passed = 0

    for test_input, expected in zip(test_cases, expected_output):

        code = f"""
{source_code}

result = solve({json.dumps(test_input)})
print(result)
"""

        execution = run_in_sandbox(code)

        # Debug (temporary)
        print(execution)

        output = execution["stdout"].strip()

        is_pass = execution["success"] and output == expected

        if is_pass:
            passed += 1

        results.append({
            "input": test_input,
            "expected": expected,
            "output": output,
            "passed": is_pass
        })

    score = round((passed / len(test_cases)) * 10)

    return {
        "score": score,
        "passed": passed,
        "total": len(test_cases),
        "results": results
    }