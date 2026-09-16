def evaluate_edge_cases(source_code: str):
    namespace = {}

    try:
        exec(source_code, namespace)
        solve = namespace["solve"]

        hidden_cases = [
            "",
            "A",
            "12345",
            "Madam",
            "racecar"
        ]

        results = []
        passed = 0

        for case in hidden_cases:
            output = solve(case)
            expected = case[::-1]

            ok = output == expected

            if ok:
                passed += 1

            results.append({
                "input": case,
                "expected": expected,
                "output": output,
                "passed": ok
            })

        score = round((passed / len(hidden_cases)) * 10, 2)

        return {
            "edge_case_score": score,
            "edge_cases": results
        }

    except Exception as e:
        return {
            "edge_case_score": 0,
            "error": str(e)
        }