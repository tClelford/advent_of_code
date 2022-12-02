from enum import Enum
from typing import Iterable, Tuple
from functools import reduce


class Opponent(Enum):
    """Docstring for Opponent."""

    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class Me(Enum):
    """Docstring for Me."""

    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Result(Enum):
    """Docstring for Result."""
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


response_lookup = {
    Opponent.ROCK: {Result.DRAW: Me.ROCK, Result.WIN: Me.PAPER, Result.LOSE: Me.SCISSORS},
    Opponent.PAPER: {Result.DRAW: Me.PAPER, Result.LOSE: Me.ROCK, Result.WIN: Me.SCISSORS},
    Opponent.SCISSORS: {Result.DRAW: Me.SCISSORS, Result.LOSE: Me.PAPER, Result.WIN: Me.ROCK},
}


scores = {
    Opponent.ROCK: {Me.ROCK: 3, Me.PAPER: 6, Me.SCISSORS: 0},
    Opponent.PAPER: {Me.ROCK: 0, Me.PAPER: 3, Me.SCISSORS: 6},
    Opponent.SCISSORS: {Me.ROCK: 6, Me.PAPER: 0, Me.SCISSORS: 3},
}

shape_bonus = {
    Me.ROCK: 1,
    Me.PAPER: 2,
    Me.SCISSORS: 3,
}


def get_games(games: Iterable[str]) -> Tuple[Opponent, Me]:
    for s in games:
        cleaned = s.strip()
        if not cleaned:
            continue
        turn = cleaned.split(" ")
        yield Opponent(turn[0]), Result(turn[1])


test = ["A Y", "B X", "C Z"]


def reducer(total: int, game: Tuple[Opponent, Result]) -> int:
    opponent, result = game
    me = response_lookup[opponent][result]
    return total + shape_bonus[me] + scores[opponent][me]


def main():
    with open("./data/two.txt", "r") as f:
        lines = f.readlines()

    total_score = reduce(reducer, get_games(lines), 0)
    print(total_score)


if __name__ == "__main__":
    main()
