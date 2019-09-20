# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    n_puzzle.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:01:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/20 13:41:19 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import heapq
import numpy as np
import math

from solvability import solvability, find_zero 
from generator import make_goal, make_puzzle
#from algorithm import a_star

#from algorithm import a_star

#Formatting of the fichier ?

def     init_board(board_str):
    index, x, y = 0, 0, 0

    board_arr = board_str.split(", ")
    arrlength = len(board_arr)
    size = int(math.sqrt(arrlength))
    if size * size != arrlength:
        print("Invalid dimensions")
        sys.exit()
    init_board = np.arange(arrlength)
    init_board = init_board.reshape(size, size)
    board = np.empty_like(init_board)
    while index < arrlength:
        board[y][x] = board_arr[index]
        x += 1
        index += 1
        if (x == size):
            x = 0
            y += 1
    return tuple(map(tuple, board)), size



def     init_state(board_arr):
    state = {}
    state['board'], state['size'] = init_board(board_arr)
    state['moves'] = ((1, 0), (0, 1), (-1, 0), (0, -1))
    state['zero_pos'] = find_zero(state)
    return state

def     get_input():
    li = []
    try:
        print("Choose an Algorithm :\n" + "1- A*\n" "2- Dijkstra's algorithm\n" + "$>", end = ' ')
        li.append(int(input()))
        if li[0] > 2 or li[0] < 0:
            raise(True)
        print("Choose a Heuristic :\n" + "1- Manathan\n" + "2- Hamming\n" + "$>", end = ' ')
        li.append(int(input()))
        if li[1] > 2 or li[1] < 0:
            raise(True)
    except:
        print("Your input is not correct")
        sys.exit()
    return li


if __name__ == "__main__":
    #user_input = get_input()
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle", type=str, help="must be a solvable puzzle and size >= 3")
    args = parser.parse_args()
    f = open(args.puzzle).read()
    print(f)
    state = init_state(f)
    print(state['board'])
    #a_star(state)
    solvability(state)
