from typing import List


def get_elves(lines: List[str]) -> List[int]:
    current = 0
    elves = []
    for line in lines:
        line=line.strip()
        if not line:
            elves.append(current)
            current = 0
            continue
        current += int(line)

    return elves


def read_file(path: str) -> List[str]:
    with open(path, "r") as file:
        return file.readlines()


def main():
    lines= read_file("./data/one.txt")
    elves = get_elves(lines)
    elves_by_calories=sorted(elves)
    top_three = elves_by_calories[-3:]
    print(sum(top_three))


if __name__ == "__main__":
    main()