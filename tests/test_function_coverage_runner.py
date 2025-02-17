import pytest
from core.runner.function_coverage_runner import FunctionCoverageRunner
from core.runner.base_runner import Runner
from core.coverage.base_coverage import Coverage

def test_function_coverage_runner(mocker):
    """Проверка работы FunctionCoverageRunner"""

    # Функция, которую будем исполнять
    def sample_function(inp: str) -> str:
        return inp.upper()

    # Подмена Coverage для теста
    mock_coverage = mocker.patch.object(Coverage, "__enter__", return_value=mocker.Mock())
    mock_coverage.return_value.coverage.return_value = {"dummy_location"}

    runner = FunctionCoverageRunner(sample_function)

    # Проверяем успешное выполнение
    result, outcome = runner.run("test")
    assert result == "TEST"
    assert outcome == Runner.PASS

    # Проверяем, что coverage корректно собирается
    assert runner.coverage() == {"dummy_location"}

    # Проверяем обработку исключений
    def faulty_function(inp: str):
        raise ValueError("Boom!")

    faulty_runner = FunctionCoverageRunner(faulty_function)

    with pytest.raises(ValueError, match="Boom!"):
        faulty_runner.run("test")

    # Проверяем, что coverage все равно собирается
    assert faulty_runner.coverage() == {"dummy_location"}

