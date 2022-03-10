
def is_valid_part_1(letter, min, max, password):
    count = password.count(letter)
    return count >= min and count <= max


def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            if line is None:
                continue
            yield to_values(line)

def to_values(line):
    arr = line.split(" ")
    nums = arr[0].split("-")
    min, max = int(nums[0]), int(nums[1])
    letter = arr[1][0]
    password = arr[2].rstrip("\n")
    return (letter, int(min), int(max), password)


examples =map(lambda s: to_values(s),  [
    "1-3 a: abcde",
"1-3 b: cdefg",
"2-9 c: ccccccccc"
])

def do_it(iterable, validator):
    count = 0
    for (letter, min, max, password) in iterable:
        if validator(letter, min, max, password):
            count +=1
    return count

filename = "./2_1.txt"

def is_valid_2(letter, index_1, index_2, password):
    first = password[index_1-1] == letter
    second = password[index_2-1] == letter

    if first and second:
        return False
    if first or second:
        return True
    return False


print(do_it(examples, is_valid_2))

print(do_it(read_file(filename), is_valid_2))