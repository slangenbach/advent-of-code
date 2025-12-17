import pytest

from advent_of_code.constants import TWENTY_TWENTY_FIVE_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_five.day01 import (
    solve_part_one,
    solve_part_two,
)
from advent_of_code.utils import load_input

TODAYS_TEST_INPUT_PATH = TWENTY_TWENTY_FIVE_TEST_INPUT_PATH.joinpath("day01.txt")


@pytest.fixture(scope="session")
def raw_input():
    return load_input(TODAYS_TEST_INPUT_PATH)


def test_solve_part_one(raw_input):
    assert solve_part_one(raw_input) == 3


def test_solve_part_two(raw_input):
    assert solve_part_two(raw_input) == 6
