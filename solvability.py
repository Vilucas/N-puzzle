# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solvability.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 11:59:49 by viclucas          #+#    #+#              #
#    Updated: 2019/09/23 21:39:00 by jcruz-y-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

#   Checking doublon and if the map is a square
def     first_checks(state):
    flag = 0 
    board = list(state['board'])
    if state['size'] < 3 or state['size'] > 10:
        print("size of the puzzle has to be between 3x3 and 10x10, Exiting ...")
        sys.exit()
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

#   Calcul of the number of transposition we have to do to resolve the game
#   Return True if even, False if odd
def     complexity_value(state, final_board):
    board = from_tuples_to_list(state['board'])
    final_board = from_tuples_to_list(final_board)
    i, var = 0, 0
    while i < len(board):
        if board[i] != final_board[i]:
            for x in range(len(final_board)):
                if board[i] == final_board[x]:
                    tmp = board[x]
                    board[x] = final_board[x]
                    board[i] = tmp
                    var += 1
            i = 0
        else:
            i += 1
        x = 0
    if var % 2 != 0:
        return False
    return True

#   Calcul the distance between 0 and his final destination one square cost 1
#   Return True if even, False if odd
def     zero_factor(state, final_board):
    zero = state['zero_pos']
    state['board'] = final_board
    final_zero = find_zero(state)
    var = (final_zero[0] - zero[0] + final_zero[1] - zero[1])
    if (abs(var) % 2 != 0):
        return False
    return True

#   If the distance between Zero (the empty square) toward his final destination and
#   the number of transposition we have to do to resolve the game are both even or 
#   odd numbers then the puzzle is resolvable otherwise its not
def     solvability(state):
    first_checks(state)
    final_board = make_goal(state)
    comp = complexity_value(state, final_board)
    zero = zero_factor(state, final_board)
    if (comp != zero):
        print("Not Solvable Exiting...")
        sys.exit()
