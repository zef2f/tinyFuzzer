# tests/test_binary_program_runner.py
import unittest
from core.runner import BinaryProgramRunner


class TestBinaryProgramRunner(unittest.TestCase):
    def test_binary_program_runner_pass(self):
        bpr = BinaryProgramRunner("cat")
        result, outcome = bpr.run("hello")
        self.assertEqual(result.stdout.decode().strip(), "hello")
        self.assertEqual(outcome, bpr.PASS)


if __name__ == "__main__":
    unittest.main()
