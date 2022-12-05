"""Utility functions."""

from pathlib import Path


def load_input(input_path: Path) -> list[str]:
    """Load input for puzzle.

    Args:
        input_path (Path): Path to input file.

    Returns:
        list[str]: Input as text split by linebreaks
    """

    return input_path.read_text().split("\n")
