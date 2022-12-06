import string
from typing import Tuple, Dict




def gen_scores(s:str, start_from:int)-> Dict[str,int]:


test = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def split_pack(s:str)->Tuple[str,str]:
    midpoint = len(s)//2
    return s[:midpoint], s[midpoint:]

