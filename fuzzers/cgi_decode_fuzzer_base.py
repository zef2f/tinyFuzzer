# fuzzers/cgi_decode_fuzzer.py

import matplotlib.pyplot as plt
import inspect
from core.coverage import Coverage
from core.fuzzer.random_fuzzer import RandomFuzzer
from targets.cgi_decode import cgi_decode
from typing import List, Tuple, Callable, Set

trials = 100
runs = 300

def population_coverage(population: List[str], function: Callable) -> Tuple[Set[Tuple[str, int]], List[int]]:
    cumulative_coverage: List[int] = []
    all_coverage: Set[Tuple[str, int]] = set()

    for s in population:
        with Coverage() as cov:
            try:
                function(s)
            except Exception as e:
                # print(f"Error detected for input {s}: {e}")
                pass
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))

    return all_coverage, cumulative_coverage


def hundred_inputs(fuzzer: RandomFuzzer) -> List[str]:
    return [fuzzer.fuzz() for _ in range(trials)]


def compare_with_oracle(fuzzer: RandomFuzzer, oracle: Callable, function: Callable, trials: int) -> None:
    """Compare results of `function` and `oracle` for the same inputs."""
    for _ in range(trials):
        s = fuzzer.fuzz()
        try:
            oracle_result = oracle(s)
            function_result = function(s)
            assert oracle_result == function_result, f"Mismatch for input {s}: {oracle_result} != {function_result}"
        except Exception as e:
            print(f"Error comparing results for input {s}: {e}")


if __name__ == "__main__":
    random_fuzzer = RandomFuzzer(min_length=5, max_length=200, char_start=32, char_range=95)

    sum_coverage = [0] * trials

    # Compare `cgi_decode` with an oracle function
    def oracle(s: str) -> str:
        """Python reference implementation of CGI decode."""
        from urllib.parse import unquote_plus
        return unquote_plus(s)

    compare_with_oracle(random_fuzzer, oracle, cgi_decode, trials)
    
    for run in range(runs):
        _, coverage = population_coverage(hundred_inputs(random_fuzzer), cgi_decode)
        assert len(coverage) == trials
        for i in range(trials):
            sum_coverage[i] += coverage[i]

    source_lines, start_line_number = inspect.getsourcelines(cgi_decode)

    max_coverage = [len(source_lines) for i in range(trials)]

    average_coverage = [sum_coverage[i] / runs for i in range(trials)]

    average_coverage_proc = [average_coverage[i] * 100 / max_coverage[i] for i in range(trials)]

    plt.figure(figsize=(10, 6))
    plt.plot(average_coverage_proc, label="Average Coverage (%)", color="blue")
    plt.title('Average coverage of cgi_decode() with random inputs')
    plt.xlabel('# of inputs')
    plt.ylabel('Lines Covered')
    plt.legend()
    plt.grid(True)
    plt.show()
