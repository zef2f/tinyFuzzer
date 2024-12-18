# core/runner/base_runner.py
from typing import Any

class Runner:
    """ Base class for testing inputs """

    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"

    def __init__(self) -> None:
        """ Initialize """
        pass

    def run(self, inp: str) -> Any:
        """ Run the runner with given input """
        return (inp, Runner.UNRESOLVED)

if __name__ == "__main__":
    runner = Runner()
    assert runner.run("hello")[0] == "hello"
