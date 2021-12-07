#!/bin/python3.9
"""
Advent of code
Day 4: Bingo
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

# Santise data into a useable format
def santise_data(data:list):
    numbers = data[0].split(',')
    boards = []
    board = []
    idx = 0
    for line in data[2:]:
        line = line.strip('\n').split(' ')
        for i in line:
            try:
                board.append([int(i),0])
                idx += 1
            except:
                pass
            if idx == 25:
                boards.append(board)
                board = []
                idx = 0
    return numbers, boards

# for a given 5 rows or columns find out if 
# the total is 5 thus marking a winner
# incr_row and incr_col are offsets
def find_completed(board, incr_row, incr_col):
    total = 0
    start = 0
    idx = 0
    for i in range(5):
        idx = (i * incr_row)
        total = 0
        for j in range(5):
            total += board[idx][1]
            idx += incr_col
        if total == 5:
            return True
    return False

# check if board is a winner
def is_win(board:list):
    # return completed row or completed col results
    return find_completed(board, 1, 5) or find_completed(board, 5 , 1)

def bingo(numbers,boards):
    total_boards = len(boards)
    completed_boards = []
    part_1_res = True
    for value in numbers:
        value = int(value)
        for b_idx, board in enumerate(boards):
            for d_idx, data in enumerate(board):
                if data[0] == int(value):
                    boards[b_idx][d_idx][1] = 1
        for idx, board in enumerate(boards):
            #pp.debug(board)
            if is_win(board):
                # part2
                if idx not in completed_boards:
                    completed_boards.append(idx)
                if len(completed_boards) == total_boards:
                    res = score(value, board)
                    pp.info("Part 2 solution: " + str(res))
                    return
                # part 1
                if part_1_res:
                    res = score(value, board)
                    pp.info("Part 1 solution: " + str(res))
                    part_1_res = False


def score(value:int,board:list):
    board_total = 0
    for data in board:
        if data[1] == 0:
            board_total += data[0]
    return board_total * value

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
        numbers, boards = santise_data(data)
        bingo(numbers,boards)
