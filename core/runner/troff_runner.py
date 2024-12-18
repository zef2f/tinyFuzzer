# core/runner/troff_runner.py
from core.runner.base_runner import Runner
from typing import Tuple
from targets import troff_check


class TroffRunner(Runner):
    """TroffRunner checks troff-specific rules."""

    def __init__(self):
        self.no_backslash_d_failures = 0
        self.no_8bit_failures = 0
        self.no_dot_failures = 0

    def run(self, inp: str = "") -> Tuple[str, int, int, int]:
        try:
            troff_check.no_backslash_d(inp)
        except AssertionError:
            self.no_backslash_d_failures += 1

        try:
            troff_check.no_8bit(inp)
        except AssertionError:
            self.no_8bit_failures += 1

        try:
            troff_check.no_dot(inp)
        except AssertionError:
            self.no_dot_failures += 1

        return (inp, self.no_backslash_d_failures, self.no_8bit_failures, self.no_dot_failures)


if __name__ == "__main__":
    tr = TroffRunner()
    print(tr.run("sdfsdfkhsdkjf"))
