# tests/test_runner.py
import unittest
from core.runner import Runner, PrintRunner

class TestRunner(unittest.TestCase):
    def test_base_runner(self):
        runner = Runner()
        result = runner.run("test")
        self.assertEqual(result[0], "test")
        self.assertEqual(result[1], Runner.UNRESOLVED)

    def test_print_runner(self):
        pr = PrintRunner()
        result = pr.run("hello")
        self.assertEqual(result[0], "hello")
        self.assertEqual(result[1], Runner.UNRESOLVED)

if __name__ == "__main__":
    unittest.main()
