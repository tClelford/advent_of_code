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
def calc_score(arr) -> int:
   return [[ y[0] * y[1] * y[2] * y[3] for y in x] for x in arr]

def get_visible_count(input: List[str]) -> int:
    vals = get_input_matrix(input)
    visible = np.zeros(vals.shape)
    scores = np.zeros((vals.shape[0], vals.shape[1], 4))
    for i in range(4):
        visible = np.rot90(visible, i)
        vals = np.rot90(vals, i)
        scores = np.rot90(scores, i)
        visible[0] = 1

        for x, arr in enumerate(vals):
            for y, _ in enumerate(arr):
                if y == 0:
                    continue

                val = arr[y]
                trees_to_edge = arr[0:y]
                score = 0
                backwards = trees_to_edge[-1::-1]
                for tree in backwards:
                    if tree >= val:
                        break
                    score += 1
                scores[x][y][i] = score
                if visible[x][y] == 1:
                    continue

                if val > trees_to_edge.max():
                    visible[x][y] = 1

    vals = np.rot90(vals, 2)
    visible = np.rot90(visible, 2)

    calc_scores = calc_score(scores)


    print("visible trees:", sum(sum(visible)))
    print("max_score", np.amax(calc_scores))


def get_input_matrix(input: List[str]):
    return np.array([[int(c) for c in l] for l in input], np.int32)


get_visible_count(test)



