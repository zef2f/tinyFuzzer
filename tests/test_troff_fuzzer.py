# tests/test_troff_fuzzer.py
import unittest
from core.fuzzer.random_fuzzer import RandomFuzzer
from core.runner.troff_runner import TroffRunner


class TestTroffFuzzer(unittest.TestCase):
    def test_fuzzer_runs(self):
        fuzzer = RandomFuzzer()
        runner = TroffRunner()
        results = fuzzer.runs(runner, trials=5)
        self.assertEqual(len(results), 5)


if __name__ == "__main__":
    unittest.main()
