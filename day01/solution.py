#!/bin/python3.9
"""
Advent of code
Day 1: Sonar Sweep

This program requires a file of integers seperated by new lines as an input.
"""

import sys
sys.path.append('..') # add parent dir to path (for tools import)
from tools.prettyprint import PrettyPrint

pp = PrettyPrint()

# turn a file into a list of integers
def file_to_int_list(file_path:str):
    with open(file_path) as f:
        data = f.read().splitlines()
    data = list(map(int, data))
    return data

# performs a sliding window count of 
# window_size on a given list of data
def sliding_window_count(window_size:int,data:list):
    res = []
    for idx, value in enumerate(data):
        # ignore any windows that go out of bounds
        if idx + window_size > len(data):
            pass
        # sum up values for the given window size and append
        else:
            tmp = 0
            for i in range(0,window_size):
                tmp += data[idx + i]
            res.append(tmp)
    return count_increases(res)

def count_increases(data:list):
    # count the number of the current value is greater
    # than the previous value
    previous_value = None
    count = 0
    for value in data:
        value = int(value)
        if previous_value == None:
            pass
        elif value > previous_value:
            count += 1
            previous_value = value
        previous_value = value
    return count

if __name__ == "__main__":
    # check the passed arguments are correct
    if len(sys.argv) == 1:
        raise Exception(str(sys.argv[0]) + " expected more arguments")

    # for all given files
    input_files = sys.argv[1:]
    for input_file in input_files:
        # read input file and get count
        pp.warn("File: " + input_file)
        data = file_to_int_list(input_file)
        # count data
        res = count_increases(data)
        pp.info("Count result: " + str(res))
        # sliding window of 3
        res = sliding_window_count(3, data)
        pp.info("Sliding window result: " + str(res))
