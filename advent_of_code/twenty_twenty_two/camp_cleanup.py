"""Puzzle for advent of code 2022 day 04."""

from typing import Tuple

from advent_of_code.constants import TWENTY_TWENTY_TWO_PATH
from advent_of_code.utils import load_input


def split_assignment(assignment: str) -> list[list[str]]:
    return [section.split("-") for section in assignment.split(",")]


def transform_sections(sections: list[list[str]]) -> Tuple[int, int, int, int]:
    return (
        int(sections[0][0]),
        int(sections[0][1]),
        int(sections[1][0]),
        int(sections[1][1]),
    )


def is_fully_contained(
    start_first_section: int,
    stop_first_section: int,
    start_second_section: int,
    stop_second_section: int,
) -> bool:
    if (
        start_first_section >= start_second_section
        and stop_first_section <= stop_second_section
    ) | (
        start_second_section >= start_first_section
        and stop_second_section <= stop_first_section
    ):
        return True

    return False


def calculate_fully_contained_assignments(assignments: list[str]) -> int:
    fully_contained = 0

    for assignment in assignments:
        sections = split_assignment(assignment)
        (
            start_first_section,
            stop_first_section,
            start_second_section,
            stop_second_section,
        ) = transform_sections(sections)
        if is_fully_contained(
            start_first_section,
            stop_first_section,
            start_second_section,
            stop_second_section,
        ):
            fully_contained += 1

    return fully_contained


def is_overlapping(
    start_first_section: int,
    stop_first_section: int,
    start_second_section: int,
    stop_second_section: int,
) -> bool:
    return (start_first_section <= stop_second_section) & (
        stop_first_section >= start_second_section
    )


def calculate_overlapping_assignments(assignments: list[str]) -> int:
    overlapping = 0

    for assignment in assignments:
        sections = split_assignment(assignment)
        (
            start_first_section,
            stop_first_section,
            start_second_section,
            stop_second_section,
        ) = transform_sections(sections)
        if is_overlapping(
            start_first_section,
            stop_first_section,
            start_second_section,
            stop_second_section,
        ):
            overlapping += 1

    return overlapping


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_TWO_PATH.joinpath("input_camp_cleanup")
    puzzle_input = load_input(puzzle_input_path)
    solution_part_one = calculate_fully_contained_assignments(puzzle_input)
    solution_part_two = calculate_overlapping_assignments(puzzle_input)
    print(
        "Camp cleanup",
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )


if __name__ == "__main__":
    solve_puzzle()
