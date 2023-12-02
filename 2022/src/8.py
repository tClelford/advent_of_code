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


def rotate_arr_90(arr):
    rotated = np.rot90(arr, k=1)
    return rotated


def get_visible_count(input: List[str]) -> int:
    vals = get_input_matrix(input)
    visible = np.zeros(vals.shape)

    set_visibles(vals=)




    vals = np.rot90(vals, 2)
    visible = np.rot90(visible, 2)


def set_visibles(vals: np.ndarray, visible:np.ndarray):
    for x, arr in enumerate(vals):
        for y, _ in enumerate(arr):
            if y == 0:
                continue

            val = arr[y]
            trees_to_edge = arr[:y]

            if val > trees_to_edge.max():
                visible[x][y] = 1


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





def test_rotate():
    input = ["12","34"]
    matrix = get_input_matrix(input)


def main():
    test_rotate()


if __name__ == "__main__":
    main()