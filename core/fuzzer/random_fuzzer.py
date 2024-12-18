# core/fuzzer/random_fuzzer.py
from core.fuzzer.base_fuzzer import Fuzzer
import random


class RandomFuzzer(Fuzzer):
    """Generate random input strings for fuzzing."""

    def __init__(self, min_length: int = 10, max_length: int = 100,
                 char_start: int = 32, char_range: int = 32) -> None:
        self.min_length = min_length
        self.max_length = max_length
        self.char_start = char_start
        self.char_range = char_range

    def fuzz(self) -> str:
        string_length = random.randrange(self.min_length, self.max_length + 1)
        return "".join(
            chr(random.randrange(self.char_start, self.char_start + self.char_range))
            for _ in range(string_length)
        )


if __name__ == "__main__":
    rf = RandomFuzzer()
    print(rf.fuzz())
