from util import read_lines




def load_input() -> str:
    return read_lines("./data/six.txt")[0]


def sliding_window(input:str, window_size:int)-> int:
    start=0
    end=window_size

    while end < len(input):
        subs=input[start:end]
        if len(set(subs)) == window_size:
            return end
        start+=1
        end+=1

test_strs=[
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

test_strs_2=[
"mjqjpqmgbljsphdztnvjfqwrcgsmlb", #: first marker after character 19
"bvwbjplbgvbhsrlpgdmjqwftvncz", #: first marker after character 23
"nppdvjthqldpwncqszvftbrmjlhg", #: first marker after character 23
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", #: first marker after character 29
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", #: first marker after character 26
]


for s in test_strs_2:
    print(sliding_window(s, 14))


print(sliding_window(load_input(), 14))
