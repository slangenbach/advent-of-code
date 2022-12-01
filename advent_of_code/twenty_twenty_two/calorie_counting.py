from pathlib import Path
from advent_of_code.constants import TWENTY_TWENTY_TWO_PATH


def count_calories(calorie_list: Path) -> int:
    max_calories = 0
    counter = 0

    with calorie_list.open("r") as f:
        calories = f.read().split("\n")

    for calorie in calories:
        try:
            counter += int(calorie)
        except ValueError:
            if counter > max_calories:
                max_calories = counter
            counter = 0

    return max_calories


def count_top3_calories(calorie_list: Path) -> int:
    counter = 0
    result = []

    with calorie_list.open("r") as f:
        calories = f.read().split("\n")

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
    calorie_list = TWENTY_TWENTY_TWO_PATH.joinpath("input_calorie_counting")
    print(
        f"Solution for count_calories: {count_calories(calorie_list)}",
        f"Solution for count_top3_calories is: {count_top3_calories(calorie_list)}",
        sep="\n",
    )
