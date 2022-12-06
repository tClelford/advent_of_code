from functools import reduce
from typing import List


def to_ints(filename: str) -> List[int]:
    with open(filename) as file:
        lines = file.readlines()
    return [int(x) for x in lines if x != ""]


def one_one(lines):
    prev = int(lines[0])
    count = 0
    for i, x in enumerate(lines[1:]):
        if x == "":
            return count
        val = int(x)
        if val > prev:
            count += 1
        prev = val

    return count


def one_two(m: List[int], classes: int) -> int:
    count = 0
    l = len(m)
    l = 10
    end_at = l % classes
    prev = m[0:classes]
    for i in range(1, len(m)-end_at): #, x in enumerate(m)[classes:-end_at]:
        this = m[i : i + classes]
        print(f"{i}: prev: {prev} == {sum(prev)}| this {this} == {sum(this)}")
        if sum(this) > sum(prev):
            count += 1
        prev = this
    print(count)


# print(one_one())
ints = to_ints("./input_1.txt")
print(one_two(ints, 3))
