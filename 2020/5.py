import math


def partition(min: int, max: int, partition: str):
    newval = (min + max)/2
    if partition == "F" or partition == "L":
        return (min, math.floor(newval))
    else:
        return (math.ceil(newval), max)


def search(code: str):
    minrow, maxrow = 0, 127
    mincol, maxcol = 0, 7

    for c in code:
        if c in ["F", "B"]:
            minrow, maxrow = partition(minrow, maxrow, c)
        else:
            mincol, maxcol = partition(mincol, maxcol, c)
    return(maxrow, maxcol)


def get_seat_id(tuple):
    (row, col) = tuple
    return (8*row) + col




def get_max_seat(filename):
    max = 0
    with open(filename, "r") as file:
        for line in file:
            id = get_seat_id(search(line.strip()))
            if id > max:
                max = id
    return max


def get_empty_seats(filename):
    occupied = []
    with open(filename, "r") as file:
        for line in file:
            id = get_seat_id(search(line.strip()))
            occupied.append(id)
    expected = range(0, 864)
    return [value for value in expected if value not in occupied]
        

print(get_empty_seats("./5.txt"))