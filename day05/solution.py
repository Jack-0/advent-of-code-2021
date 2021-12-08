#!/bin/python3.9
"""
Advent of code
Day 5: Hydothermal Venture
"""

import sys
sys.path.append('..') # add parent dir to path (for tools import)
from tools.prettyprint import PrettyPrint
import math
pp = PrettyPrint()

# turn a file into a list
# x1, y1, x2, y2
def file_to_list(file_path:str) -> list:
    b = []
    with open(file_path) as f:
        data = [list(map(int, line.strip().replace('->',',').split(','))) for line in f]
    return data

# get max len for data lengths
def xy_len(data):
    x_len = max(max([(c[0], c[2])for c in data])) + 1
    y_len = max(max([(c[1], c[3])for c in data])) + 1
    return x_len, y_len

# append 1 to a grid for each 'line'
# sum grid to return crossover total
def calc_crossover(data, grid, diagonal=False):
    pp.warn(len(data))
    for x1, y1, x2, y2 in data:
        # find x y starting pos and delta
        xmin = min(x1, x2)
        ymin = min(y1, y2)
        delta_x = abs(x2 - x1)+1 # add one to account of offset
        delta_y = abs(y2 - y1)+1
        # draw vertical
        if x1 == x2:
            for i in range(delta_y):
                grid[ymin + i][x1] += 1
        # draw horizontal
        elif y1 == y2:
            for i in range(delta_x):
                grid[y1][xmin + i] += 1
        # draw diagonal
        elif diagonal:
            # fortunately the data is so that if it's not horizonatal
            # or vertical entry, it's a 45 degree line
            x_pos = -1
            y_pos = -1
            # find diagonal direction
            if x2 > x1:
                x_pos = 1
            if y2 > y1:
                y_pos = 1
            # draw 45 degree line based of direction
            for i in range( delta_x):
                grid[(y_pos * i) + y1][(x_pos * i) + x1] += 1
    # sum total
    total = 0
    for i in grid:
        for res in i:
            if res > 1:
                total+=1
    return total


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
        x_len, y_len = xy_len(data)
        # create grid
        grid = [[0 for i in range(x_len)] for j in range(y_len)]
        solution_1 = calc_crossover(data, grid)
        grid = [[0 for i in range(x_len)] for j in range(y_len)]
        solution_2 = calc_crossover(data, grid, diagonal=True)
        pp.info("Solution 1: " + str(solution_1))
        pp.info("Solution 2: " + str(solution_2))
