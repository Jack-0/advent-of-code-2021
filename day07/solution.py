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

def calulate_max_fuel_to_pos(data:list, pos:int, crab_logic:bool=False):
    fuel = 0
    for x in data:
        if not crab_logic:
            fuel += abs(x - pos)
        else:
            base = abs(x - pos)
            crab_fuel = ((base + 1) * base) / 2
            fuel += crab_fuel
    return fuel

def get_least_expensive(data:list, crab_logic:bool=False):
    data_map = Counter(map(int, data))
    fuel_map = defaultdict(int)
    #for value, _ in data_map.items():
    for value in range(max(data)):
        fuel_map[value] = calulate_max_fuel_to_pos(data, value, crab_logic)
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
        res = get_least_expensive(data)
        pp.info("Solution 1: " + str(res))
        res = get_least_expensive(data, crab_logic=True)
        pp.info("Solution 2: " + str(int(res)))
