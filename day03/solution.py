#!/bin/python3.9
"""
Advent of code
Day 3: Binary Diagnostic

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

# return sum of 0's and 1's from each column
# given data such as:
# -----
# 0|1|2 <- index
# -----
# 0|1|0 <- first row
# 1|1|1
# 0|1|1
# -----
# generate a 2d array with the format:
# 0[2,1] # column 1 contains: 2 zeros and 1 one
# 1[0,3]
# 2[1,2]
def sum_0_1_via_cols(data:list):
    total_0 = 0
    total_1 = 0
    length = len(data[0])
    index_bit = [[0 for x in range(2)] for y in range(length)]
    pp.info("Line length: " + str(length))
    pp.info("List info: " + str(index_bit))
    for line in data:
        for idx, i in enumerate(line):
            if i == '0':
                index_bit[idx][0] += 1
            else:
                index_bit[idx][1] += 1
    pp.info("Data :" + str(index_bit))
    return index_bit

def index_bits_to_gamma_epsilon(data:list):
    gamma = [None for x in range(len(data))]
    epsilon = [None for x in range(len(data))]
    for idx, i in enumerate(data):
        if i[0] > i[1]:
            gamma[idx] = '0'
            epsilon[idx] = '1'
        elif i[0] < i[1]:
            gamma[idx] = '1'
            epsilon[idx] = '0'
        else:
            pp.warn("Not defined by solution")
    gamma_str = ''.join(gamma)
    epsilon_str = ''.join(epsilon)
    gamma_int = int(gamma_str, 2)
    epsilon_int = int(epsilon_str, 2)
    pp.info("Gamma binary   : " + gamma_str + " = " + str(gamma_int))
    pp.info("Epsilon binary : " + epsilon_str + " = " + str(epsilon_int))
    power = gamma_int * epsilon_int
    pp.warn("Solution (power): "+ str(power))



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
        data = sum_0_1_via_cols(data)
        data = index_bits_to_gamma_epsilon(data)

