import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.rock_paper_scissors import (
    evaluate_tournament,
    transform_scores,
)
from advent_of_code.utils import load_input

ROCK_PAPER_SCISSORS_INPUT_PATH = TEST_INPUT_PATH.joinpath("input_rock_paper_scissors")


@pytest.fixture(scope="session")
def rock_paper_scissors_input():
    return load_input(ROCK_PAPER_SCISSORS_INPUT_PATH)


def test_load_input():
    assert load_input(ROCK_PAPER_SCISSORS_INPUT_PATH) == ["A Y", "B X", "C Z"]


def test_transform_scores():
    assert transform_scores("A", "Z", faked=False) == ("rock", "scissors")


def test_transform_faked_scores():
    assert transform_scores("A", "Z", faked=True) == ("rock", "win")


def test_evaluate_tournament(rock_paper_scissors_input):
    assert evaluate_tournament(rock_paper_scissors_input, faked=False) == 15


def test_evaluate_faked_tournament(rock_paper_scissors_input):
    assert evaluate_tournament(rock_paper_scissors_input, faked=True) == 12
