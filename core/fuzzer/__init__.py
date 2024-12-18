# core/fuzzer/__init__.py
from core.fuzzer.base_fuzzer import Fuzzer
from core.fuzzer.random_fuzzer import RandomFuzzer

__all__ = ["Fuzzer", "RandomFuzzer"]
