#!/bin/python3.9
"""
Advent of code
Day 1: Sonar Sweep

This program requires a file of integers seperated by new lines as an input.
"""

import sys
sys.path.append('..') # add parent dir to path (for tools import)
from tools.prettyprint import PrettyPrint

EXPECTED_INPUT = 2  # script expects day01.py as a input
                    # and a file, thus 2 args

pp = PrettyPrint()

if __name__ == "__main__":
    # check the passed arguments are correct
    if len(sys.argv) != EXPECTED_INPUT:
        raise Exception("Expected " + str(EXPECTED_INPUT)+\
                        " arguments, but recieved " + str(len(sys.argv)))
    # read input file
    input_file = sys.argv[1]
    pp.info("input file is \'" + input_file + "\'")
    data = None
    with open(input_file) as f:
        data = f.read().splitlines()
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
    # print answer
    pp.info("count: " + str(count))
