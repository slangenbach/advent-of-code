"""Puzzle for advent of code 2022 day 03."""

from string import ascii_lowercase, ascii_uppercase
from typing import Tuple

from advent_of_code.constants import TWENTY_TWENTY_TWO_INPUT_PATH
from advent_of_code.utils import load_input


def split_compartments(rucksack: str) -> Tuple[str, str]:
    midpoint = len(rucksack) // 2
    return rucksack[:midpoint], rucksack[midpoint:]


def find_identical_item(first_compartment: str, second_compartment: str) -> str:
    return set(first_compartment).intersection(set(second_compartment)).pop()


def get_priority(item: str) -> int:
    if item.islower():
        return ascii_lowercase.index(item) + 1
    return ascii_uppercase.index(item) + 1 + 26


def calculate_item_priority(rucksacks: list[str]) -> int:
    total_priority = 0

    for rucksack in rucksacks:
        first_compartment, second_compartment = split_compartments(rucksack)
        identical_item = find_identical_item(first_compartment, second_compartment)
        priority = get_priority(identical_item)
        total_priority += priority

    return total_priority


def split_groups(
    rucksacks: list[str],
) -> list[list[str]]:
    groups = []
    for index in range(0, len(rucksacks), 3):
        groups.append([rucksacks[index], rucksacks[index + 1], rucksacks[index + 2]])

    return groups


def find_badge(first_group: str, second_group: str, third_group: str) -> str:
    return set(first_group).intersection(set(second_group), set(third_group)).pop()


def calculate_badge_priority(rucksacks: list[str]) -> int:
    total_priority = 0

    groups = split_groups(rucksacks)
    for group in groups:
        badge = find_badge(group[0], group[1], group[2])
        priority = get_priority(badge)
        total_priority += priority

    return total_priority


if __name__ == "__main__":
    day03_input = TWENTY_TWENTY_TWO_INPUT_PATH.joinpath("day03")
    rucksacks = load_input(day03_input)
    item_priority = calculate_item_priority(rucksacks)
    badge_priority = calculate_badge_priority(rucksacks)
    print(
        "Advent of code 2022 day 03:",
        f"Item priority: {item_priority}",
        f"Badge priority: {badge_priority}",
        sep="\n",
    )
