import pytest

from advent_of_code.constants import TWENTY_TWENTY_FIVE_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_five.day03 import (
    solve_part_one,
    solve_part_two,
)
from advent_of_code.utils import load_input

TODAYS_TEST_INPUT_PATH = TWENTY_TWENTY_FIVE_TEST_INPUT_PATH.joinpath("day03.txt")


@pytest.fixture(scope="session")
def raw_input():
    return load_input(TODAYS_TEST_INPUT_PATH)


def test_solve_part_one(raw_input):
    expected = 357
    actual = solve_part_one(raw_input)

    assert actual == expected


@pytest.mark.xfail(raises=NotImplementedError)
def test_solve_part_two(raw_input):
    expected = 3121910778619
    actual = solve_part_two(raw_input)

    assert actual == expected
