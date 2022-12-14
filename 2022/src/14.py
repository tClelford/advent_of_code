import sys
from typing import List


def read_lines(path: str, clean: bool = True) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if clean:
        lines = [s.strip() for s in lines]

    return lines

test_data = []

def part_1(data:List[str]):

    answer=None
    print(f"Part 1: {answer}")

def part_2(data:List[str]):

    answer=None
    print(f"Part 2: {answer}")


def main():
    if len(sys.argv) > 1:
        data = read_lines(sys.argv[1])
    else:
        data = test_data

    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
