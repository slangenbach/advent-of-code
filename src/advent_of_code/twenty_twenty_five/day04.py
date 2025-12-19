"""Puzzle for advent of code 2025 day 4."""

from aocd import submit

from advent_of_code.constants import TWENTY_TWENTY_FIVE_INPUT_PATH
from advent_of_code.logger import get_logger
from advent_of_code.utils import load_input, timer

logger = get_logger(__name__, level="INFO")

Grid = list[list[str]]


def parse_input(raw_input: list[str]) -> Grid:
    return [list(line) for line in raw_input]


def is_roll(row_idx: int, col_idx: int, grid: Grid) -> bool:
    return grid[row_idx][col_idx] == "@"


def is_valid_position(row_idx: int, col_idx: int, grid: Grid, num_rows: int, num_cols: int) -> bool:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    count = 0

    for direction in directions:
        new_row = row_idx + direction[0]
        new_col = col_idx + direction[1]
        # only check positions within the grid
        if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
            if is_roll(row_idx=new_row, col_idx=new_col, grid=grid):
                count += 1
                if count > 3:
                    return False

    return True


def remove_rolls(positions: list[tuple[int, int]], grid: Grid) -> None:
    for pos in positions:
        grid[pos[0]][pos[1]] = "."


@timer
def solve_part_one(grid: Grid) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    result = 0

    for row_idx in range(num_rows):
        for col_idx in range(num_cols):
            if is_roll(row_idx, col_idx, grid):
                if is_valid_position(
                    row_idx, col_idx, grid=grid, num_rows=num_rows, num_cols=num_cols
                ):
                    result += 1

    return result


@timer
def solve_part_two(grid: Grid) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])
    result = 0

    while True:
        positions_to_remove = []
        for row_idx in range(num_rows):
            for col_idx in range(num_cols):
                if is_roll(row_idx, col_idx, grid) and is_valid_position(
                    row_idx, col_idx, grid=grid, num_rows=num_rows, num_cols=num_cols
                ):
                    positions_to_remove.append((row_idx, col_idx))
        if not positions_to_remove:
            break
        remove_rolls(positions_to_remove, grid)
        result += len(positions_to_remove)

    return result


def solve_puzzle():
    logger.info("Advent of code 2025 day 4")
    puzzle_input_path = TWENTY_TWENTY_FIVE_INPUT_PATH.joinpath("day04.txt")
    puzzle_input = load_input(puzzle_input_path)
    parsed_input = parse_input(puzzle_input)

    logger.info("Solving part one")
    solution_part_one = solve_part_one(parsed_input)
    logger.info("Solution for part one: %s", solution_part_one)

    logger.info("Solving part two")
    solution_part_two = solve_part_two(parsed_input)
    logger.info("Solution for part two: %s", solution_part_two)

    logger.info("Submitting solutions")
    submit(solution_part_one, part="a", year=2025, day=4)
    submit(solution_part_two, part="b", year=2025, day=4)


if __name__ == "__main__":
    solve_puzzle()
