"""Puzzle for advent of code 2025 day 3."""

from aocd import submit

from advent_of_code.constants import TWENTY_TWENTY_FIVE_INPUT_PATH
from advent_of_code.logger import get_logger
from advent_of_code.utils import load_input, timer

logger = get_logger(__name__, level="INFO")


def get_max_joltage(bank: str) -> int:
    _max = 0
    temp_max = 0

    for i in range(0, len(bank) - 1):
        curr_max = 0
        for j in range(i + 1, len(bank)):
            second_battery = int(bank[j])
            if second_battery > curr_max:
                curr_max = second_battery
        first_battery = bank[i]
        temp_max = int(f"{first_battery}{curr_max}")

        if temp_max > _max:
            _max = temp_max

    return _max


def _get_suffix_max(bank: str) -> list[int]:
    n = len(bank)
    suffix_max = [0] * n
    suffix_max[-1] = int(bank[-1])

    # Get indices for bank in reverse order, starting from second last index
    for idx in range(n - 2, -1, -1):
        # Max for current index, is max of current val and previous max
        suffix_max[idx] = max(int(bank[idx]), suffix_max[idx + 1])

    return suffix_max


def get_max_joltage_optimized(bank: str) -> int:
    _max = 0
    temp_max = 0
    suffix_max = _get_suffix_max(bank)

    for idx, battery in enumerate(bank[:-1]):
        temp_max = int(f"{battery}{suffix_max[idx + 1]}")
        if temp_max > _max:
            _max = temp_max

    return _max


@timer
def solve_part_one(raw_input: list[str]):
    result = 0

    for bank in raw_input:
        largest = get_max_joltage_optimized(bank)
        result += largest

    return result


def solve_part_two(raw_input: list[str]):
    raise NotImplementedError()


def solve_puzzle():
    logger.info("Advent of code 2025 day 3")
    puzzle_input_path = TWENTY_TWENTY_FIVE_INPUT_PATH.joinpath("day03.txt")
    puzzle_input = load_input(puzzle_input_path)

    logger.info("Solving part one")
    solution_part_one = solve_part_one(puzzle_input)
    logger.info("Solution for part one: %s", solution_part_one)

    logger.info("Solving part two")
    solution_part_two = solve_part_two(puzzle_input)
    logger.info("Solution for part two: %s", solution_part_two)

    logger.info("Submitting solutions")
    submit(solution_part_one, part="a", year=2025, day=3)
    submit(solution_part_two, part="b", year=2025, day=3)


if __name__ == "__main__":
    solve_puzzle()
