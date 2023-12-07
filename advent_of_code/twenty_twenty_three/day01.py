"""Puzzle for advent of code 2023 day 01."""

import re
from typing import Match

from advent_of_code.constants import TWENTY_TWENTY_THREE_INPUT_PATH
from advent_of_code.utils import load_input


def parse_words_as_digits(match: Match) -> str:
    WORD_DIGIT_MAP = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    return WORD_DIGIT_MAP[match.group(0)]


def parse_input(raw_input):
    pattern = r"(one|two|three|four|five|six|seven|eight|nine)"

    return [re.sub(pattern, parse_words_as_digits, line) for line in raw_input]


def solve_part_one(raw_input):
    calibration_sum = 0

    for line in raw_input:
        digits = []

        for char in line:
            if char.isdigit():
                if len(digits) < 2:  # noqa: PLR2004
                    digits.append(char)
                else:
                    digits[1] = char

        if len(digits) != 2:  # noqa: PLR2004
            digits.append(digits[0])

        calibration_sum += int("".join(digits))

    return calibration_sum


def solve_part_two(raw_input):
    parsed_input = parse_input(raw_input)

    return solve_part_one(parsed_input)


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_THREE_INPUT_PATH.joinpath("day01")
    puzzle_input = load_input(puzzle_input_path)
    solution_part_one = solve_part_one(puzzle_input)
    solution_part_two = solve_part_two(puzzle_input)
    print(
        "Advent of code 2023 day 1:",
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )


if __name__ == "__main__":
    solve_puzzle()
