"""Puzzle for advent of code 2022 day 02."""

from typing import Tuple

from advent_of_code.constants import TWENTY_TWENTY_TWO_PATH
from advent_of_code.utils import load_input

OUTCOME_SCORE = {"win": 6, "draw": 3, "lost": 0}

SHAPE_SCORE = {"rock": 1, "paper": 2, "scissors": 3}

STRATEGY_MAPPING = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissors",
    "Z": "scissors",
}

FAKE_MAPPING = {"X": "lose", "Y": "draw", "Z": "win"}


def transform_scores(opponent: str, you: str, faked: bool) -> Tuple[str, str]:
    if faked:
        return STRATEGY_MAPPING[opponent], FAKE_MAPPING[you]

    return STRATEGY_MAPPING[opponent], STRATEGY_MAPPING[you]


def evaluate_round(opponent: str, you: str) -> int:
    if (
        (opponent == "rock" and you == "rock")
        or (opponent == "paper" and you == "paper")
        or (opponent == "scissors" and you == "scissors")
    ):
        return OUTCOME_SCORE["draw"] + SHAPE_SCORE[you]
    elif (
        (opponent == "rock" and you == "paper")
        or (opponent == "paper" and you == "scissors")
        or (opponent == "scissors" and you == "rock")
    ):
        return OUTCOME_SCORE["win"] + SHAPE_SCORE[you]
    else:
        return OUTCOME_SCORE["lost"] + SHAPE_SCORE[you]


def evaluate_faked_round(opp: str, you: str):
    if you == "lose":
        if opp == "rock":
            shape = "scissors"
        elif opp == "paper":
            shape = "rock"
        else:
            shape = "paper"
        return OUTCOME_SCORE["lost"] + SHAPE_SCORE[shape]
    elif you == "win":
        if opp == "rock":
            shape = "paper"
        elif opp == "paper":
            shape = "scissors"
        else:
            shape = "rock"
        return OUTCOME_SCORE["win"] + SHAPE_SCORE[shape]
    else:
        return OUTCOME_SCORE["draw"] + SHAPE_SCORE[opp]


def evaluate_tournament(rounds: list[str], faked: bool) -> int:
    total_score = 0

    for round in rounds:
        raw_opponent_score, raw_your_score = round.split(" ")
        if faked:
            opponent_score, your_score = transform_scores(
                raw_opponent_score, raw_your_score, faked=True
            )
            score = evaluate_faked_round(opponent_score, your_score)
        else:
            opponent_score, your_score = transform_scores(
                raw_opponent_score, raw_your_score, faked=False
            )
            score = evaluate_round(opponent_score, your_score)

        total_score += score

    return total_score


if __name__ == "__main__":
    rock_paper_scissors_input = TWENTY_TWENTY_TWO_PATH.joinpath(
        "input_rock_paper_scissors"
    )
    strategy_guide = load_input(rock_paper_scissors_input)
    legit_score = evaluate_tournament(strategy_guide, faked=False)
    faked_score = evaluate_tournament(strategy_guide, faked=True)
    print(
        f"Total score for legit tournament: {legit_score}",
        f"Total score for faked tournament: {faked_score}",
        sep="\n",
    )
