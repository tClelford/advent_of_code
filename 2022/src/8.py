import numpy as np
from typing import List
from util import read_lines

lines = read_lines("./2022/data/8.txt")

test = [
    "30373",
    "25512",
    "65332",
    "33549",
    "35390",
]

test_2 = ["12",
        "34"]

def get_visible_count(input: List[str]) -> int:
    vals = get_input_matrix(input)
    visible = np.zeros(vals.shape)
    for i in range(4):
        visible = np.rot90(visible, i)
        vals = np.rot90(vals, i)
        visible[0] = 1

        for x, arr in enumerate(vals):
            for y, _ in enumerate(arr):
                if y == 0:
                    continue

                val = arr[y]
                trees_to_edge = arr[0:y]

                if val > trees_to_edge.max():
                    visible[x][y] = 1

    vals = np.rot90(vals, 2)
    visible = np.rot90(visible, 2)




    print("visible trees:", sum(sum(visible)))


def get__max_score(input: List[str])-> int:
    trees = get_input_matrix(input)
    w, h = trees.shape
    scores = np.zeros((w, h, 4))

    for x, row in enumerate(trees):
        for y, tree in enumerate(row):
            left = get_left(x, tree, row)


def get_left(x: int, tree: int, row)-> int:
    if x == 0:
        return 0
    neighbours = row[:x]
    reversed = neighbours[::-1]
    for i, val in enumerate(reversed):
        if val >= tree:
            return i
    return len(row)

def get_right(x, tree, row)->int:
    if x == len(row):
        return 0
    neighbours = row[x:]
    for i, val in enumerate(neighbours):
        if val >= tree:
            return i
    return len(row)



def get_input_matrix(input: List[str]):
    return np.array([[int(c) for c in l] for l in input], np.int32)


input = get_input_matrix(test)
for x, tree in enumerate(input[0]):
    print(get_left(x, int(tree), input[0]))


get_visible_count(test_2)



