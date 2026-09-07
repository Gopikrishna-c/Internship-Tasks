import ast

DECISION_NODES = (
    ast.If,
    ast.For,
    ast.While,
    ast.Try,
    ast.IfExp,
    ast.With,
    ast.BoolOp
)


def calculate_complexity(source_code: str):
    tree = ast.parse(source_code)

    complexity = 1

    for node in ast.walk(tree):
        if isinstance(node, DECISION_NODES):
            complexity += 1

    if complexity <= 3:
        grade = "Easy"
    elif complexity <= 6:
        grade = "Medium"
    else:
        grade = "Hard"

    return {
        "cyclomatic_complexity": complexity,
        "grade": grade
    }