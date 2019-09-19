# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    n_puzzle.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:01:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 15:51:00 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import heapq
import numpy as np
import math

from solvability import solvability 
from generator import make_goal, make_puzzle
from algorithm import a_star


def     init_board(board_str):
    index, x1, y = 0, 0, 0
    arrlength = 9

    board_arr = board_str.split(", ")
    print(board_arr)
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
    return tuple(board), size

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
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle", type=str, help="must be a solvable puzzle and size >= 3")
    args = parser.parse_args()
    f = open(args.puzzle).read()
    print(f)
    state = init_state(f)
    #solvability(state)
    a_star(state)
    solvability(state)
