# fuzzers/__init__.py
from fuzzers.troff_fuzzer import main as run_troff_fuzzer
from fuzzers.real_troff_fuzzer import main as run_real_troff_fuzzer

__all__ = ["run_troff_fuzzer", "run_real_troff_fuzzer"]
