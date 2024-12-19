# tests/test_fuzzer.py
import unittest
from core.coverage import Coverage
from helper.cgi_decode import cgi_decode

class TestCoverage(unittest.TestCase):
    def test_cov(self):
        before = 0
        middle = 0
        after = 0

        cov2_count = 0
        with Coverage() as cov:
            before = len(cov.coverage())
            cgi_decode("a+b")
            cgi_decode("asd")
            middle = len(cov.coverage())
            cgi_decode("%20")
            with Coverage() as cov2:
                cgi_decode("assdfdsfsdff")
        after = len(cov.coverage())
        cov2_count = len(cov2.coverage())
        self.assertTrue(before < cov2_count < middle < after)


if __name__ == "__main__":
    unittest.main()

