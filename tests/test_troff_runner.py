# tests/test_troff_runner.py
import unittest
from core.runner.troff_runner import TroffRunner


class TestTroffRunner(unittest.TestCase):
    def test_no_violations(self):
        runner = TroffRunner()
        result = runner.run("simpletext")
        self.assertEqual(result[1:], (0, 0, 0))

    def test_backslash_d(self):
        runner = TroffRunner()
        result = runner.run("abc\\D\0")
        self.assertGreater(result[1], 0)

    def test_8bit_violation(self):
        runner = TroffRunner()
        result = runner.run("abcé\n")
        self.assertGreater(result[2], 0)

    def test_dot_violation(self):
        runner = TroffRunner()
        result = runner.run(".\n")
        self.assertGreater(result[3], 0)


if __name__ == "__main__":
    unittest.main()
