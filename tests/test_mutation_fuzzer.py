import unittest
import random
from core.fuzzer.mutation_fuzzer import MutationFuzzer

class TestMutationFuzzer(unittest.TestCase):
    def setUp(self):
        """Создает экземпляр MutationFuzzer перед каждым тестом"""
        random.seed(42)  # Фиксируем случайность для стабильных тестов
        self.seed = ["http://www.google.com/search?q=fuzzing"]
        self.mutation_fuzzer = MutationFuzzer(seed=self.seed)

    def test_fuzz_length(self):
        """Проверяет, что длина выходных данных находится в разумных пределах"""
        fuzz_input = self.mutation_fuzzer.fuzz()
        self.assertGreaterEqual(len(fuzz_input), 0)
        self.assertLessEqual(len(fuzz_input), 100)

    def test_mutation_changes_string(self):
        """Проверяет, что мутация изменяет строку"""
        original = self.seed[0]
        mutated = self.mutation_fuzzer.mutate(original)
        self.assertNotEqual(original, mutated, "Мутация должна изменять строку")

    def test_reset(self):
        """Проверяет, что `reset()` сбрасывает состояние фаззера"""
        self.mutation_fuzzer.fuzz()  # Генерируем хотя бы один новый инпут
        self.mutation_fuzzer.reset()  # Сбрасываем состояние
        self.assertEqual(self.mutation_fuzzer.population, self.seed, "После reset() population должен совпадать с seed")

    def test_fuzz_uses_seed_then_mutates(self):
        """Проверяет, что fuzz() сначала использует seed, а потом начинает мутации"""
        first_fuzz = self.mutation_fuzzer.fuzz()
        self.assertIn(first_fuzz, self.seed, "Первый вызов fuzz() должен вернуть сид")

        second_fuzz = self.mutation_fuzzer.fuzz()
        self.assertNotIn(second_fuzz, self.seed, "Второй вызов fuzz() должен уже мутировать данные")

if __name__ == "__main__":
    unittest.main()
