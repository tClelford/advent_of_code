import functools 



example = [
    "..##.........##.........##.........##.........##.........##.......",
    "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
    ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
    "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
    ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
    "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
    ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
    ".#........#.#........#.#........#.#........#.#........#.#........#",
    "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
    "#...##....##...##....##...##....##...##....##...##....##...##....#",
    ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"
]

class TreeCounter:
    def __init__(self, x_move, y_move):
        self.x_move = x_move
        self.y_move = y_move
        self.count = 0
        self.x = 0
        self.next_y = 0
    
    def parse_line(self, line, y):
        if y != self.next_y:
            return
        max_x = len(line.strip())
        if self.x >= max_x:
            self.x = self.x - max_x
        if line[self.x] == "#":
            self.count +=1
        self.x += self.x_move
        self.next_y += self.y_move
        return

    def get_count(self):
        return self.count
    def to_string(self):
        return f"{self.x_move}, {self.y_move}"


def get_trees(pattern, counters):
    for y, line in enumerate(pattern):
        for c in counters:
            c.parse_line(line, y)
    return functools.reduce(lambda val, prev: val * prev, map(lambda counter: counter.count, counters), 1)
        


day1 = [TreeCounter(3, 1)]
day2 = [TreeCounter(1,1),TreeCounter(3, 1), TreeCounter(5,1), TreeCounter(7, 1), TreeCounter(1, 2)]

# print(get_trees(example, day2))

with open("./3_1.txt", "r") as file:
    lines = file.readlines()
    print(get_trees(lines, day2))




