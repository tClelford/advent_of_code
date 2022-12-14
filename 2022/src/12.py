import string
from util import read_lines


test = [
"Sabqponm",
"abcryxxl",
"accszExk",
"acctuvwj",
"abdefghi",
]

heights={
    c:i for i, c in enumerate(string.ascii_lowercase)
}
heights["S"]=0
heights["E"]=0

