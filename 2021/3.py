from typing import List
import numpy as np


def get_matrix(lines):
    mtrx = np.array([np.array(string_to_bin_array(l)) for l in lines if l != ""])
    print(mtrx.shape)
    return mtrx


def get_lines(path):
    with open(path) as file:
        lines = file.readlines()
    return lines


def three_one(path):
    lines = get_lines(path)
    mtrx = get_matrix(lines)
    sums = np.squeeze(np.asarray(mtrx.sum(axis=0)))
    gamma = np.array((sums / 1000) >= 0.5)
    epsilon = np.array((sums / 1000) < 0.5)

    print(to_int(gamma) * to_int(epsilon))


test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def three_two(path):
    lines = get_lines(path)
    mtrx = get_matrix(lines)
    oxygen = bit_criteria_recursive(mtrx, 0)
    carbon_dioxide = bit_criteria_recursive(mtrx, 0, is_oxygen=False)

    print(oxygen * carbon_dioxide)


def bit_criteria_recursive(matrix, i, is_oxygen=True):
    if len(matrix) == 1:
        return to_int(np.squeeze(np.array(matrix[0])) == 1)

    count = np.count_nonzero(np.transpose(matrix)[i, :] == 1)
    halfway = len(matrix) / 2
    if count >= halfway:
        flag = 1 if is_oxygen else 0
    else:
        flag = 0 if is_oxygen else 1

    new_matrix = np.array([a for a in matrix if a[i] == flag])
    print(new_matrix.shape)
    return bit_criteria_recursive(new_matrix, i + 1, is_oxygen)


def to_int(bin: List[bool]) -> int:
    val = 1
    res = 0
    for item in bin[::-1]:
        res = res if not item else res + val
        val = val * 2

    return res


def string_to_bin_array(string: str) -> List[int]:
    return [int(c) for c in string.strip()]


# three_one("./input_3.txt")
three_two("./input_3.txt")
