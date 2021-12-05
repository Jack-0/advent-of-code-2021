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
    height = len(data[0])
    res = [[0 for x in range(2)] for y in range(height)]
    for line in data:
        for idx, i in enumerate(line):
            if i == '0':
                res[idx][0] += 1
            else:
                res[idx][1] += 1
    return res

def data_into_columnns(data:list):
    width = len(data[0])
    height = len(data)
    res = [[None for x in range(width)] for y in range(height)]
    for i, line in enumerate(data):
        for j, value in enumerate(line):
            res[i][j] = value
    return res

def more_zeros_than_ones(idx:int, lst:list):
    # counts
    zero_count = lst[idx][0]
    one_count = lst[idx][1]
    if zero_count > one_count:
        return True
    return False

def calc_rating(most_common, data, bit_crit):
    other_bit = 0
    if bit_crit == 0:
        other_bit = 1
    res = data.copy()
    while len(res) > 1:
        for line in res:
            for i in range(len(line)):
                if more_zeros_than_ones(i, most_common):
                    res = prune_value_from_data(i, bit_crit, res)
                    most_common = sum_0_1_via_cols(res)
                else:
                    res = prune_value_from_data(i, other_bit, res)
                    most_common = sum_0_1_via_cols(res)

    pp.info("Rating result: " + str(res))
    res = bit_lst_to_int(res[0])
    return res

def prune_value_from_data(idx, value, data:list):
    if len(data) == 1:
        return data
    res = data.copy()
    removed_count = 0
    for ref, line in enumerate(data):
        if int(line[idx]) == int(value):
            res.pop(ref - removed_count)
            removed_count += 1
    return res

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
    power = bit_lst_to_int(gamma) * bit_lst_to_int(epsilon)
    pp.warn("Part 1 Solution (power): "+ str(power))

def bit_lst_to_int(b:list):
    b = ''.join(b)
    return int(b, 2)

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
        most_common = sum_0_1_via_cols(data)
        data = data_into_columnns(data)
        index_bits_to_gamma_epsilon(most_common)
        #calc_oxygen_c02(most_common, data)
        oxygen = calc_rating(most_common, data, 1)
        c02 = calc_rating(most_common, data, 0)
        pp.info("Oxygen: "+str(oxygen))
        pp.info("C02: "+str(c02))
        rating = oxygen * c02
        pp.info("C02 scrubber rating: " + str(rating))

