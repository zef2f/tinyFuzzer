# tests/test_program_runner.py
import unittest
from core.runner import ProgramRunner


class TestProgramRunner(unittest.TestCase):
    def test_program_runner_pass(self):
        import shutil

        echo_path = shutil.which("echo")
        self.assertIsNotNone(echo_path, "Команда echo не найдена в системе!")

        pr = ProgramRunner([echo_path, "hello"])
        result, outcome = pr.run()
        self.assertEqual(result.stdout.strip(), "hello")
        self.assertEqual(outcome, pr.PASS)

    def test_program_runner_fail(self):
        pr = ProgramRunner("/bin/false")
        _, outcome = pr.run()
        self.assertEqual(outcome, pr.FAIL)


if __name__ == "__main__":
    unittest.main()
