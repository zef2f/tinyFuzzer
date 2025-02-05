import sys
import inspect
from typing import List, Set, Tuple, Type, Optional, Callable, Any
from types import FrameType, TracebackType
from core.coverage.base_coverage import Coverage

Location = Tuple[str, int]

class BranchCoverage(Coverage):
    """Track branch coverage (imitation) within a `with` block. Use as:
    ```
    with BranchCoverage() as cov:
        function_to_be_traced()
    c = cov.coverage()
    ```
    """
    def coverage(self):
        """The set of executed line pairs"""
        coverage = set()
        past_line = None
        for line in self.trace():
            if past_line is not None:
                coverage.add((past_line, line))
            past_line = line

        return coverage
    
    def function_names(self) -> Set[str]:
        """The set of function names seen."""
        # Extract function names from both elements of each pair in coverage
        return set(
            function_name
            for pair in self.coverage()
            for function_name, _ in pair
    
        )

    def population_branch_coverage(population, function):
        cumulative_coverage = []
        all_coverage = set()

        for s in population:
            with BranchCoverage() as cov:
                try:
                    function(s)
                except Exception:
                    pass
            all_coverage |= cov.coverage()
            cumulative_coverage.append(len(all_coverage))
        
        return all_coverage, cumulative_coverage

    def __repr__(self) -> str:
        """Return a string representation showing covered lines."""
        result = ""
        for function_name in self.function_names():
            try:
                # Get the function object by its name
                fun = eval(function_name)
            except Exception as exc:
                result += f"Skipping {function_name}: {exc}\n"
                continue

            # Get the source code and starting line number of the function
            source_lines, start_line_number = inspect.getsourcelines(fun)

            for lineno in range(start_line_number, start_line_number + len(source_lines)):
                # Check if the line is part of any pair in coverage
                is_covered = any(
                    (function_name, lineno) == pair[0] for pair in self.coverage()
                )
                prefix = "  " if is_covered else "# "
                result += f"{prefix}{lineno:2d}  {source_lines[lineno - start_line_number]}"
        return result
