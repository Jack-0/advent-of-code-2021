#!/bin/python3.9
"""
Advent of code
Day 6: Lanternfish
"""

import sys
sys.path.append('..') # add parent dir to path (for tools import)
from tools.prettyprint import PrettyPrint
import math
pp = PrettyPrint()

# turn a file into a list
def file_to_list(file_path:str) -> list:
    b = []
    with open(file_path) as f:
        data = [list(map(int, line.strip().split(','))) for line in f]
    return data[0]

def lanternfish(iterations:int, data:list):
    for i in range(iterations):
        progress = "Progress [" + str(i) + "/" + str(iterations) + "]"
        print(progress,end="\r")
        data = modify_count(data)
    return data

def modify_count(data:list):
    idx_offset = 0
    for idx, value in enumerate(data):
        if value == 0:
            # reset the fishes spawn counter if it hits '0'
            data[idx] = 6
            idx_offset += 1
        else:
            data[idx] -= 1
    # append the new spawns of fish
    for i in range(idx_offset):
        # TODO could we append this in the spawn statment code?
        data.append(8)
    return data



if __name__ == "__main__":
    # check the passed arguments are correct
    if len(sys.argv) == 1:
        raise Exception(str(sys.argv[0]) + " expected more arguments")

    # for all given files
    input_files = sys.argv[1:]
    for input_file in input_files:
        # read input file 
        pp.warn("File: " + input_file)
        data = file_to_list(input_file)
        data = lanternfish(80, data)
        pp.warn("Solution part 1: " + str(len(data)))
        data = lanternfish(256, data)
        pp.warn("Solution part 2: " + str(len(data)))

