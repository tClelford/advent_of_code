import math
import statistics
import matplotlib as plt
import pprint


test_data = ["16,1,2,0,4,2,7,1,2,14"]


def get_data(test_data=None):
    with open("./7/input.txt") as file:
        lines = file.readlines()

    lines = test_data if test_data else lines
    line = lines[0]
    return [int(c) for c in line.strip().split(",")]


def part_one():
    data = get_data()
    in_order = sorted(data)

    keys = set(in_order)
    dic = {sum([abs(v - k) for v in in_order]): k for k in keys}
    print(min(dic.keys()))


def part_two():
    data = get_data()
    in_order = sorted(data)
    keys = set(in_order)
    possible_positions = [i for i in range(max(keys) + 1)]

    distance_table = {k: build_distance_table(k, possible_positions) for k in keys}

    results = {
        target_position: sum(
            [distance_table[start][target_position] for start in in_order]
        )
        for target_position in possible_positions
    }

    # for target_position in possible_positions:
    #     results[target_position] = 0
    #     for start_position in in_order:
    #         if target_position not in distance_table[start_position].keys():
    #             distance_table[start_position][target_position] = fuel(
    #                 start_position, target_position
    #             )
    #         results[target_position] += distance_table[start_position][target_position]

    pprint.pprint(results)

    print(min(results.values()))


def build_distance_table(start_point, possible_endpoints):
    return {end: fuel(start_point, end) for end in possible_endpoints}


def fuel(target, value):
    if value == target:
        return 0
    distance = abs(value - target)

    return sum([1 + i for i in range(distance)])
    return (2 ** distance) - 1


# print(fuel(16, 5))
part_two()
