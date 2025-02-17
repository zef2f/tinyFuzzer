# tests/test_random_fuzzer.py
import unittest
from core.fuzzer import MutationFuzzer


class TestMutationFuzzer(unittest.TestCase):
    def test_fuzz_length(self):
        mf = MutationFuzzer(seed=["http://www.google.com/search?q=fuzzing"])
        fuzz_input = mf.fuzz()
        fuzz_input = mf.fuzz()
        print(fuzz_input, end='\n')
        self.assertGreaterEqual(len(fuzz_input), 0)
        self.assertLessEqual(len(fuzz_input), 100)

if __name__ == "__main__":
    unittest.main()

