import sys
from typing import Dict, List, Tuple
from pydantic import BaseModel


def read_lines(path: str, clean: bool = True) -> List[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if clean:
        lines = [s.strip() for s in lines]

    return lines


test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

possibe_dict = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class Turn:
    def __init__(self, input: str):
        draws = input.split(",")
        self.balls = {}
        for draw in draws:
            n, k = draw.replace(",", "").replace(";", "").strip().split(" ")
            val = self.balls.get(k, 0)
            self.balls[k] = val + int(n)

    def is_possible(self, possible: Dict[str, int]):
        for k, v in self.balls.items():
            if k not in possible:
                return False
            if possible[k] < v:
                return False
        return True


def parse_game_to_turns(game: str) -> Tuple[int, List[Turn]]:
    title, turn_strs = game.split(":")
    turns = [Turn(t) for t in turn_strs.split(";")]
    return int(title.split(" ")[1]), turns


def part_1(data: List[str]):
    answer = 0
    for game in data:
        possible = True
        i, turns = parse_game_to_turns(game)
        print("game", i)
        for turn in turns:
            if not possible:
                continue
            print(turn.balls)
            if not turn.is_possible(possibe_dict):
                print("not possible")
                possible = False
        if possible:
            answer += i
        print("-------")
    print(f"Part 1: {answer}")


def part_2(data: List[str]):
    answer = 0
    for game in data:
        mins = {}
        i, turns = parse_game_to_turns(game)
        print("game", i)
        for turn in turns:
            for k, v in turn.balls.items():
                mins[k] = max(mins.get(k, 0), v)
        power = 1
        for k, v in mins.items():
            power *= v
        answer += power

    print(f"Part 2: {answer}")


def main():
    if len(sys.argv) > 1:
        data = read_lines(sys.argv[1])
    else:
        data = test_data

    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()
