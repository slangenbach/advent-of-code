"""Puzzle for advent of code 2025 day 2."""

from collections.abc import Callable, Generator

from aocd import submit

from advent_of_code.constants import TWENTY_TWENTY_FIVE_INPUT_PATH
from advent_of_code.logger import get_logger
from advent_of_code.utils import load_input

logger = get_logger(__name__, level="INFO")


def parse_input(raw_input: list[str]) -> list[str]:
    return raw_input[0].strip().split(",")


def parse_range(id_range: str) -> tuple[int, int]:
    start, stop = id_range.split("-")

    return int(start), int(stop)


def generate_ids(id_range: str) -> Generator[int]:
    start, stop = parse_range(id_range)

    yield from range(start, stop + 1)


def is_invalid_id(id: str) -> bool:
    # invalid IDs must have same length
    if len(id) % 2 != 0:
        return False
    else:
        midpoint = len(id) // 2
        first, second = id[:midpoint], id[midpoint:]
        if first == second:
            return True

        return False


def is_also_invalid_id(id: str) -> bool:
    n = len(id)
    windows = [w for w in range(1, (n // 2) + 1)]  # only consider integer windows
    logger.debug("Processing ID '%s' with length: %s", id, n)
    logger.debug("Valid windows are: %s", windows)

    for window in windows:
        logger.debug("Checking window: %s", window)
        # skip windows not fitting the length of the ID
        if n % window != 0:
            continue

        ref = id[0:window]
        logger.debug("Reference: %s", ref)

        for pos in range(window, n, window):
            curr_window = id[pos : pos + window]
            logger.debug("Current window: %s", curr_window)
            if curr_window != ref:
                break
        else:
            return True

    return False


def _solve_puzzle(raw_input: list[str], check_fn: Callable) -> int:
    result = 0
    parsed_input = parse_input(raw_input)

    for _input in parsed_input:
        for _id in generate_ids(_input):
            if check_fn(str(_id)):
                logger.debug("ID %s is invalid", _id)
                result += int(_id)

    return result


def solve_part_one(raw_input: list[str]) -> int:
    result = _solve_puzzle(raw_input, check_fn=is_invalid_id)

    return result


def solve_part_two(raw_input: list[str]) -> int:
    result = _solve_puzzle(raw_input, check_fn=is_also_invalid_id)

    return result


def solve_puzzle():
    logger.info("Advent of code 2025 day 2")
    puzzle_input_path = TWENTY_TWENTY_FIVE_INPUT_PATH.joinpath("day02.txt")
    puzzle_input = load_input(puzzle_input_path)

    logger.info("Solving part one")
    solution_part_one = solve_part_one(puzzle_input)
    logger.info("Solution for part one: %s", solution_part_one)

    logger.info("Solving part two")
    solution_part_two = solve_part_two(puzzle_input)
    logger.info("Solution for part two: %s", solution_part_two)

    logger.info("Submitting solutions")
    submit(solution_part_one, part="a", year=2025, day=2)
    submit(solution_part_two, part="b", year=2025, day=2)


if __name__ == "__main__":
    solve_puzzle()
