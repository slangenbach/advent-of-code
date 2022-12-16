import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day13 import (
    compare_integers,
    compare_lists,
    is_correct_order,
    parse_input,
    solve_part_one,
    solve_part_two,
)
from advent_of_code.utils import load_input

DAY13_TEST_INPUT_PATH = TEST_INPUT_PATH.joinpath("day13")


@pytest.fixture(scope="session")
def day13_input():
    return load_input(DAY13_TEST_INPUT_PATH)


def test_parse_input(day13_input):
    assert parse_input(day13_input) == [
        [[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]],
        [[[1], [2, 3, 4]], [[1], 4]],
        [[9], [[8, 7, 6]]],
        [[[4, 4], 4, 4], [[4, 4], 4, 4, 4]],
        [[7, 7, 7, 7], [7, 7, 7]],
        [[], [3]],
        [[[[]]], [[]]],
        [[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]],
    ]


@pytest.mark.parametrize(
    ["left", "right", "expected"], [(1, 2, True), (2, 1, False), (1, 1, None)]
)
def test_compare_integers(left, right, expected):
    assert compare_integers(left, right) == expected


@pytest.mark.parametrize(
    ["left", "right", "expected"],
    [([1, 2], [1, 3], True), ([1, 1], [1, 1, 1], True), ([1, 1, 1], [1, 1], False)],
)
def test_compare_lists(left, right, expected):
    assert compare_lists(left, right) == expected


@pytest.mark.parametrize(
    ["left", "right", "expected"],
    [
        ([1, 1, 3, 1, 1], [1, 1, 5, 1, 1], True),
        ([[1], [2, 3, 4]], [[1], 4], True),
        ([9], [[8, 7, 6]], False),
        ([[4, 4], 4, 4], [[4, 4], 4, 4, 4], True),
        ([7, 7, 7, 7], [7, 7, 7], False),
        ([], [3], True),
        ([[[]]], [[]], False),
        (
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
            False,
        ),
    ],
)
def test_is_correct_order(left, right, expected):
    assert is_correct_order(left, right) == expected


def test_solve_part_one(day13_input):
    assert solve_part_one(day13_input) == 13


@pytest.mark.skip(reason="Not yet implemented")
def test_solve_part_two(day13_input):
    pass
