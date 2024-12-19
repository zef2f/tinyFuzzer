# tinyFuzzer

**tinyFuzzer** is a project for studying fuzzing based on the book *"The Fuzzing Book"*. It includes fuzzers, runners, targets, and a code coverage system.

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
