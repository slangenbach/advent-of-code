import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.calorie_counting import (
    count_calories,
    count_top3_calories,
)
from advent_of_code.utils import load_input

CALORIE_COUNTING_INPUT_PATH = TEST_INPUT_PATH.joinpath("input_calorie_counting")


@pytest.fixture(scope="session")
def calorie_counting_input():
    return load_input(CALORIE_COUNTING_INPUT_PATH)


def test_load_input():
    assert load_input(CALORIE_COUNTING_INPUT_PATH) == [
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


def test_count_calories(calorie_counting_input):
    assert count_calories(calorie_counting_input) == 24000


def test_count_top3_calories(calorie_counting_input):
    assert count_top3_calories(calorie_counting_input) == 45000
