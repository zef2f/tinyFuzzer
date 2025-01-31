# WARNING: This script may consume a significant amount of RAM.
# Ensure you have enough available memory before running it.
import matplotlib.pyplot as plt
from typing import Set, Tuple
from core.coverage import BranchCoverage  # Замените на ваш путь импорта
from devel.helper.cgi_decode import cgi_decode  # Замените на ваш путь импорта
from core.fuzzer.random_fuzzer import RandomFuzzer  # Замените на ваш путь импорта

Location = Tuple[str, int]

if __name__ == "__main__":
    # Создаем фаззер с заданными параметрами
    random_fuzzer = RandomFuzzer(min_length=5, max_length=20, char_start=32, char_range=95)
    total_iterations = 10 # Количество итераций фаззинга
    coverage_progress = []

    # Инициализируем общий coverage для всех итераций
    with BranchCoverage() as overall_coverage:
        for iteration in range(total_iterations):
            # Отдельный coverage для текущей итерации
            with BranchCoverage() as iteration_coverage:
                try:
                    # Генерируем входные данные и передаем их в целевую функцию
                    fuzz_input = random_fuzzer.fuzz()
                    cgi_decode(fuzz_input)
                except Exception as e:
                    pass  # Игнорируем исключения

            print(overall_coverage.coverage_cgi_decode())

            # Фильтруем покрытие только для функции `cgi_decode`
            filtered_coverage: Set[Tuple[Location, Location]] = {
                pair for pair in overall_coverage.coverage_cgi_decode() if pair[0][0] == 'cgi_decode'
            }

            # Вывод текущего покрытия в консоль
            print(f"Iteration {iteration + 1}: {len(filtered_coverage)} branches covered")

            # Добавляем размер покрытия в список прогресса
            coverage_progress.append(len(filtered_coverage))

    # Визуализируем рост покрытия
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, total_iterations + 1), coverage_progress, label="Coverage Progress", color="blue")
    plt.xlabel("Iteration")
    plt.ylabel("Branch Coverage Count")
    plt.title("Branch Coverage Growth Over Fuzzing Iterations")
    plt.legend()
    plt.grid(True)
    plt.show()
