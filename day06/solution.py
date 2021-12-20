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

from collections import Counter, defaultdict

# turn a file into a list
def file_to_list(file_path:str) -> list:
    b = []
    with open(file_path) as f:
        data = [list(map(int, line.strip().split(','))) for line in f]
    return data[0]

def lanternfish(iterations:int, data:list):
    # use Counter to get the number of fish at a given stage
    data_map = Counter(map(int, data))
    pp.debug(data_map)

    for _ in range(iterations):
        new_map = defaultdict(int)
        for fish_status, total in data_map.items():
            if fish_status == 0:
                # increase the reset counter '6'
                new_map[6] += total
                # increase the new fish counter '8'
                new_map[8] += total
                # note values are equal to num as if there are x fish in 
                # stage zero, x fish reset to the value 6 and x fish are
                # spawned into fish_status 8
            else:
                # every fish below the current status is incremented
                # by one according to the fish spawning rules
                new_map[fish_status-1] += total
        data_map = new_map
    return sum(new_map.values())


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
        res = lanternfish(80, data)
        pp.warn("Solution part 1: " + str(res))
        res = lanternfish(256, data)
        pp.warn("Solution part 2: " + str(res))

