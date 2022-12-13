import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.day03 import (
    calculate_badge_priority,
    calculate_item_priority,
    find_badge,
    find_identical_item,
    get_priority,
    split_compartments,
    split_groups,
)
from advent_of_code.utils import load_input

DAY03_INPUT_PATH = TEST_INPUT_PATH.joinpath("day03")


@pytest.fixture(scope="session")
def day03_input():
    return load_input(DAY03_INPUT_PATH)


def test_load_input():
    assert load_input(DAY03_INPUT_PATH) == [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]


def test_split_compartment():
    assert split_compartments("vJrwpWtwJgWrhcsFMMfFFhFp") == (
        "vJrwpWtwJgWr",
        "hcsFMMfFFhFp",
    )


def test_find_identical_item():
    assert (
        find_identical_item(
            first_compartment="vJrwpWtwJgWr", second_compartment="hcsFMMfFFhFp"
        )
        == "p"
    )


def test_get_priority():
    assert get_priority("p") == 16
    assert get_priority("L") == 38


def test_calculate_item_priority(day03_input):
    assert calculate_item_priority(day03_input) == 157


def test_split_groups(day03_input):
    assert split_groups(day03_input) == [
        [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        ],
        [
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw",
        ],
    ]


def test_find_badge():
    assert (
        find_badge(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
        )
        == "r"
    )


def test_calculate_badge_priority(day03_input):
    assert calculate_badge_priority(day03_input) == 70
