# tests/test_random_fuzzer.py
import unittest
from core.fuzzer import RandomFuzzer


class TestRandomFuzzer(unittest.TestCase):
    def test_fuzz_length(self):
        rf = RandomFuzzer(min_length=5, max_length=10)
        fuzz_input = rf.fuzz()
        self.assertGreaterEqual(len(fuzz_input), 5)
        self.assertLessEqual(len(fuzz_input), 10)

    def test_fuzz_characters(self):
        rf = RandomFuzzer(char_start=65, char_range=26)
        fuzz_input = rf.fuzz()
        for c in fuzz_input:
            self.assertGreaterEqual(ord(c), 65)
            self.assertLessEqual(ord(c), 90)


if __name__ == "__main__":
    unittest.main()
