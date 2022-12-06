from typing import Dict, List


test_data = [
    "dc-end",
    "HN-start",
    "start-kj",
    "dc-start",
    "dc-HN",
    "LN-dc",
    "HN-end",
    "kj-sa",
    "kj-HN",
    "kj-dc",
]

actual = [
    "dr-of",
    "start-KT",
    "yj-sk",
    "start-gb",
    "of-start",
    "IJ-end",
    "VT-sk",
    "end-sk",
    "VT-km",
    "KT-end",
    "IJ-of",
    "dr-IJ",
    "yj-IJ",
    "KT-yj",
    "gb-VT",
    "dr-yj",
    "VT-of",
    "PZ-dr",
    "KT-of",
    "KT-gb",
    "of-gb",
    "dr-sk",
    "dr-VT",
]


noddy = [
    "start-A",
    "start-b",
    "A-c",
    "A-b",
    "b-d",
    "A-end",
    "b-end",
]


def to_path_lookup(dataset: List[str]) -> Dict[str, List[str]]:
    dic = {}
    for line in dataset:
        start, end = line.split("-")
        if start not in dic:
            dic[start] = []
        dic[start].append(end)
        if end not in dic:
            dic[end] = []
        if start not in dic[end]:
            dic[end].append(start)
    return dic


START, END = "start", "end"


def recursive_walk(
    path_so_far: List[str], lookup: Dict[str, List[str]]
) -> List[List[str]]:
    current_pos = path_so_far[-1]
    if current_pos == END:
        return [path_so_far]

    return_paths = []
    for next_step in lookup[current_pos]:
        if next_step.islower() and next_step in path_so_far:
            continue
        new_path = path_so_far.copy()
        new_path.append(next_step)
        paths = recursive_walk(new_path, lookup)
        return_paths.extend(paths)

    return return_paths


def one(dataset):
    path_lookup = to_path_lookup(dataset)
    paths = []
    for v in path_lookup[START]:
        paths.extend(recursive_walk([START, v], path_lookup))

    small_caves = set([k for k in path_lookup if k.islower()])
    visited_all_small = 0
    for path in paths:
        visited = set(path)
        if small_caves.issubset(visited):
            visited_all_small += 1

    return visited_all_small


print(one(actual))
