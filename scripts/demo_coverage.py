from core.coverage.base_coverage import Coverage

def function_a():
    print("Function A, Line 1")
    print("Function A, Line 2")
    print("Function A, Line 3")

def function_b():
    print("Function B, Line 1")
    print("Function B, Line 2")

def function_c():
    print("Function C, Line 1")
    print("Function C, Line 2")

def demo_coverage():
    with Coverage() as cov:
        function_a()
        function_b()
        function_c()

    print("Covered lines:")
    print(cov.coverage())

    print("Code with coverage markings:")
    print(cov)

if __name__ == "__main__":
    demo_coverage()
