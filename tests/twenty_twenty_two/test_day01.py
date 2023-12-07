import pytest

from advent_of_code.constants import TWENTY_TWENTY_TWO_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day01 import count_calories, count_top3_calories
from advent_of_code.utils import load_input

DAY01_TWENTY_TWENTY_TWO_TEST_INPUT_PATH = TWENTY_TWENTY_TWO_TEST_INPUT_PATH.joinpath("day01")


@pytest.fixture(scope="session")
def day01_input():
    return load_input(DAY01_TWENTY_TWENTY_TWO_TEST_INPUT_PATH)


def test_load_input():
    assert load_input(DAY01_TWENTY_TWENTY_TWO_TEST_INPUT_PATH) == [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]


def test_count_calories(day01_input):
    assert count_calories(day01_input) == 24000


def test_count_top3_calories(day01_input):
    assert count_top3_calories(day01_input) == 45000
