"""Utility functions."""

import time
from collections.abc import Callable
from functools import wraps
from pathlib import Path

from .logger import get_logger

logger = get_logger(name=__name__)


def load_input(input_path: Path) -> list[str]:
    """Load input for puzzle.

    Args:
        input_path (Path): Path to input file.

    Returns:
        list[str]: Input as text split by linebreaks
    """
    return input_path.read_text().splitlines()


def timer(func: Callable):
    """Decorator to track execution of functions."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        logger.info("Execution of '%s' took: %.4f seconds", func.__name__, end - start)  # type: ignore[unresolved-attribute]

        return result

    return wrapper
