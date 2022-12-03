import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.rock_paper_scissors import (
    evaluate_tournament,
    load_input,
    transform_scores,
)


@pytest.fixture(scope="session")
def input_rock_paper_scissors():
    return TEST_INPUT_PATH.joinpath("input_rock_paper_scissors")


def test_load_input(input_rock_paper_scissors):
    assert load_input(input_rock_paper_scissors) == ["A Y", "B X", "C Z"]


def test_transform_scores():
    assert transform_scores("A", "Z", faked=False) == ("rock", "scissors")


def test_transform_faked_scores():
    assert transform_scores("A", "Z", faked=True) == ("rock", "win")


def test_evaluate_tournament(input_rock_paper_scissors):
    rounds = load_input(input_rock_paper_scissors)
    assert evaluate_tournament(rounds, faked=False) == 15


def test_evaluate_faked_tournament(input_rock_paper_scissors):
    rounds = load_input(input_rock_paper_scissors)
    assert evaluate_tournament(rounds, faked=True) == 12
