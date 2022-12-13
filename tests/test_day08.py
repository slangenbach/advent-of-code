import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day08 import (
    calculate_max_scenic_score,
    calculate_scenic_score,
    calculate_visible_trees,
    get_sight_lines,
    is_visible,
    load_input,
)

DAY08_INPUT_PATH = TEST_INPUT_PATH.joinpath("day08")


@pytest.fixture(scope="session")
def day08_input():
    return load_input(DAY08_INPUT_PATH)


def test_load_input():
    assert load_input(DAY08_INPUT_PATH) == [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]


@pytest.mark.parametrize(
    ["x", "y", "expected"],
    [
        (2, 1, ([5, 2], [3], [1, 2], [3, 5, 3])),
        (0, 0, ([], [], [0, 3, 7, 3], [2, 6, 3, 3])),
        (3, 1, ([5, 5, 2], [7], [2], [3, 4, 9])),
    ],
)
def test_get_sight_lines(x, y, day08_input, expected):
    assert get_sight_lines(x=x, y=y, grid=day08_input) == expected


def test_is_visible():
    assert is_visible(height=5, sight_lines=([5, 2], [3], [1, 2], [3, 5, 3]))
    assert not is_visible(height=1, sight_lines=([5, 5, 2], [7], [2], [3, 4, 9]))


def test_calculate_visible_trees(day08_input):
    assert calculate_visible_trees(day08_input) == 21


def test_calculate_scenic_score():
    assert (
        calculate_scenic_score(height=5, sight_lines=([5, 2], [3], [1, 2], [3, 5, 3]))
        == 4
    )


def test_calculate_max_scenic_score(day08_input):
    assert calculate_max_scenic_score(day08_input) == 8
