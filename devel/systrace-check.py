import sys
import inspect


coverage = []
def trace_calls(frame, event, arg):
    if event == 'call':
        print(f"function call {frame.f_code.co_name} in line {frame.f_lineno}")
    elif event == 'return':
        print(f"function {frame.f_code.co_name} return {arg}")
    elif event == 'line':
        global coverage
        coverage.append(frame.f_lineno)
        print(f"run line {frame.f_lineno} in {frame.f_code.co_name} function")
    else:
        print(f"unknown event {event}. for debug: func-{frame.f_code.co_name}, line-{frame.f_lineno} ")
    return trace_calls

sys.settrace(trace_calls)

def example_function(x):
    y = x * 2
    return y + 3

result = example_function(5)

sys.settrace(None)

decode_lines = inspect.getsource(example_function)

decode_split = [""] + decode_lines.splitlines()

print(type(decode_split), "\n", decode_split)

covered_lines = set(coverage)

print("coverage = ", coverage)

shift = 20

for lineno in range(1, len(decode_split)):
    if (lineno + shift) not in covered_lines:
        print("# ", end="")
    else:
        print("  ", end="")
    print("%2d  " % lineno, end="")
    print(decode_split[lineno])
