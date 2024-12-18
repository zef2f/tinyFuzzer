# targets/troff_check.py
import string

def no_backslash_d(inp: str) -> bool:
    pattern = "\\D"
    index = inp.find(pattern)

    if index < 0 or index + len(pattern) >= len(inp):
        return True

    c = inp[index + len(pattern)]
    assert c in string.printable
    return True

def no_8bit(inp: str) -> bool:
    for i in range(len(inp) - 1):
        assert ord(inp[i]) <= 127 or inp[i + 1] != '\n'
    return True

def no_dot(inp: str) -> bool:
    assert inp != ".\n"
    return True
