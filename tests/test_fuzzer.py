# tests/test_fuzzer.py
import unittest
from core.fuzzer import Fuzzer


class TestFuzzer(unittest.TestCase):
    def test_fuzz(self):
        fuzzer = Fuzzer()
        self.assertEqual(fuzzer.fuzz(), "")

    def test_runs(self):
        fuzzer = Fuzzer()
        results = fuzzer.runs(trials=3)
        self.assertEqual(len(results), 3)


if __name__ == "__main__":
    unittest.main()
