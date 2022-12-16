"""Puzzle for advent of code 2022 day 13."""

import ast
from typing import Union

from advent_of_code.constants import TWENTY_TWENTY_TWO_INPUT_PATH
from advent_of_code.utils import load_input


def parse_input(raw_input: list[str]) -> list[list]:
    parsed_input = []
    pair = []

    for line in raw_input:
        if len(line) > 0:
            parsed_line = ast.literal_eval(line)
            pair.append(parsed_line)
        else:
            parsed_input.append(pair)
            pair = []

    # make sure last pair is parsed despite missing new line
    if pair:
        parsed_input.append(pair)

    return parsed_input


def compare_integers(left: int, right: int) -> Union[bool, None]:
    if left < right:
        return True
    elif left > right:
        return False
    else:
        return


def compare_lists(left: list, right: list) -> Union[bool, None]:
    for left_value, right_value in zip(left, right):

        is_ordered = is_correct_order(left_value, right_value)
        if is_ordered is not None:
            return is_ordered

    if len(left) <= len(right):
        return True
    elif len(left) > len(right):
        return False
    else:
        return


def is_correct_order(left: list, right: list) -> Union[bool, None]:
    if isinstance(left, int) and isinstance(right, int):
        return compare_integers(left, right)
    elif isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    elif isinstance(left, int) and isinstance(right, list):
        return is_correct_order([left], right)
    else:
        return is_correct_order(left, [right])


def solve_part_one(raw_input: list[str]) -> int:
    correct_order = 0

    parsed_input = parse_input(raw_input)

    for index, pair in enumerate(parsed_input):
        if is_correct_order(left=pair[0], right=pair[1]):
            correct_order += index + 1

    return correct_order


def solve_part_two(raw_input: list[str]):
    pass


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_TWO_INPUT_PATH.joinpath("day13")
    puzzle_input = load_input(puzzle_input_path)
    solution_part_one = solve_part_one(puzzle_input)
    solution_part_two = None
    print(
        "Advent of code 2022 day 13:",
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )


if __name__ == "__main__":
    solve_puzzle()
