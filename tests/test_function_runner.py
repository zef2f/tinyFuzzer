import pytest
from core.runner.function_runner import FunctionRunner
from core.runner.base_runner import Runner

def test_function_runner():
    """Проверка работы FunctionRunner"""

    # Простая функция сложения
    def add_prefix(inp: str) -> str:
        return "prefix_" + inp

    runner = FunctionRunner(add_prefix)

    # Проверяем успешный запуск
    result, outcome = runner.run("test")
    assert result == "prefix_test"
    assert outcome == Runner.PASS

    # Проверяем обработку исключений
    def faulty_function(inp: str):
        raise ValueError("Error!")

    faulty_runner = FunctionRunner(faulty_function)
    result, outcome = faulty_runner.run("test")
    assert result is None
    assert outcome == Runner.FAIL

