"""Puzzle for advent of code 2025 day 01."""

from aocd import submit

from advent_of_code.constants import TWENTY_TWENTY_FIVE_INPUT_PATH
from advent_of_code.utils import load_input


def parse_sign(instr: str) -> str:
    return "-" if instr[0] == "L" else ""


def parse_instruction(instr: str) -> int:
    sign = parse_sign(instr)
    result = f"{sign}{instr[1:]}"

    return int(result)


def calc_full_laps(delta: int) -> int:
    return abs(delta) // 100


def calc_partial_laps(pos: int, delta: int) -> int:
    if delta < 0:
        return 1 if pos < abs(delta) else 0
    return 1 if (pos + delta) >= 100 else 0


def solve_part_one(raw_input: list[str]) -> int:
    position = 50
    result = 0

    for instr in raw_input:
        delta = parse_instruction(instr)
        position = (position + delta) % 100

        if position == 0:
            result += 1

    return result


def solve_part_two(raw_input):
    position = 50
    result = 0

    for instr in raw_input:
        delta = parse_instruction(instr)
        full_laps = calc_full_laps(delta)
        partial_laps = calc_partial_laps(position, delta)

        result += full_laps + partial_laps

    return result


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_FIVE_INPUT_PATH.joinpath("day01.txt")
    puzzle_input = load_input(puzzle_input_path)
    solution_part_one = solve_part_one(puzzle_input)
    solution_part_two = solve_part_two(puzzle_input)
    print(
        "Advent of code 2025 day 01:",
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )
    submit(
        solution_part_one,
        part="a",
        year=2025,
        day=1,
    )
    submit(
        solution_part_two,
        part="b",
        year=2025,
        day=1,
    )


if __name__ == "__main__":
    solve_puzzle()
