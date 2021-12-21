#!/bin/python3.9
"""
Advent of code
Day 7: The Treachery of Whales
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

def mean(data:list):
    return sum(data) / len(data)

def mode(data:list):
    return max(data, key=data.count)

def calulate_max_fuel_to_pos(data:list, pos:int):
    fuel = 0
    for x in data:
        fuel += abs(x - pos)
    return fuel

def get_least_expensive(data:list):
    data_map = Counter(map(int, data))
    fuel_map = defaultdict(int)
    for value, _ in data_map.items():
        fuel_map[value] = calulate_max_fuel_to_pos(data, value)
    min_pos = min(fuel_map, key=fuel_map.get)
    return fuel_map[min_pos]


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
        data_mean = mean(data)
        data_mode = mode(data)
        pp.warn("mean: " + str(data_mean))
        pp.warn("mode: " + str(data_mode))
        res = get_least_expensive(data)
        pp.warn("Solution 1: " + str(res))
