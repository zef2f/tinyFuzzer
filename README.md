# tinyFuzzer

**tinyFuzzer** is a project for studying fuzzing based on the book *"The Fuzzing Book"*. It includes fuzzers, runners, targets, and a code coverage system.

# Project Structure

## As of 31.01.2025

### `/artifacts`
Directory for storing fuzzing artifacts.

### `/base-corpus`
Directory for storing the initial corpus for fuzzers.

### `/devel`
A directory for development and testing various concepts from the book. Added to the index to avoid losing potentially useful files.

### `/core`
Contains the main codebase for fuzzers, coverage collectors, and runners.

#### `/core/coverage`
**Directory for coverage collection functionality.**
- `coverage/base_coverage.py`
- `coverage/branch_coverage.py`

Coverage collection is implemented using a function tracing approach. Example:

```python
with Coverage() as cov:
    function_to_be_traced()
c = cov.coverage()
```

Upon entering the `with` block, the function tracing is passed to the `Coverage()` class. When exiting, tracing is restored to the previous function.
Currently, standard coverage collection and branch-coverage simulation are implemented. The branch coverage approach analyzes sequentially executed lines, but its correctness is still under evaluation.

#### `/core/fuzzer`
**Directory for fuzzers.**
- `fuzzer/base_fuzzer.py`
- `fuzzer/random_fuzzer.py`

A **fuzzer** is responsible for generating random input data. It passes this data to a runner, which executes the target program with the generated input.
- `base_fuzzer.py` – a template class for other fuzzers, without actual fuzzing logic.
- `random_fuzzer.py` – generates a random string of a specified length (`str`).

#### `/core/runner`
**Directory containing various runner implementations.**
- `runner/base_runner.py`
- `runner/binary_program_runner.py`
- `runner/print_runner.py`
- `runner/program_runner.py`
- `runner/troff_runner.py`

A **runner** is responsible for executing a target program with given input data. The main function is the constructor, which typically sets the fuzzing target, and the `run()` method, which takes arguments for the target function and executes it (usually via `subprocess`).
- `base_runner.py` – a template class for other runners.
- `print_runner.py` – a dummy runner that simply prints output.
- `program_runner.py` and `binary_program_runner.py` – execute a specified program, but the binary runner converts input data into a binary format.
- `troff_runner.py` – a simulated runner for the `troff` program.

---

### `/fuzzers/`
**Actual fuzzing implementations.**
- `cgi_decode_fuzzer.py`
- `real_troff_fuzzer.py`
- `troff_fuzzer.py`

A **fuzzer** in this context is an infrastructure for testing. It usually combines a runner and a fuzzer.
- `troff_fuzzer.py` – simulates fuzzing of the `troff` utility.
- `real_troff_fuzzer.py` – an actual fuzzer for `troff`.
- `cgi_decode_fuzzer.py` – fuzzes the `cgi_decode` function (located in `/tests/helpers/cgi_decode.py`).
  - Integrated with coverage collection.
  - Generates a graph showing how coverage evolves with each fuzzing iteration.

---

### `/scripts`
**Various utility scripts.**
- `demo_coverage.py`

### `/targets`
**Explicitly declared fuzzing targets.**
- `troff_check.py`

### `/tests`
**Directory containing test cases.**

---

## Running Fuzzers

Run the fuzzers using the following commands:

### Troff Fuzzer
```bash
python3 -m fuzzers.troff_fuzzer
```

### Real Troff Fuzzer (if `troff` is installed on your system)
```bash
python3 -m fuzzers.real_troff_fuzzer
```

## Running Runners

### Troff Runner (manual input testing)
```bash
python3 -m core.runner.troff_runner
```

## Running Tests

Run all tests using:
```bash
python3 -m unittest discover -s tests
```

## Notes
- Use `python3 -m <module>` to run scripts.
- Set the `PYTHONPATH` environment variable for proper fuzzer execution:
  ```bash
  PYTHONPATH=$(pwd) python3 fuzzers/real_troff_fuzzer.py
  ```
