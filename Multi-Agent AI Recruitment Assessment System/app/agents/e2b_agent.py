from e2b_code_interpreter import Sandbox
from app.config import E2B_API_KEY


def run_in_sandbox(code: str):
    try:
        with Sandbox.create(api_key=E2B_API_KEY) as sandbox:
            execution = sandbox.run_code(code)

            stdout = ""
            if execution.logs.stdout:
                stdout = "\n".join(execution.logs.stdout)

            stderr = ""
            if execution.logs.stderr:
                stderr = "\n".join(execution.logs.stderr)

            return {
                "success": stderr == "",
                "stdout": stdout.strip(),
                "stderr": stderr.strip()
            }

    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e)
        }