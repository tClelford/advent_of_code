from typing import Dict, List
from util import get_lines

test_input = [3, 4, 3, 1, 2]
days = 256


def six_one(input=List[int]):
    dic = input_to_dict(input)
    print(dic)
    for day in range(days):
        dic = turn(dic)
        print(f"DAY {day}: {dic}")

    print(sum(list(dic.values())))


def input_to_dict(input: List[int]) -> Dict:
    max_val = 8
    dic = {}
    for timer in range(max_val + 1):
        dic[timer] = input.count(timer)

    return dic


def turn(dic: Dict) -> Dict:
    out = dict.fromkeys(dic.keys(), 0)
    for k, v in dic.items():
        if k == 0:
            out[8] += v
            out[6] += v
            continue
        out[k-1] += v
    return out





proper_input = [int(i) for i in get_lines("./input_6.txt")[0].strip().split(",")]


six_one(proper_input)
