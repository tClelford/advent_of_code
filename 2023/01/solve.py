import sys
from typing import List, Optional


def read_lines(path: str, clean: bool = True) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if clean:
        lines = [s.strip() for s in lines]

    return lines


test_data = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def value_part_two(s: str) -> str:
    first, last = None, None
    replaces = [
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]

    for i, c in enumerate(s):
        if c in "123456789":
            if first is None:
                first = c
            last = c
        for word, num in replaces:
            if s[i : i + len(word)] == word:
                if first is None:
                    first = str(num)
                last = str(num)
    val = int(first + last)
    print(s, val)
    return val


def get_value(s: str) -> int:
    first, last = None, None
    for c in s:
        # parse c as int
        try:
            int(c)
        except ValueError:
            continue
        if first is None:
            first = c
        last = c
    return int(first + last)


def part_1(data: List[str]):
    answer = 0
    for line in data:
        answer += get_value(line)
    print(f"Part 1: {answer}")


def part_2(data: List[str]):
    answer = 0
    for line in data:
        answer += value_part_two(line)
    print(f"Part 2: {answer}")


def main():
    if len(sys.argv) > 1:
        data = read_lines(sys.argv[1])
    else:
        data = test_data

    # part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
