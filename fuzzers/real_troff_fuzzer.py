# fuzzers/real_troff_fuzzer.py
from core.fuzzer.random_fuzzer import RandomFuzzer
from core.runner.binary_program_runner import BinaryProgramRunner

def main():
    fuzz = RandomFuzzer(5, 500, 0, 255)
    results = fuzz.runs(BinaryProgramRunner("troff"), trials=1000)

    for result, outcome in results:
        if outcome != "PASS":
            print(f"Failing input: {result}, Outcome: {outcome}")

if __name__ == "__main__":
    main()
