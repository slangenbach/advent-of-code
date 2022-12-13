"""Puzzle for advent of code 2022 day 06."""

from functools import partial
from typing import Union

from advent_of_code.constants import TWENTY_TWENTY_TWO_INPUT_PATH
from advent_of_code.utils import load_input


def has_duplicate(chars: list[str]) -> bool:
    if len(chars) > len(set(chars)):
        return True
    return False


def find_marker(buffer: str, distinct_chars: int) -> Union[int, None]:
    chars = []

    for index, char in enumerate(buffer):
        if len(chars) < distinct_chars:
            chars.append(char)
            continue
        if has_duplicate(chars):
            chars.pop(0)
            chars.append(char)
            continue
        else:
            return index


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_TWO_INPUT_PATH.joinpath("day06")
    puzzle_input = load_input(puzzle_input_path)
    find_package_marker = partial(find_marker, distinct_chars=4)
    find_message_marker = partial(find_marker, distinct_chars=14)
    solution_part_one = find_package_marker(puzzle_input[0])
    solution_part_two = find_message_marker(puzzle_input[0])
    print(
        "Advent of code 2022 day 06:",
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )


if __name__ == "__main__":
    solve_puzzle()
