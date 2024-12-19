# fuzzers/cgi_decode_fuzzer.py
import matplotlib.pyplot as plt
from core.coverage import Coverage
from tests.helper.cgi_decode import cgi_decode
from core.fuzzer.random_fuzzer import RandomFuzzer

if __name__ == "__main__":
    random_fuzzer = RandomFuzzer(min_length=5, max_length=20, char_start=32, char_range=95)
    total_iterations = 1000
    coverage_progress = []

    with Coverage() as overall_coverage:
        for iteration in range(total_iterations):
            with Coverage() as iteration_coverage:
                try:
                    fuzz_input = random_fuzzer.fuzz()
                    cgi_decode(fuzz_input)
                except:
                    pass
            filtered_coverage = {entry for entry in overall_coverage.coverage() if entry[0] == 'cgi_decode'}
            coverage_progress.append(len(filtered_coverage))

    plt.figure(figsize=(10, 6))
    plt.plot(range(total_iterations), coverage_progress, label="Coverage Progress", color="blue")
    plt.xlabel("Iteration")
    plt.ylabel("Coverage Count")
    plt.title("Coverage Growth Over Fuzzing Iterations")
    plt.legend()
    plt.grid(True)
    plt.show()
