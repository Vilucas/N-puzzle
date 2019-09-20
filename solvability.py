# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solvability.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 11:59:49 by viclucas          #+#    #+#              #
#    Updated: 2019/09/20 13:29:06 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import copy
import sys
from algorithm import make_goal
import numpy as np


def     from_tuples_to_list(board_init):
    board = []

    for y in range(len(board_init)):
            board += list(board_init[y])
    return board

def     find_zero(state):
    pos = []
    for y in range(state["size"]):
        for x in range(state["size"]):
            if state["board"][y][x] == 0:
                pos = [y, x]
                break
    return pos

def     first_checks(state):
    #board, flag = state['board'], 0
    flag = 0 
    board = list(state['board'])
  
    print(board)

#    if state['size'] < 3 or state['size'] > 5:
#       print("size of the puzzle has to be between 3x3 and 5x5, Exiting ...")
#       sys.exit()
    for i in range(state['size'] * state['size']):
        for y in range(state['size']):
            for x in range(state['size']):
                if board[y][x] == i:
                    flag += 1
        if flag != 1:
            print("Invalid Map, Exiting ...")
            sys.exit()
        flag = 0
    return True

def     complexity_value(state, final_board):
    board = from_tuples_to_list(state['board'])
    final_board = from_tuples_to_list(final_board)
    print(board)
    print(final_board)
    exit()
    i, var = 0, 0
    while i < len(board):
        print(board[i])
        print(final_board[i])
        if board[i] != final_board[i]:
            print(board[i]," - ",final_board[i])
            for x in range(len(final_board)):
                print("---- ", final_board[x], "--",board[i])
                if board[i] == final_board[x]:
                    print("1", board[i])
                    tmp = board[x]
                    board[x] = final_board[x]
                    board[i] = tmp
                    var += 1
                    print("2", board[i])
            i = 0
        else:
            i += 1
        x = 0
    if var % 2 != 0:
        return False
    return True

def     zero_factor(state, final_board):
    zero = state['zero_pos']
    state['board'] = final_board
    final_zero = find_zero(state)
    var = (final_zero[0] - zero[0] + final_zero[1] - zero[1])
    var = abs(var)
    if (var % 2 != 0):
        return False
    return True

def     solvability(state):
    first_checks(state)
    final_board = make_goal(state)
    comp = complexity_value(state, final_board)
    zero = zero_factor(state, final_board)
    if (comp != zero):
        print("Not Solvable Exiting...")
        sys.exit()
        return False
    return True
