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
# return the sum of ints for each unique <str>
def sum_for_each_str(data:list):
    word_count_dict = {}
    for line in data:
        word = line.split()[0]
        value = int(line.split()[1])
        if word in word_count_dict.keys():
            word_count_dict[word] = word_count_dict[word] + value
        else:
            word_count_dict[word] = value
    return word_count_dict

def product_of_depth_and_horizontal(data: list):
    forward = data['forward']
    down = data['down']
    up = data['up']
    horizontal = forward
    depth = down - up
    return depth * horizontal


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
        # sum of each str
        data = sum_for_each_str(data)
        pp.info("Data: " + str(data))
        # product of depth and horizontal pos
        res = product_of_depth_and_horizontal(data)
        pp.info("Result: " + str(res))
