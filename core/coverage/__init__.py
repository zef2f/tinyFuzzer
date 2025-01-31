# core/coverage/__init__.py
from core.coverage.base_coverage import Coverage
from core.coverage.branch_coverage import BranchCoverage
"""
Coverage tracking module.

This module handles code coverage tracking for fuzzing.
"""
__all__ = ["Coverage", "BranchCoverage"]
