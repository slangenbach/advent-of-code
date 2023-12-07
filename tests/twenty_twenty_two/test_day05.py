import pytest

from advent_of_code.constants import TWENTY_TWENTY_TWO_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day05 import (
    parse_input,
    solve_part_one,
    solve_part_two,
)
from advent_of_code.utils import load_input

TODAYS_TWENTY_TWENTY_TWO_TEST_INPUT_PATH = TWENTY_TWENTY_TWO_TEST_INPUT_PATH.joinpath("day05")


@pytest.fixture(scope="session")
def raw_input():
    return load_input(TODAYS_TWENTY_TWENTY_TWO_TEST_INPUT_PATH)


def test_parse_input(raw_input):
    assert parse_input == []


def test_solve_part_one(raw_input):
    assert solve_part_one(raw_input) == 42


def test_solve_part_two(raw_input):
    assert solve_part_two(raw_input) == 42
