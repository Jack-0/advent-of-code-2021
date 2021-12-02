#!/bin/python3.9
"""
Advent of code
Day 2: Dive!

This program requires a file of integers seperated by new lines as an input.
"""

import sys
sys.path.append('..') # add parent dir to path (for tools import)
from tools.prettyprint import PrettyPrint

pp = PrettyPrint()

# turn a file into a list
def file_to_list(file_path:str):
    with open(file_path) as f:
        data = f.read().splitlines()
    return data

# given a list that conatins <str> <int>
# some words alter values:
#   "down" 
#       increases aim by x units
#   "up" 
#       decrease aim by x units
#   "forward" 
#       increase horizontal by x units
#       increase depth by aim multiplied by x
def aim(data:list):
    aim = 0
    dumb_depth = 0 #for part one only
    depth = 0
    horizontal = 0
    word_count_dict = {}
    for line in data:
        word = line.split()[0]
        value = int(line.split()[1])
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict[word] + value
        else:
            word_count_dict[word] = value

        if word == "down":
            dumb_depth += value
            aim += value
        elif word == "up":
            aim -= value
            dumb_depth -= value
        elif word == "forward":
            horizontal += value
            depth += aim * value

    pp.info("part 1 answer:" + str(horizontal * dumb_depth))
    pp.info("part 2 answer:" + str(horizontal * depth))

if __name__ == "__main__":
    # check the passed arguments are correct
    if len(sys.argv) == 1:
        raise Exception(str(sys.argv[0]) + " expected more arguments")

    # for all given files
    input_files = sys.argv[1:]
    for input_file in input_files:
        # read input file and get count
        pp.warn("File: " + input_file)
        data = file_to_list(input_file)
        aim(data)
