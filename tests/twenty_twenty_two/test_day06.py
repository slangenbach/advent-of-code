import pytest

from advent_of_code.constants import TWENTY_TWENTY_TWO_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day06 import find_marker, has_duplicate
from advent_of_code.utils import load_input

DAY06_INPUT_PATH = TWENTY_TWENTY_TWO_TEST_INPUT_PATH.joinpath("day06")


@pytest.fixture(scope="session")
def day06_input():
    return load_input(DAY06_INPUT_PATH)


def test_load_input():
    inputs = load_input(DAY06_INPUT_PATH)
    assert inputs[0] == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_has_duplicate():
    assert has_duplicate(["a", "b", "c", "a"])
    assert not has_duplicate(["a", "b", "c", "d"])


@pytest.mark.parametrize("example,expected", [(0, 7), (1, 5), (2, 6), (3, 10), (4, 11)])
def test_find_package_marker(day06_input, example, expected):
    assert find_marker(buffer=day06_input[example], distinct_chars=4) == expected


@pytest.mark.parametrize("example,expected", [(0, 19), (1, 23), (2, 23), (3, 29), (4, 26)])
def test_find_message_marker(day06_input, example, expected):
    assert find_marker(buffer=day06_input[example], distinct_chars=14) == expected
