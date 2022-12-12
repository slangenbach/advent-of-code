"""Puzzle for advent of code 2022 day 08."""

import math
from pathlib import Path
from typing import Tuple

from advent_of_code.constants import TWENTY_TWENTY_TWO_INPUT_PATH

Grid = list[list[int]]
SightLines = Tuple[list[int], list[int], list[int], list[int]]


def load_input(input_path: Path) -> Grid:
    raw_input = input_path.read_text().splitlines()
    grid = [list(row) for row in raw_input]
    return [[int(height) for height in row] for row in grid]


def get_sight_lines(x: int, y: int, grid: Grid) -> SightLines:
    left = grid[y][:x][::-1]
    up = [row[x] for row in grid[:y]][::-1]
    right = grid[y][x + 1 :]
    down = [row[x] for row in grid[y + 1 :]]

    return left, up, right, down


def is_visible(height: int, sight_lines: SightLines) -> bool:
    return any([height > max(line) if line else True for line in sight_lines])


def calculate_visible_trees(grid: Grid) -> int:
    visible_trees = 0

    for row in range(0, len(grid[0])):
        for col in range(0, len(grid)):
            height = grid[col][row]
            sight_lines = get_sight_lines(row, col, grid)

            if is_visible(height, sight_lines):
                visible_trees += 1

    return visible_trees


def calculate_scenic_score(height: int, sight_lines: SightLines) -> int:
    visible_trees = []

    for line in sight_lines:
        if line:
            for index, tree in enumerate(line):
                if height <= tree:
                    break
            visible_trees.append(index + 1)  # pyright: ignore

    return math.prod(visible_trees)


def calculate_max_scenic_score(grid: Grid) -> int:
    max_scenic_score = 0

    # do not consider trees at edge of grid
    for row in range(1, len(grid[0]) - 1):
        for col in range(1, len(grid) - 1):
            height = grid[col][row]
            sight_lines = get_sight_lines(row, col, grid)
            scenic_score = calculate_scenic_score(height, sight_lines)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


def solve_puzzle():
    puzzle_input_path = TWENTY_TWENTY_TWO_INPUT_PATH.joinpath("day08")
    puzzle_input = load_input(puzzle_input_path)
    solution_part_one = calculate_visible_trees(puzzle_input)
    solution_part_two = calculate_max_scenic_score(puzzle_input)
    print(
        f"Solution for part one: {solution_part_one}",
        f"Solution for part two: {solution_part_two}",
        sep="\n",
    )


if __name__ == "__main__":
    solve_puzzle()
