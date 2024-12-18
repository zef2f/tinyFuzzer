# core/runner/print_runner.py
from typing import Any
from core.runner.base_runner import Runner


class PrintRunner(Runner):
    """ Simple runner that prints the input """

    def run(self, inp: str) -> Any:
        print(inp)
        return (inp, Runner.UNRESOLVED)


if __name__ == "__main__":
    pr = PrintRunner()
    pr.run("hi, denis. are u rly alive?")
