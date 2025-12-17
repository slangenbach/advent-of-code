import pytest

from advent_of_code.constants import TWENTY_TWENTY_FIVE_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_five.day02 import (
    parse_input,
    solve_part_one,
    solve_part_two,
)
from advent_of_code.utils import load_input

TODAYS_TEST_INPUT_PATH = TWENTY_TWENTY_FIVE_TEST_INPUT_PATH.joinpath("day02.txt")


@pytest.fixture(scope="session")
def raw_input():
    return load_input(TODAYS_TEST_INPUT_PATH)


@pytest.mark.xfail(raises=NotADirectoryError)
def test_parse_input(raw_input):
    assert parse_input == []


@pytest.mark.xfail(raises=NotADirectoryError)
def test_solve_part_one(raw_input):
    assert solve_part_one(raw_input) == 1227775554


@pytest.mark.xfail(raises=NotADirectoryError)
def test_solve_part_two(raw_input):
    assert solve_part_two(raw_input) == 42
