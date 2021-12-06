#!/bin/python3.9
"""
Advent of code
Day 4: Bingo

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

# Santise data into a useable format
def santise_data(data:list):
    #numbers = data[0].split(',')
    #numbers = map(int,numbers)
    numbers = data[0].split(',')
    pp.debug(numbers)
    #return
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
            #pp.info(idx)
            if idx == 25:
                boards.append(board)
                board = []
                idx = 0

        #board.extend([[int(x),0] for x in line if x != ''])
    for x in boards:
        pp.info(x)

    return numbers, boards

def total_board_idx(board, idx, increment):
    total = 0
    print(board)
    start=0
    for i in range(5):
        total += board[increment+idx*i][1]
        start += increment
    if total == 5:
        return True


# check if board is a winner
def is_win(board:list):
    win = False
    if total_board_idx(board, 1,5):
        win = True
    if total_board_idx(board, 5,1):
        win = True
    return win


def bingo(numbers,boards):
    #bingo = False
    for value in numbers:
        value = int(value)

        for b_idx, board in enumerate(boards):
            for d_idx, data in enumerate(board):
                #pp.info(data)
                if data[0] == int(value):
                    boards[b_idx][d_idx][1] = 1
        for idx, board in enumerate(boards):
            if is_win(board):
                board_total = 0
                for data in board:
                    if data[1] == 0:
                        board_total += data[0]
                pp.warn(board)
                res = board_total*value
                pp.info("Part 1 solition: " + str(res))
                return
            pp.warn(idx)
        if value == 15:
            return


def score(value:int,board:list):
    board_sum = 0
    print()
    for row in board:
        #pp.info(row)
        for col in row:
            if col[1] == 0:
                board_sum += col[0]
    pp.warn("board sum = " + str(board_sum) + " value = " + str(value))
    pp.info("score is " + str(board_sum * value))

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
        pp.info("Numbers:")
        pp.info(numbers)
        pp.info("Boards:")
        bingo(numbers,boards)
        for i in numbers:
            print(str(i),end=" ")
