import string
from typing import List, Tuple, Dict
from functools import reduce

from util import read_lines

def gen_scores() -> Dict[str, int]:
    chars = string.ascii_lowercase + string.ascii_uppercase
    return {s: i + 1 for i, s in enumerate(chars)}


SCORE_LOOKUP = gen_scores()

test = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def split_pack(s: str) -> Tuple[str, str]:
    midpoint = len(s) // 2
    return s[:midpoint], s[midpoint:]







def part_two(packs: List[str])->int:
    total, skip, take = 0, 0, 3

    while skip < len(packs):
        subset_matches = None
        subset = packs[skip: skip+take]
        # print(subset)
        for pack in subset:
            if not subset_matches:
                subset_matches = set(pack)
            subset_matches.intersection_update(pack)
        # print(subset_matches)
        total += reduce(lambda total, char: total + SCORE_LOOKUP[char], list(subset_matches), 0)
        skip += take
    return total



def reducer(total: int, pack: str) -> int:
    first, second = split_pack(pack)
    matches = set(first).intersection(second)
    return total + reduce(lambda total, match: total + SCORE_LOOKUP[match], matches, 0)



print(part_two(test))
print(part_two(read_lines("./data/three.txt")))


# print(process_packs(test[0:1]))
