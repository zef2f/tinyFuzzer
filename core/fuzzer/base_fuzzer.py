# core/fuzzer/base_fuzzer.py
from core.runner.base_runner import Runner
from core.runner.print_runner import PrintRunner
from typing import Tuple, List
import subprocess


class Fuzzer:
    """Base class for generating fuzzing input."""

    def __init__(self) -> None:
        pass

    def fuzz(self) -> str:
        """Return fuzz input."""
        return ""

    def run(self, runner: Runner = Runner()) -> Tuple[subprocess.CompletedProcess, str]:
        return runner.run(self.fuzz())

    def runs(self, runner: Runner = PrintRunner(), trials: int = 10) -> List[Tuple[subprocess.CompletedProcess, str]]:
        """Run the runner with fuzz input multiple times."""
        return [self.run(runner) for _ in range(trials)]


if __name__ == "__main__":
    fuzzer = Fuzzer()
    results = fuzzer.runs(trials=3)
    print(results)
