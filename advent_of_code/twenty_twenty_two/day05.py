"""Puzzle for advent of code 2022 day 05."""

from advent_of_code.constants import TWENTY_TWENTY_TWO_INPUT_PATH
from advent_of_code.utils import load_input


def parse_input(raw_input):
    raise NotImplementedError()


def solve_part_one(raw_input):
    raise NotImplementedError()


def solve_part_two(raw_input):
    raise NotImplementedError()


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_TWO_INPUT_PATH.joinpath("day05")
    puzzle_input = load_input(puzzle_input_path)
    solution_part_one = solve_part_one(puzzle_input)
    solution_part_two = solve_part_two(puzzle_input)
    print(
        "Advent of code 2022 day 05:",
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )


if __name__ == "__main__":
    solve_puzzle()
