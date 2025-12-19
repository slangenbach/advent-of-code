import pytest

from advent_of_code.constants import TWENTY_TWENTY_FIVE_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_five.day04 import (
    parse_input,
    solve_part_one,
    solve_part_two,
)
from advent_of_code.utils import load_input

TODAYS_TEST_INPUT_PATH = TWENTY_TWENTY_FIVE_TEST_INPUT_PATH.joinpath("day04.txt")


@pytest.fixture(scope="session")
def raw_input():
    return load_input(TODAYS_TEST_INPUT_PATH)


@pytest.fixture(scope="session")
def parsed_input(raw_input):
    return parse_input(raw_input)


def test_parse_input(raw_input):
    expected = [
        [".", ".", "@", "@", ".", "@", "@", "@", "@", "."],
        ["@", "@", "@", ".", "@", ".", "@", ".", "@", "@"],
        ["@", "@", "@", "@", "@", ".", "@", ".", "@", "@"],
        ["@", ".", "@", "@", "@", "@", ".", ".", "@", "."],
        ["@", "@", ".", "@", "@", "@", "@", ".", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", ".", "@"],
        [".", "@", ".", "@", ".", "@", ".", "@", "@", "@"],
        ["@", ".", "@", "@", "@", ".", "@", "@", "@", "@"],
        [".", "@", "@", "@", "@", "@", "@", "@", "@", "."],
        ["@", ".", "@", ".", "@", "@", "@", ".", "@", "."],
    ]
    actual = parse_input(raw_input)

    assert actual == expected


def test_solve_part_one(parsed_input):
    expected = 13
    actual = solve_part_one(parsed_input)

    assert actual == expected


def test_solve_part_two(parsed_input):
    expected = 43
    actual = solve_part_two(parsed_input)

    assert actual == expected
