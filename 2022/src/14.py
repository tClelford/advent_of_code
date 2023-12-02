import sys
from typing import List, Tuple
import numpy as np

def read_lines(path: str, clean: bool = True) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if clean:
        lines = [s.strip() for s in lines]

    return lines

test_data = [
"498,4 -> 498,6 -> 496,6",
"503,4 -> 502,4 -> 502,9 -> 494,9",
]


def get_path(line:str)-> List[Tuple[int, int]]:
    strs = line.split("->")
    return [get_coords(s) for s in strs]

def get_coords(s:str)-> Tuple[int, int]:
    x, y = s.strip().split(",")
    return int(x), int(y)


def path_coords(start, end):
    start_x,start_y= start
    end_x, end_y=end

    arr = [start, end]
    if start_x == end_x:
        arr.extend([(start_x, y) for y in range(min(start_y, end_y),max(start_y, end_y))])
    else:
        arr.extend([(x, start_y) for x in range(min(start_x, end_x), max(start_x, end_x))])
    return arr


def build_matrix(paths:List[List[Tuple[int, int]]]):
    coords = []
    max_x = 0
    max_y = 0
    for path in paths:
        for start, end in zip(*[iter(path)]*2):
            max_x = max(max(start[0], end[0]), max_x)
            max_y = max(max(start[1], end[1]), max_y)

            coords.extend(path_coords(start, end))


    board= np.full((max_y+1, max_x+1), ".", dtype=str)

    for coord in coords:
        x,y = coord
        board[y][x]="#"
    return board


def print_board(board):
    np.savetxt("14_vis.txt", board, fmt='%s')


def part_1(data:List[str]):
    paths = [get_path(s) for s in data]
    board = build_matrix(paths)
    print_board(board)

    answer=None
    print(f"Part 1: {answer}")


def part_2(data:List[str]):

    answer=None
    print(f"Part 2: {answer}")


def main():
    if len(sys.argv) > 1:
        print(sys.argv)
        data = read_lines(sys.argv[1])
    else:
        data = test_data

    part_1(data)
    part_2(data)


if __name__ == "__main__":

    main()
