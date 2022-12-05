import pytest

from advent_of_code.constants import TEST_INPUT_PATH
from advent_of_code.twenty_twenty_two.rucksack_reorganization import (
    calculate_badge_priority,
    calculate_item_priority,
    find_badge,
    find_identical_item,
    get_priority,
    split_compartments,
    split_groups,
)
from advent_of_code.utils import load_input

RUCKSACK_REORGANIZATION_INPUT_PATH = TEST_INPUT_PATH.joinpath(
    "input_rucksack_reorganization"
)


@pytest.fixture(scope="session")
def rucksack_reorganization_input():
    return load_input(RUCKSACK_REORGANIZATION_INPUT_PATH)


def test_load_input():
    assert load_input(RUCKSACK_REORGANIZATION_INPUT_PATH) == [
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


def test_calculate_item_priority(rucksack_reorganization_input):
    assert calculate_item_priority(rucksack_reorganization_input) == 157


def test_split_groups(rucksack_reorganization_input):
    assert split_groups(rucksack_reorganization_input) == [
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


def test_calculate_badge_priority(rucksack_reorganization_input):
    assert calculate_badge_priority(rucksack_reorganization_input) == 70
