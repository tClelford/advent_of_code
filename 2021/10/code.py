from functools import reduce

from statistics import median


test_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]

lookup_matching_tag = {")": "(", "]": "[", "}": "{", ">": "<"}
score_lookup = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

pt_2_score_lookup = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

close_lookup = {v: k for k, v in lookup_matching_tag.items()}

opening_tags = set(["(", "[", "{", "<"])


def parse_line(line: str) -> int:
    stack = []
    for c in line.strip():
        if c in opening_tags:
            stack.append(c)
        else:
            last_opened = stack.pop()
            if last_opened == lookup_matching_tag[c]:
                continue
            return score_lookup[c]
    return 0


def fix_line(line):
    stack = []
    for c in line.strip():
        if c in opening_tags:
            stack.append(c)
        else:
            last_opened = stack.pop()
            if last_opened != lookup_matching_tag[c]:
                raise Exception("WTF")
    completion = [pt_2_score_lookup[close_lookup[c]] for c in stack[::-1]]
    return reduce(lambda score, add: score * 5 + add, completion)


def one(test_input=None):
    with open("./10/input.txt") as file:
        lines = file.readlines()
    lines = test_input if test_input else lines

    print(sum([parse_line(line) for line in lines]))


def two(test_input=None):
    with open("./10/input.txt") as file:
        lines = file.readlines()
    lines = test_input if test_input else lines
    need_fixing = [l for l in lines if parse_line(l) == 0]

    return median([fix_line(l) for l in need_fixing])

print(two())
