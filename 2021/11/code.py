import numpy as np

input = [
    "2138862165",
    "2726378448",
    "3235172758",
    "6281242643",
    "4256223158",
    "1112268142",
    "1162836182",
    "1543525861",
    "1882656326",
    "8844263151",
]

test_input = [
    "5483143223",
    "2745854711",
    "5264556173",
    "6141336146",
    "6357385478",
    "4167524645",
    "2176841721",
    "6882881134",
    "4846848554",
    "5283751526",
]

noddy_input = [
    "11111",
    "19991",
    "19191",
    "19991",
    "11111",
]


def grid(string_input):
    return np.array([np.array([int(c) for c in s.strip()]) for s in string_input])


def boost_neighbours(x: int, y: int, board):
    is_top_row = y == 0
    is_bottom_row = y == board.shape[1] - 1
    is_far_left = x == 0
    is_far_right = x == board.shape[0] - 1

    if not is_top_row:
        board[x, y - 1] += 1
        if not is_far_left:
            board[x - 1, y - 1] += 1
        if not is_far_right:
            board[x + 1, y - 1] += 1

    if not is_far_right:
        board[x + 1, y] += 1
    if not is_far_left:
        board[x - 1, y] += 1

    if not is_bottom_row:
        board[x, y + 1] += 1
        if not is_far_left:
            board[x - 1, y + 1] += 1
        if not is_far_right:
            board[x + 1, y + 1] += 1

    return board


def recursive_flash(grid, not_flashed_before=None):
    if not_flashed_before is None:
        not_flashed_before = np.full(grid.shape, 1)
    this_round = grid * not_flashed_before > 9

    if sum(sum(this_round)) == 0:
        return grid

    not_flashed_before = grid <= 9

    for (x, y), val in np.ndenumerate(this_round):
        if not val:
            continue
        grid = boost_neighbours(x, y, grid)

    return recursive_flash(grid, not_flashed_before)


def mask(grid, mask1, mask2):
    combined = np.bitwise_or(mask1, mask2)
    print(combined)
    return grid * np.invert(np.ndarray(combined, dtype=bool))


def steps(grid, n):
    count = 0
    print("INITIAL STATE:")
    print(grid)
    for step in range(n):
        print("#######################")
        grid = grid + 1
        recursive_flash(grid)
        flashes = get_count(grid)
        count += flashes
        if flashes == grid.shape[0] ** 2:
            print(grid)
            return step + 1
        grid = tidy_up(grid)
        print(f"STEP {step+1}:")
        print(grid)
    print("#######################")
    print("#######################")
    print("#######################")
    return count


def tidy_up(grid):
    mask = grid <= 9
    g = grid * mask
    return g


def get_count(grid) -> int:
    return sum(sum(grid > 9))


def one():
    print(steps(grid(input), 1000))


g = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
m1 = [[0, 0, 0], [1, 0, 0], [0, 0, 0]]
m2 = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]


test_coords = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

# boost_ne(2, 2, test_coords)

# recursive_flash(grid())
one()
