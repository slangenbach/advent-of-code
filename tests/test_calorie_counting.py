import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.calorie_counting import (
    count_calories,
    count_top3_calories,
)


@pytest.fixture(scope="session")
def input_calorie_counting():
    return TEST_INPUT_PATH.joinpath("input_calorie_counting")


def test_count_calories(input_calorie_counting):
    assert count_calories(input_calorie_counting) == 24000


def test_count_top3_calories(input_calorie_counting):
    assert count_top3_calories(input_calorie_counting) == 45000
