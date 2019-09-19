# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    N-puzzle.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:01:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 15:24:05 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import heapq
import numpy as np

from solvability import solvability 
from generator import make_goal, make_puzzle


def     init_list(tmp, size):
    index, x1, y = 0, 0, 0
    arrlength = len(tmp)
    board = []

    x = np.arange(arrlength)
    x = x.reshape(size,size)
    otherb = np.empty_like(x)
    while index < arrlength:
        otherb[y][x1] = tmp[index]
        x1 += 1
        index += 1
        if (x1 == size):
            x1 = 0
            y += 1
    return otherb

def     find_depart(board, size):
    for y in range(size):
        for x in range(size):
            if board[y][x] == 0:
                data = [y, x]
                break
    return data

def     init_state(size, board):
    data = {}

    data['board'] = tuple(board)
    data['moves'] = ((1, 0), (0, 1), (-1, 0), (0, -1))
    data['size'] = size
    data['zero_pos'] = find_depart(board, size)
    return data

def     get_input():
    li = []
    try:
        print("Choose an Algorithm :\n" + "1- A*\n" "2- Dijkstra's algorithm\n" + "$>", end = ' ')
        li.append(int(input()))
        if li[0] > 2 or li[0] < 0:
            raise(True)
        print("Choose a Heuristic :\n" + "1- \n" + "2- \n" + "$>", end = ' ')
        li.append(int(input()))
        if li[1] > 2 or li[1] < 0:
            raise(True)
    except:
        print("Your input is not correct")
        sys.exit()
    return li


if __name__ == "__main__":

    #user_input = get_input()
    size = 5
    tmp = make_puzzle(size, 1, 10000);
    board = init_list(tmp, size);
    movements = init_state(size, board);
    solvability(movements)
#    algorithm(movements, user_input)