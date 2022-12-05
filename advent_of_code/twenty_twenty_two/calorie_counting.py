"""Puzzle for advent of code 2022 day 01."""

from advent_of_code.constants import TWENTY_TWENTY_TWO_PATH
from advent_of_code.utils import load_input


def count_calories(calories: list[str]) -> int:
    max_calories = 0
    counter = 0

    for calorie in calories:
        try:
            counter += int(calorie)
        except ValueError:
            if counter > max_calories:
                max_calories = counter
            counter = 0

    return max_calories


def count_top3_calories(calories: list[str]) -> int:
    counter = 0
    result = []

    for calorie in calories:
        try:
            counter += int(calorie)
        except ValueError:
            result.append(counter)
            counter = 0

    # account for edge case
    if counter:
        result.append(counter)

    return sum(sorted(result)[-3:])


if __name__ == "__main__":
    calorie_counting_input = TWENTY_TWENTY_TWO_PATH.joinpath("input_calorie_counting")
    calorie_list = load_input(calorie_counting_input)
    print(
        f"Solution for count_calories: {count_calories(calorie_list)}",
        f"Solution for count_top3_calories is: {count_top3_calories(calorie_list)}",
        sep="\n",
    )
