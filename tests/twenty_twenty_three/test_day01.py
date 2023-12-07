import pytest

from advent_of_code.constants import (
    TWENTY_TWENTY_THREE_TEST_INPUT_PATH,
)
from advent_of_code.twenty_twenty_three.day01 import parse_input, solve_part_one, solve_part_two
from advent_of_code.utils import load_input

DAY01_INPUT_PATH = TWENTY_TWENTY_THREE_TEST_INPUT_PATH.joinpath("day01")
DAY01_INPUT_PATH_PART_TWO = TWENTY_TWENTY_THREE_TEST_INPUT_PATH.joinpath("day01_part_02")


@pytest.fixture(scope="session")
def raw_input():
    return load_input(DAY01_INPUT_PATH)


@pytest.fixture(scope="session")
def raw_input_part_two():
    return load_input(DAY01_INPUT_PATH_PART_TWO)


def test_load_input(raw_input):
    assert load_input(DAY01_INPUT_PATH) == [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]


def test_parse_input(raw_input_part_two):
    assert parse_input(raw_input_part_two) == [
        "219",
        "8wo3",
        "abc123xyz",
        "x2ne34",
        "49872",
        "z1ight234",
        "7pqrst6teen",
    ]


def test_solve_part_one(raw_input):
    assert solve_part_one(raw_input) == 142


def test_solve_part_two(raw_input_part_two):
    assert solve_part_two(raw_input_part_two) == 281
