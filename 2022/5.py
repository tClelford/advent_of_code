from typing import List
from util import get_lines
import numpy as np

test_input = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]


def to_coords(input: str) -> List[List[int]]:

    return [
        [int(point) for point in coord.strip().split(",")]
        for coord in input.strip().split(" -> ")
        if input != ""
    ]


def five_one(input: List[str]):
    max_x, max_y = 0, 0
    coords = []

    for line in input:
        c1, c2 = to_coords(line)
        x, y = zip(c1, c2)
        max_x = max(max_x, max(x))
        max_y = max(max_y, max(y))
        coords.append([c1, c2])

    score_card = np.zeros((max_x + 1, max_y + 1), dtype=int)
    for c1, c2 in coords:
        points = get_line(c1, c2)
        matrix = np.zeros(score_card.shape, dtype=int)
        for x, y in points:
            matrix[x][y] = 1
        score_card = np.add(matrix, score_card)

    matches = np.array(score_card > 1)
    score = np.sum(np.sum(matches))
    print(score)


def get_line(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    is_vertical = x1 == x2
    is_horizontal = y1 == y2

    if not is_vertical and not is_horizontal:
        return diagonal_line(c1, c2)
    return line(x1, y1, y2, True) if is_vertical else line(y1, x1, x2, False)


def diagonal_line(c1, c2):
    start, end = c1, c2
    if c1[0] > c2[0]:
        start, end = c2, c1
    y_increment = 1 if start[1] < end[1] else -1
    out = []
    y = start[1]
    for x in range(start[0], end[0] + 1):
        out.append([x, y])
        y += y_increment
    return out


def line(fixed_axis: int, p1: int, p2: int, is_vertical: bool):
    min_p, max_p = min(p1, p2), max(p1, p2)
    return [
        [fixed_axis, p] if is_vertical else [p, fixed_axis]
        for p in range(min_p, max_p + 1)
    ]


five_one(test_input)

five_one(get_lines("./input_5.txt"))
