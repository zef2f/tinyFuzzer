# fuzzers/cgi_decode_fuzzer.py

import matplotlib.pyplot as plt
from core.coverage import Coverage
from tests.helper.cgi_decode import cgi_decode
from core.fuzzer.random_fuzzer import RandomFuzzer
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
            except:
                pass
        all_coverage |= cov.coverage()
        cumulative_coverage.append(len(all_coverage))

    return all_coverage, cumulative_coverage


def hundred_inputs(fuzzer: RandomFuzzer) -> List[str]:
    return [fuzzer.fuzz() for _ in range(trials)]


if __name__ == "__main__":
    random_fuzzer = RandomFuzzer(min_length=5, max_length=20, char_start=32, char_range=95)

    sum_coverage = [0] * trials

    for run in range(runs):
        _, coverage = population_coverage(hundred_inputs(random_fuzzer), cgi_decode)
        assert len(coverage) == trials
        for i in range(trials):
            sum_coverage[i] += coverage[i]

    average_coverage = [sum_coverage[i] / runs for i in range(trials)]

    plt.figure(figsize=(10, 6))
    plt.plot(average_coverage, label="Average Coverage", color="blue")
    plt.title('Average coverage of cgi_decode() with random inputs')
    plt.xlabel('# of inputs')
    plt.ylabel('Lines Covered')
    plt.legend()
    plt.grid(True)
    plt.show()
