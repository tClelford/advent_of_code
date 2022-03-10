from os import error
from typing import List, Tuple


def read_instructions(path):
    with open(path) as file:
        lines = file.readlines()
    depth, horizontal_position, aim = 0, 0, 0

    for line in lines:
        if line == "":
            continue
        direction, distance = to_instruction(line)
        print(f"direction: {direction}| distance: {distance}")
        if direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance
        elif direction == "forward":
            horizontal_position += distance
            depth += (aim * distance)
            if depth < 0:
                depth = 0
        else:
            raise error("WTF")

        print(f"depth: {depth} | distance: {horizontal_position}| aim: {aim}")

    return depth * horizontal_position


def to_instruction(st: str) -> Tuple[str, int]:
    split = st.lower().split(" ")
    return (split[0], int(split[1][0]))


print(read_instructions("./input_2.txt"))
