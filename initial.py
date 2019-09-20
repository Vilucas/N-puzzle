# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    initial.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:01:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 19:22:44 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import heapq
import numpy as np
import math

from solvability import solvability 
from generator import make_goal, make_puzzle


def     init_board(board_str):
    index, x1, y = 0, 0, 0
    board_arr = board_str.split(", ")
    arrlength = len(board_arr)
    size = int(math.sqrt(arrlength))
    x = np.arange(arrlength)
    x = x.reshape(size, size)
    board = np.empty_like(x)
    while index < arrlength:
        board[y][x1] = board_arr[index]
        x1 += 1
        index += 1
        if (x1 == size):
            x1 = 0
            y += 1
    print("BOARD\n", board)
    return tuple(map(tuple, board)), size

def     find_zero(state):

    for y in range(state["size"]):
        for x in range(state["size"]):
            if state["board"][y][x] == 0:
                pos = [y, x]
                break
    return pos

def     init_state(board_arr):
    state = {}
    state['board'], state['size'] = init_board(board_arr)
    state['moves'] = ((1, 0), (0, 1), (-1, 0), (0, -1))
    state['zero_pos'] = find_zero(state)
    return state

def     get_input():
    li = []
    print("Choose an Algorithm :")
    print("1- A*")
    print("2- Dijkstra's algorithm")
    print("$> ", end = '')
    li.append(int(input()))
    print("Choose a Heuristic")
    print("1- ")
    print("2- ")
    print("$> ", end = '')
    li.append(int(input()))
    return li
