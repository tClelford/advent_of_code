from typing import List


def read_lines(path: str, clean: bool = True) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if clean:
        lines = [s.strip() for s in lines]

    return lines


def some_numpy_operation(input: List[List[int]])-> int:
    import numpy as np

    arr = np.array(input, dtype=int)
    return arr.max()




print(some_numpy_operation([[1,2,3], [4,5,6]]))