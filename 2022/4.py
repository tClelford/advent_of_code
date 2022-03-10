from typing import Iterable, List
import numpy as np
from util import get_lines


class Board:
    def __init__(self, card) -> None:
        self.card = np.array(card)
        self.scored = np.zeros(self.card.shape, dtype=bool)

    def house(self, n: int) -> bool:
        return self.could_have_won([n])

    def score(self, n: int) -> int:
        mask = np.invert(self.scored)
        masked = np.multiply(self.card, mask)
        score = np.sum(masked)
        return score * n

    def could_have_won(self, ns: List[int]) -> bool:
        this_round = np.isin(self.card, ns)
        self.scored = np.add(self.scored, this_round)
        rows = np.all(self.scored, axis=1)
        if any(rows):
            return True
        columns = np.all(self.scored.transpose(), axis=1)
        return any(columns)


def numbers(s: str, split_on=",") -> List[int]:
    return [int(c) for c in s.strip().split(split_on)]


def get_boards(lines: Iterable[str]) -> List[Board]:
    output = []
    current = []
    for l in lines:
        cleaned = l.strip()
        if cleaned == "":
            if len(current) > 0:
                output.append(Board(current))
                current = []
            continue
        row = [int(c) for c in cleaned.split() if c != ""]
        if len(row) == 0:
            continue
        current.append(row)
    if len(current) > 0:
        output.append(Board(current))

    return np.array(output)


path = "./input_4.txt"
test_frame = [
    "87 60 64 25 12",
    "12  12 11 12 12",
    " 6 12 58 11 12",
    "23 49 44 91 12",
    "45 52 99 47 12",
]


def three_one():
    lines = get_lines(path)
    bingo_numbers = numbers(lines[0])
    boards = get_boards(lines[1:])
    for n in bingo_numbers:
        for board in boards:
            if board.house(n):
                print(board.score(n))
                return


def three_two():
    lines = get_lines(path)
    bingo_numbers = numbers(lines[0])
    boards = get_boards(lines[1:])
    loser, remaining_numbers = bin_search(boards, bingo_numbers)
    for n in remaining_numbers:
        if loser.house(n):
            print(loser.score(n))
            return
    

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def bin_search(boards: List[Board], numbers: List[int]):
    first_half, second_half = split_list(numbers)
    losers = [b for b in boards if not b.could_have_won(first_half)]

    if len(losers) == 1:
        return losers[0], second_half
    elif len(losers) > 0:
        return bin_search(losers, second_half)
    else:
        return bin_search(boards, first_half)

three_two()
