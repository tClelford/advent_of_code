import logging
from typing import List
from collections import deque
from util import read_lines

lines = read_lines("./2022/data/seven.txt")


from dataclasses import dataclass


from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int


class Dir:
    def __init__(self, parent, name):
        self.name = name
        self.files = []
        self.dirs = {}
        self.parent = parent
        self.__size__ = None

    def process_line(self, line: str):
        self.__size__ = None
        prop, name = line.split()
        if prop == "dir":
            if name not in self.dirs:
                self.dirs[name] = Dir(self, name)
        else:
            self.files.append(File(name, size=int(prop)))

    def size(self)->int:
        if self.__size__:
            return self.__size__
        self.__size__ = 0
        for file in self.files:
            self.__size__ += file.size

        for dir in self.dirs.values():
            self.__size__ += dir.size()
        return self.__size__    

    def cd(self, path: str):
        if path == self.name:
            return self
        if path == "..":
            if not self.parent:
                return self
            return self.parent
        if path not in self.dirs:
            self.dirs[path] = Dir(self, path)

        return self.dirs[path]

    def get_path(self):
        if self.parent is None:
            return self.name
        return self.parent.get_path() + "/" + self.name
    
    def size_at_or_below_threshold(self, threshold:int)-> int: 
        total = 0
        for child in self.dirs.values():
            size = child.size()
            if size <= threshold:
                total +=size
        
        self_size = self.size()
        if self_size <= threshold:
            total+=size
        
        return total



def attempt_two(input:str, threshold=100000):
    root = Dir(parent=None, name="/")
    cwd = root
    for i, line in enumerate(input):
        print(i, line)
        if line[0] == "$":
            cleaned = line[2:]
            if cleaned[0:2] == "ls":
                continue
            cwd = cwd.cd(cleaned[3:])
            print(f"cwd path is now {cwd.get_path()}" )
        else:
            cwd.process_line(line)
    

    total = root.size_at_or_below_threshold(threshold)
    print(total)


    # def add_file(self, line: str):
    #     size, name = line.split(" ")
    #     size = int(size)
    #     self.files.append(File(name, size))

    # def add_dir(self, dir):
    #     self.size += dir.size
    #     self.dirs.append((dir.name, dir.size))


test = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]

# need to actually model file structure.


# class FileTree:
#     def __init__(self):
#         root = Dir("/")
#         self.stack = [root]
#         self.dirs = []
#         self.seen_dir_names = []

#     def process_command(self, line: str):
#         cleaned = line[2:]
#         if cleaned[0:2] == "ls":
#             return
#         self.cd(cleaned[3:])

#     def cd(self, target: str):
#         if target in self.seen_dir_names:
#             print(target)

#         self.seen_dir_names.append(target)

#         current_dir = self.cwd().name
#         if current_dir == target:
#             return

#         if current_dir == "/" and target == "..":
#             return

#         if target == "..":
#             popped = self.stack.pop()
#             self.cwd().add_dir(popped)
#             self.dirs.append(popped)
#             return

#         self.stack.append(Dir(target))

#     def process_dir_contents(self, line: str):
#         if line[:3] != "dir":
#             self.cwd().add_file(line)

#     def cwd(self):
#         return self.stack[-1]

#     def process_line(self, line: str):
#         if line[0] == "$":
#             self.process_command(line)
#             return
#         self.process_dir_contents(line)

#     def finalise(self):
#         while self.cwd().name != "/":
#             self.cd("..")
#         self.dirs.append(self.cwd())

#     def get_sum_under(self, threshold: int) -> int:
#         return sum([d.size for d in self.dirs if d.size <= threshold])


def main():
    attempt_two(lines)
   


if __name__ == "__main__":
    main()
