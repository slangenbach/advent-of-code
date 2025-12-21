"""Puzzle for advent of code 2025 day 5."""

from dataclasses import dataclass

from aocd import submit

from advent_of_code.constants import TWENTY_TWENTY_FIVE_INPUT_PATH
from advent_of_code.logger import get_logger
from advent_of_code.utils import load_input, timer

logger = get_logger(__name__, level="INFO")


@dataclass
class ParsedRange:  # noqa: D101
    start: int
    stop: int


@dataclass
class ParsedInput:  # noqa: D101
    fresh_id_ranges: list[ParsedRange]
    available_ids: list[int]


def _parse_range(id_range: str) -> ParsedRange:
    start, stop = map(int, id_range.split("-"))

    return ParsedRange(start, stop)


def parse_input(raw_input: list[str]) -> ParsedInput:
    fresh_id_ranges = []
    available_ids = []

    for _id in raw_input:
        if "-" in _id:
            parsed_range = _parse_range(_id)
            fresh_id_ranges.append(parsed_range)
        elif _id == "":
            continue
        else:
            available_ids.append(int(_id))

    return ParsedInput(fresh_id_ranges, available_ids)


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []
    merged.append(ranges[0])

    for _range in sorted(ranges[1:]):
        start, end = _range
        last_start, last_end = merged[-1]

        # check if ranges overlap
        if start <= last_end:
            # update last merged range
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append(_range)

    return merged


@timer
def solve_part_one(parsed_input: ParsedInput) -> int:
    result = 0

    for _id in parsed_input.available_ids:
        for id_range in parsed_input.fresh_id_ranges:
            if id_range.start <= _id <= id_range.stop:
                result += 1
                break

    return result


@timer
def solve_part_two(parsed_input: ParsedInput) -> int:
    ranges = [(val.start, val.stop) for val in parsed_input.fresh_id_ranges]
    merged_ranges = merge_ranges(ranges)

    result = 0

    for _range in merged_ranges:
        result += _range[1] - _range[0] + 1

    return result


def solve_puzzle():
    logger.info("Advent of code 2025 day 5")
    puzzle_input_path = TWENTY_TWENTY_FIVE_INPUT_PATH.joinpath("day05.txt")
    puzzle_input = load_input(puzzle_input_path)
    parsed_input = parse_input(puzzle_input)

    logger.info("Solving part one")
    solution_part_one = solve_part_one(parsed_input)
    logger.info("Solution for part one: %s", solution_part_one)

    logger.info("Solving part two")
    solution_part_two = solve_part_two(parsed_input)
    logger.info("Solution for part two: %s", solution_part_two)

    logger.info("Submitting solutions")
    submit(solution_part_one, part="a", year=2025, day=5)
    submit(solution_part_two, part="b", year=2025, day=5)


if __name__ == "__main__":
    solve_puzzle()
