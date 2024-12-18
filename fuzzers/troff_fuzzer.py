# fuzzers/troff_fuzzer.py
from core.fuzzer.random_fuzzer import RandomFuzzer
from core.runner.troff_runner import TroffRunner

def main():
    fuzz = RandomFuzzer(50, 500, 0, 255)
    results = fuzz.runs(TroffRunner(), trials=1000)
    print(results)

if __name__ == "__main__":
    main()

