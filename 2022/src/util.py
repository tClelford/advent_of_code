from typing import List


def read_lines(path: str, clean: bool = True) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if clean:
        lines = [s.strip() for s in lines]

    return lines