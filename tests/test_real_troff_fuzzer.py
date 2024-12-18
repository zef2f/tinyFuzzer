# tests/test_real_troff_fuzzer.py
import unittest
from core.fuzzer.random_fuzzer import RandomFuzzer
from core.runner.binary_program_runner import BinaryProgramRunner

class TestRealTroffFuzzer(unittest.TestCase):
    def test_real_troff_fuzzer(self):
        fuzzer = RandomFuzzer(5, 500, 0, 255)
        runner = BinaryProgramRunner("cat")  # "troff" может отсутствовать локально
        results = fuzzer.runs(runner, trials=10)

        self.assertEqual(len(results), 10)
        self.assertTrue(all(result is not None for result, _ in results))


if __name__ == "__main__":
    unittest.main()
