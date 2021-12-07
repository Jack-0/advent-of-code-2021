#!/bin/python3.9
"""
Advent of code
Day 5: Hydothermal Venture
"""

import sys
sys.path.append('..') # add parent dir to path (for tools import)
from tools.prettyprint import PrettyPrint

pp = PrettyPrint()

# turn a file into a list
def file_to_list(file_path:str):
    a = []
    b = []
    with open(file_path) as f:
        for line in f:
            tmp_a, tmp_b = line.split("->")
            a.append(single_csv_str_to_list(tmp_a))
            b.append(single_csv_str_to_list(tmp_b))
    for i in range(len(a)):
        pp.debug(str(a[i]) + " " + str(b[i]))
    return a, b

def single_csv_str_to_list(data:list):
    data = data.split(",")
    data[0] = int(data[0])
    data[1] = int(data[1])
    return data

def min_max_data(data):
    max_x = data[0][0]
    max_y = data[0][1]
    min_x = data[0][0]
    min_y = data[0][1]
    for x, y in data:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)
    return min_x, min_y, max_x, max_y

def min_max_xy(a,b):
    min_ax, min_ay, max_ax, max_ay = min_max_data(a)
    min_bx, min_by, max_bx, max_by = min_max_data(b)
    min_x = min(min_ax,min_bx)
    min_y = min(min_ay,min_by)
    max_x = max(max_ax,max_bx)
    max_y = max(max_ay,max_by)
    return min_x, min_y, max_x, max_y

def populate_grid(a,b,grid):
    for i in range(len(a)):
        ax = a[i][0]
        bx = b[i][0]
        ay = a[i][1]
        by = b[i][1]
        pp.info(str(i)+": "+str(ax)+","+str(ay)+" "+str(bx)+","+str(by))
        if ax == bx:
            pp.warn("drawing vert")
            # draw vertical
            for j in range(min(ay,by),max(ay,by)+1):
                grid[j][ax] += 1
        if ay == by:
            pp.warn("drawing hori")
            # draw horizontal
            for j in range(min(ax,bx),max(ax,bx)+1):
                grid[ay][j] += 1

    for line in grid:
        pp.info(line)
    return grid

def check_for_overlap(grid):
    total = 0
    width = len(grid)
    height = len(grid[0])
    for i in range(width):
        for j in range(height):
            if grid[i][j] > 1:
                total += 1
    return total

if __name__ == "__main__":
    # check the passed arguments are correct
    if len(sys.argv) == 1:
        raise Exception(str(sys.argv[0]) + " expected more arguments")

    # for all given files
    input_files = sys.argv[1:]
    for input_file in input_files:
        # read input file and get count
        pp.warn("File: " + input_file)
        a, b = file_to_list(input_file)
        # generate grid of size min max x and y
        min_x, min_y, max_x, max_y = min_max_xy(a,b)
        pp.info("Min xy: " + str(min_x) + "," + str(min_y))
        pp.info("Max xy: " + str(max_x) + "," + str(max_y))
        max_x += 1
        max_y += 1
        #grid = [[0 for x in range(min_x, max_x)] for y in range(min_y, max_y)]
        grid = [[0 for x in range(max_x)] for y in range(max_y)]
        grid = populate_grid(a,b,grid)
        total = check_for_overlap(grid)
        pp.info("Solution 1: " + str(total))
