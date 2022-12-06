from typing import Dict, FrozenSet, Iterable, List, Set, Tuple
import numpy as np
import pprint

from pprint import pp

test_input = [
    "2199943210",
    "3987894921",
    "9856789892",
    "8767896789",
    "9899965678",
]


def get_board(input=Iterable[str]):
    return np.array([np.array([int(c) for c in s.strip()]) for s in input if s != ""])


def one(board):
    print(
        sum(
            [
                val + 1
                for (x, y), val in np.ndenumerate(board)
                if is_lower_than_neighbours(x, y, val, board)
            ]
        )
    )


def neighbours(x: int, y: int, board):
    max_x, max_y = board.shape
    left, right, up, down = -1, -1, -1, -1
    if x > 0:
        left = board[x - 1, y]
    if x < max_x - 1:
        right = board[x + 1, y]
    if y > 0:
        up = board[x, y - 1]
    if y < max_y - 1:
        down = board[x, y + 1]
    return 


def is_lower_than_neighbours(x: int, y: int, val: int, board) -> bool:
    max_x, max_y = board.shape

    if x > 0 and val >= board[x - 1, y]:
        return False
    if x < max_x - 1 and val >= board[x + 1, y]:
        return False
    if y > 0 and val >= board[x, y - 1]:
        return False
    if y < max_y - 1 and val >= board[x, y + 1]:
        return False

    return True


def get_input(test_input=None) -> Iterable[str]:
    with open("./9/input.txt") as file:
        lines = file.readlines()
    return test_input if test_input else lines


def two(board):
    shape = board == 9
    for x in shape:
        s = ""
        for y in x:
            c = 1 if y else 0
            s += f"{c},"
        print(s)

    nines = []
    for (x, y), val in np.ndenumerate(board):
        if val == 9:
            nines.append((x, y))


two(get_board(get_input()))
