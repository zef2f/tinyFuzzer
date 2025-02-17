import pytest
from core.fuzzer.mutation_coverage_fuzzer import MutationCoverageFuzzer
from core.runner.function_coverage_runner import FunctionCoverageRunner
from core.runner.base_runner import Runner
from unittest.mock import Mock

def test_mutation_coverage_fuzzer():
    """Проверка работы MutationCoverageFuzzer"""

    # Поддельный раннер с фиктивным покрытием
    runner = Mock(spec=FunctionCoverageRunner)
    runner.coverage.return_value = {"mock_location"}
    runner.run.return_value = ("mock_result", Runner.PASS)

    # Создаем фаззер с сидом
    fuzzer = MutationCoverageFuzzer(seed=["test_input"])
    
    # Проверяем, что фуззер инициализируется с сидом
    assert fuzzer.population == ["test_input"]
    
    # Запускаем фуззер
    fuzzer.run(runner, "test_input")

    # Проверяем, что новое покрытие сохраняется
    assert "mock_location" in fuzzer.coverages_seen
    assert "test_input" in fuzzer.population

    # Проверяем, что фаззер не добавляет повторное покрытие
    initial_size = len(fuzzer.coverages_seen)
    fuzzer.run(runner, "test_input")
    assert len(fuzzer.coverages_seen) == initial_size  # Размер не изменился

