import pytest

from advent_of_code.constants import TWENTY_TWENTY_TWO_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day02 import evaluate_tournament, transform_scores
from advent_of_code.utils import load_input

DAY02_INPUT_PATH = TWENTY_TWENTY_TWO_TEST_INPUT_PATH.joinpath("day02")


@pytest.fixture(scope="session")
def day02_input():
    return load_input(DAY02_INPUT_PATH)


def test_load_input():
    assert load_input(DAY02_INPUT_PATH) == ["A Y", "B X", "C Z"]


def test_transform_scores():
    assert transform_scores("A", "Z", faked=False) == ("rock", "scissors")


def test_transform_faked_scores():
    assert transform_scores("A", "Z", faked=True) == ("rock", "win")


def test_evaluate_tournament(day02_input):
    assert evaluate_tournament(day02_input, faked=False) == 15


def test_evaluate_faked_tournament(day02_input):
    assert evaluate_tournament(day02_input, faked=True) == 12
