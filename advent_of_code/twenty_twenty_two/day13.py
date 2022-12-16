"""Puzzle for advent of code 2022 day 13."""

import ast
import math
from functools import cmp_to_key
from typing import Union

from advent_of_code.constants import TWENTY_TWENTY_TWO_INPUT_PATH
from advent_of_code.utils import load_input

DIVIDER_PACKETS = [[[2]], [[6]]]


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

        # recursively compare items of current pair
        is_ordered = is_correct_order(left_value, right_value)
        if is_ordered is not None:
            return is_ordered

    if len(left) < len(right):
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

    for index, pair in enumerate(parsed_input, start=1):
        if is_correct_order(left=pair[0], right=pair[1]):
            correct_order += index

    return correct_order


def parse_input_part_two(raw_input: list[str]) -> list[list]:
    parsed_input = [
        ast.literal_eval(line) for line in raw_input if line.startswith("[")
    ]
    parsed_input.extend(DIVIDER_PACKETS)

    return parsed_input


def order_input(parsed_input: list[list]) -> list[list]:
    def comparator(a: list, b: list) -> int:
        if is_correct_order(a, b):
            return 1
        elif not is_correct_order(a, b):
            return -1
        else:
            return 0

    return sorted(parsed_input, key=cmp_to_key(comparator), reverse=True)


def get_divider_packet_indices(ordered_input: list) -> list[int]:
    return [
        ordered_input.index(divider_packet) + 1 for divider_packet in DIVIDER_PACKETS
    ]


def solve_part_two(raw_input: list[str]) -> int:
    parsed_input = parse_input_part_two(raw_input)
    ordered_input = order_input(parsed_input)
    divider_packet_indices = get_divider_packet_indices(ordered_input)

    return math.prod(divider_packet_indices)


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_TWO_INPUT_PATH.joinpath("day13")
    puzzle_input = load_input(puzzle_input_path)
    solution_part_one = solve_part_one(puzzle_input)
    solution_part_two = solve_part_two(puzzle_input)
    print(
        "Advent of code 2022 day 13:",
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )


if __name__ == "__main__":
    solve_puzzle()
