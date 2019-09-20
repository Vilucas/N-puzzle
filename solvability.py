# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solvability.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 11:59:49 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 19:26:38 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import numpy as np
import algorithm as make_goal

def     find_zero(state):
    pos = []
    for y in range(state["size"]):
        for x in range(state["size"]):
            if state["board"][y][x] == 0:
                pos = [y, x]
                break
    return pos

def     first_checks(state):
    board, flag = state['board'], 0
    
    print(board)
    if state['size'] < 3 or state['size'] > 5:
        print("size of the puzzle has to be between 3x3 and 5x5")
        sys.exit()
    for i in range(state['size'] * state['size']):
        for y in range(state['size']):
            for x in range(state['size']):
                if board[y][x] == i:
                    flag += 1
        if flag != 1:
            print("Invalid Map")
            sys.exit()
        flag = 0
    return True

def     complexity_value(state):
    board, flag = state['board'], 0

    for y in range(state['size']):
        for x in range(state['size'] - 1):
            if board[y][x] > board[y][x + 1]:
                    flag += 1
    print(flag)
    var = flag % 2
    return float(var).is_integer()

def     zero_factor(state):
    zero = state['zero_pos']
    state['board'] = make_goal(state)
    final_zero = find_zero(state)
    print(zero + "\n" + final_zero)

def     solvability(state):
    first_checks(state)
    if complexity_value(state) - zero_factor(state) != 0:
        return False
    return True
