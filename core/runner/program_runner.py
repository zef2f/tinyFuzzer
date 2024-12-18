# core/runner/program_runner.py
from core.runner.base_runner import Runner
from typing import Union, List, Tuple
import subprocess


class ProgramRunner(Runner):
    """Runs an external program with input."""

    def __init__(self, program: Union[str, List[str]]):
        self.program = program

    def run_process(self, inp: str = "") -> subprocess.CompletedProcess:
        return subprocess.run(
            self.program,
            input=inp,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

    def run(self, inp: str = "") -> Tuple[subprocess.CompletedProcess, str]:
        result = self.run_process(inp)

        if result.returncode == 0:
            outcome = self.PASS
        else:
            outcome = self.FAIL

        return result, outcome


if __name__ == "__main__":
    pr = ProgramRunner(["/bin/echo", "2232"])
    print(pr.run())
