import pytest

from advent_of_code.constants import TWENTY_TWENTY_FIVE_TEST_INPUT_PATH
from advent_of_code.twenty_twenty_five.day02 import (
    generate_ids,
    is_also_invalid_id,
    is_invalid_id,
    parse_input,
    parse_range,
    solve_part_one,
    solve_part_two,
)
from advent_of_code.utils import load_input

TODAYS_TEST_INPUT_PATH = TWENTY_TWENTY_FIVE_TEST_INPUT_PATH.joinpath("day02.txt")


@pytest.fixture(scope="session")
def raw_input():
    return load_input(TODAYS_TEST_INPUT_PATH)


def test_parse_input(raw_input):
    expected = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]
    actual = parse_input(raw_input)

    assert actual == expected


def test_parse_range():
    expected = (13, 37)
    actual = parse_range("13-37")

    assert actual == expected


def test_generate_ids():
    expected = [val for val in range(13, 37 + 1)]
    actual = [val for val in generate_ids("13-37")]

    assert actual == expected


@pytest.mark.parametrize(
    ("id", "expected"),
    [
        (11, True),
        (12, False),
        (13, False),
        (22, True),
        (95, False),
        (99, True),
        (115, False),
        (998, False),
        (1010, True),
        (1012, False),
        (1188511880, False),
        (1188511885, True),
        (1188511890, False),
        (222220, False),
        (222222, True),
        (222224, False),
        (1698522, False),
        (1698528, False),
        (446443, False),
        (446446, True),
        (446449, False),
        (38593856, False),
        (38593859, True),
        (38593862, False),
    ],
)
def test_is_invalid_id(id: int, expected: bool):
    actual = is_invalid_id(str(id))

    assert actual == expected


@pytest.mark.parametrize(("id", "expected"), [(99, True), (111, True)])
def test_is_also_invalid_id(id: int, expected: bool):
    actual = is_also_invalid_id(str(id))

    assert actual == expected


def test_solve_part_one(raw_input):
    assert solve_part_one(raw_input) == 1227775554


@pytest.mark.xfail(raises=NotImplementedError)
def test_solve_part_two(raw_input):
    assert solve_part_two(raw_input) == 4174379265
