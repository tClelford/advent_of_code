from typing import Dict, FrozenSet, Iterable, List, Set, Tuple


UNKNOWN_TOKEN = "z"


class ProblemInput:
    def __init__(self, input_string: str) -> None:
        input, output = input_string.strip().split("|")
        self.out_display = [to_display_digit(digit) for digit in output.split()]
        all_digits = [to_display_digit(digit) for digit in input.split()]
        all_digits.extend(self.out_display)
        self.lookup = {k: -1 for k in set(all_digits)}

    def take_a_stab(self):
        known_digits = {v: k for k, v in self.lookup.items() if v != -1}
        for k, v in self.lookup.items():
            if v != -1:
                continue
            value = get_digit_value(k, known_digits)
            if value == -1:
                continue
            self.lookup[k] = value
            known_digits[value] = k

    def get_out_value(self):
        for i in range(3):
            self.take_a_stab()

        val = 0
        mult = 1000
        for display in self.out_display:
            digit = self.lookup[display]
            val += mult * digit
            mult /= 10
        return val


def get_digit_value(
    digit: FrozenSet[str], known_digits: Dict[int, FrozenSet[str]]
) -> int:
    l = len(digit)
    if l == 2:
        return 1
    if l == 3:
        return 7
    if l == 4:
        return 4
    if l == 7:
        return 8

    if l == 6:
        return nine_six_or_zero(digit, known_digits)

    return two_three_or_five(digit, known_digits)


def to_display_digit(string: str) -> FrozenSet:
    return frozenset(list(string.strip()))


def get_input(test_input=None)-> Iterable[str]:
    with open("./8/input.txt") as file:
        lines = file.readlines()

    if test_input:
        lines = test_input
    return lines


def to_digits(string: str):
    return string.strip().split(" ")


lookup = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 1}


def first():
    count = 0
    displays = get_input()
    for display in displays:
        out = display[1]
        for digit in out:
            count += lookup[len(digit)]

    print(count)


def second(test_input=None):
    inputs = get_input(test_input)
    total = 0
    for input in inputs:
        problem = ProblemInput(input)
        result = problem.get_out_value()
        total += result
    print(total)



def nine_six_or_zero(
    digit: FrozenSet[str], known_digits: Dict[int, FrozenSet[str]]
) -> int:
    key = 1 if 1 in known_digits else 7 if 7 in known_digits else -1
    if key == -1:
        return -1

    if not known_digits[key].issubset(digit):
        return 6

    if not 3 in known_digits:
        return -1

    return 9 if known_digits[3].issubset(digit) else 0


def two_three_or_five(
    digit: FrozenSet[str], known_digits: Dict[int, FrozenSet[str]]
) -> int:
    key = 1 if 1 in known_digits else 7 if 7 in known_digits else -1
    if key == -1:
        return -1

    if known_digits[key].issubset(digit):
        return 3

    if 1 not in known_digits or 4 not in known_digits:
        return -1

    subset = known_digits[4].difference(known_digits[1])
    if subset.issubset(digit):
        return 5

    return 2


def three_or_nine(
    digit: FrozenSet[str], known_digits: Dict[int, FrozenSet[str]]
) -> int:
    if 9 in known_digits and digit != known_digits[9]:
        return 3
    if 7 not in known_digits or 4 not in known_digits:
        return -1

    nine = set.union(set(known_digits[7]), set(known_digits[4]))
    if digit == frozenset(nine):
        return 9

    return -1


test_input = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",  # 8394
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",  # 9781
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",  # 1197
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
]  # 61229

# fdgacbe cefdb cefbgd gcbe: 8394
# fcgedb cgb dgebacf gc: 9781
# cg cg fdcagb cbg: 1197
# efabcd cedba gadfec cb: 9361
# gecf egdcabf bgf bfgea: 4873
# gebdcfa ecba ca fadegcb: 8418
# cefg dcbef fcge gbcadfe: 4548
# ed bcgafe cdgba cbgef: 1625
# gbdfcae bgc cg cgb: 8717
# fgae cfgab fg bagce: 4315


# print(get_digits(test_example))

second()
# test = ProblemInput(test_input[0])
# print(test.get_out_value())


# print(to_display_digit("fdgacbe"))
