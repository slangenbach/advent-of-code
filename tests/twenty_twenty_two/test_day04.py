import pytest

from advent_of_code.constants import TWENTY_TWENTY_TWO_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day04 import (
    calculate_fully_contained_assignments,
    calculate_overlapping_assignments,
    is_fully_contained,
    is_overlapping,
    split_assignment,
    transform_sections,
)
from advent_of_code.utils import load_input

DAY04_INPUT_PATH = TWENTY_TWENTY_TWO_TEST_INPUT_PATH.joinpath("day04")


@pytest.fixture(scope="session")
def day04_input():
    return load_input(DAY04_INPUT_PATH)


def test_load_data():
    assert load_input(DAY04_INPUT_PATH) == [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]


def test_split_assignments():
    assert split_assignment("2-4,6-8") == [["2", "4"], ["6", "8"]]


def test_transform_sections():
    assert transform_sections([["2", "4"], ["6", "8"]]) == (2, 4, 6, 8)


def test_is_fully_contained():
    assert not is_fully_contained(
        start_first_section=2,
        stop_first_section=4,
        start_second_section=6,
        stop_second_section=8,
    )
    assert is_fully_contained(
        start_first_section=2,
        stop_first_section=8,
        start_second_section=3,
        stop_second_section=7,
    )


def test_calculate_fully_contained_assignments(day04_input):
    assert calculate_fully_contained_assignments(day04_input) == 2


def test_is_overlapping():
    assert not is_overlapping(
        start_first_section=2,
        stop_first_section=4,
        start_second_section=6,
        stop_second_section=8,
    )
    assert is_overlapping(
        start_first_section=5,
        stop_first_section=7,
        start_second_section=7,
        stop_second_section=9,
    )
    assert is_overlapping(
        start_first_section=6,
        stop_first_section=6,
        start_second_section=4,
        stop_second_section=6,
    )
    assert is_overlapping(
        start_first_section=2,
        stop_first_section=6,
        start_second_section=4,
        stop_second_section=8,
    )


def test_calculate_overlapping_assignments(day04_input):
    assert calculate_overlapping_assignments(day04_input) == 4
