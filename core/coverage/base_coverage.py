import sys
import inspect
from typing import List, Set, Tuple, Type, Optional, Callable, Any
from types import FrameType, TracebackType

Location = Tuple[str, int]

class Coverage:
    """Track coverage within a `with` block. Use as:
    ```
    with Coverage() as cov:
        function_to_be_traced()
    c = cov.coverage()
    ```
    """

    def __init__(self) -> None:
        """Constructor"""
        self._trace: List[Location] = []
        self.original_trace_function = None

    def traceit(self, frame: FrameType, event: str, arg: Any) -> Optional[Callable]:
        """Tracing function."""
        if self.original_trace_function is not None:
            self.original_trace_function(frame, event, arg)

        if event == "line":
            function_name = frame.f_code.co_name
            lineno = frame.f_lineno
            if function_name != '__exit__':  # Avoid tracing ourselves
                self._trace.append((function_name, lineno))

        return self.traceit

    def __enter__(self) -> "Coverage":
        """Start tracing."""
        self.original_trace_function = sys.gettrace()
        sys.settrace(self.traceit)
        return self

    def __exit__(self, exc_type: Type, exc_value: BaseException,
                 tb: TracebackType) -> Optional[bool]:
        """Stop tracing."""
        sys.settrace(self.original_trace_function)
        return None

    def trace(self) -> List[Location]:
        """The list of executed lines."""
        return self._trace

    def coverage(self) -> Set[Location]:
        """The set of executed lines."""
        return set(self.trace())

    def function_names(self) -> Set[str]:
        """The set of function names seen."""
        return set(function_name for (function_name, _) in self.coverage())

    def __repr__(self) -> str:
        """Return a string representation showing covered lines."""
        result = ""
        for function_name in self.function_names():
            try:
                fun = eval(function_name)
            except Exception as exc:
                result += f"Skipping {function_name}: {exc}\n"
                continue

            source_lines, start_line_number = inspect.getsourcelines(fun)
            for lineno in range(start_line_number, start_line_number + len(source_lines)):
                prefix = "  " if (function_name, lineno) in self.trace() else "# "
                result += f"{prefix}{lineno:2d}  {source_lines[lineno - start_line_number]}"
        return result
