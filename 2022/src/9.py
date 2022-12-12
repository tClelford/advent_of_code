import numpy as np
from util import read_lines
import sys
lines = read_lines("./2022/data/9.txt")

np.set_printoptions(threshold=sys.maxsize)

test = [
    "R 4",
    "U 4",
    "L 3",
    "D 1",
    "R 4",
    "D 1",
    "L 5",
    "R 2",
]


test2 = [
"R 5",
"U 8",
"L 8",
"D 3",
"R 17",
"D 10",
"L 25",
"U 20",
]

class Knot:
    def __init__(self, parent: "Knot"):
        self.coords = (0, 0)
        self.parent = parent
        self.child = None
        if self.parent:
            self.parent.child = self
        self.visited = set([self.coords])

    def move(self, direction: str):
        if not self.parent:
            x, y = self.coords
            match direction:
                case "L":
                    x -= 1
                case "R":
                    x += 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
            self.coords = (x, y)
        else:
            self.coords = catchup(self.parent.coords, self.coords)
        if self.child:
            self.child.move(direction)

        self.visited.add(self.coords)


def pt_2(input: list):
    head = Knot(None)
    tail = head
    nodes = {0:head}
    for i in range(1,10):
        child = Knot(tail)
        nodes[i]=child


    for move in input:
        direction, distance = move.split()
        distance = int(distance)

        for _ in range(distance):
            head.move(direction)
        
            vis = np.full((15,15), ".")
            node = head
            for n in range(10):
                x,y = node.coords
                vis[y][x] = str(n)
                node = node.child
            print(vis)
            print("-------------------")


    print(len(nodes[9].visited))


def pt_1(input: list):
    head = (0, 0)
    tail = head
    visited = set([head])

    for move in input:
        direction, distance = move.split()
        distance = int(distance)

        for _ in range(distance):
            hx, hy = head
            match direction:
                case "L":
                    hx -= 1
                case "R":
                    hx += 1
                case "U":
                    hy += 1
                case "D":
                    hy -= 1
                case _:
                    raise Exception()
            head = (hx, hy)
            tail = catchup(head, tail)
            visited.add(tail)
            # vis = np.zeros((99, 99))
            # vis[head[1]][head[0]] = 1
            # vis[tail[1]][tail[0]] = 2

            # for row in vis[::-1]:
            #     print(row)
            # print("-------------------")

    print(len(visited))


def catchup(head, tail):
    hx, hy = head
    x, y = tail
    x_offset = hx - x
    y_offset = hy - y

    match (x_offset, y_offset):
        case (1, 2):  # nne
            return x + 1, y + 1
        case (-1, 2):  # nnw
            return x - 1, y + 1
        case (1, -2):  # sse
            return x + 1, y - 1
        case (-1, -2):  # ssw
            return x - 1, y - 1
        case (-2, 1):  # nww
            return x - 1, y + 1
        case (2, 1):  # nee
            return x + 1, y + 1
        case (-2, -1):  # sww
            return x - 1, y - 1
        case (2, -1):  # see
            return x + 1, y - 1
        case (2, 0):  # ww
            return x + 1, y
        case (-2, 0):  # ee:
            return x - 1, y
        case (0, -2):  # ss
            return x, y - 1
        case (0, 2):  # nn
            return x, y + 1
        case _:
            return x, y


# assert catchup((2, 4), (4, 3)) == (3, 4)

pt_2(test2)
