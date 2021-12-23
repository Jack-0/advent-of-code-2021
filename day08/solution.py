#!/bin/python3.9
"""
Advent of code
Day 8: Seven Segment Search
"""

import sys
sys.path.append('..') # add parent dir to path (for tools import)
from tools.prettyprint import PrettyPrint
import math
pp = PrettyPrint()

from collections import Counter, defaultdict

# turn a file into a list
def file_to_list(file_path:str) -> list:
    with open(file_path) as f:
        data = f.read().splitlines()
    return data

# seven segment display
# 4 * 2
# 3 * 4

#  -
# | |
#  -
# | |
#  _

# 1 has 2 segments
# 4 has 4
# 7 has 3
# 8 has 7

# issues can arise with duplicates as... 
# 2 has 5
# 3 has 5
# 5 has 5
# 6 has 6 
# 9 has 6
def count_digits_after_token(token, data):
    count = 0
    for line in data:
        end = line.split(token)[1]
        for value in end.split():
            l = len(value)
            print(value)
            print(str(l))
            if l == 2:
                count += 1
            elif l == 4:
                count += 1
            elif l == 3:
                count += 1
            elif l == 7:
                count += 1
    pp.warn(count)
    return count


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
        print(data)
        pp.warn("line 3")
        pp.info(data[2])
        res = count_digits_after_token('|', data)

