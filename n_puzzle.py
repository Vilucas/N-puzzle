# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    n_puzzle.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:01:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/23 19:37:00 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import heapq
import numpy as np
import math

from solvability import solvability, find_zero 
from generator import make_goal, make_puzzle
from algorithm import a_star, make_goal
from dataclasses import dataclass, field
from typing import Any
from parsing import reshape_board
from heuristic import heuristic

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    state: Any=field(compare=False)

#   Get file into tuples
def     init_board(board_str):
    index, x, y = 0, 0, 0

    board_arr = board_str.split(", ")
    arrlength = len(board_arr)
    size = int(math.sqrt(arrlength))
    if size * size != arrlength:
        print("Invalid dimensions, Exiting...")
        sys.exit()
    init_board = np.arange(arrlength)
    init_board = init_board.reshape(size, size)
    board = np.empty_like(init_board)
    try:
        while index < arrlength:
            board[y][x] = board_arr[index]
            x += 1
            index += 1
            if (x == size):
                x = 0
                y += 1
    except:
        print("File horribly formated UwU, Exiting...")
        exit()
    return tuple(map(tuple, board)), size


#   Init the dictionary
def     init_state(board_arr):
    state = {}
    state['board'], state['size'] = init_board(board_arr)
    state['moves'] = ((1, 0), (0, 1), (-1, 0), (0, -1))
    state['zero_pos'] = find_zero(state)
    return state

#   Get user input on Algo and heuristic selection
def     get_input():
    li = []
    try:
        print("Choose a Heuristic function :\n" + "1- Manathan\n" + "2- Hamming\n" + "3- K_double_rotor\n" + "4- Manhattan + Linear Conflict\n" + "$>", end = ' ')
        li.append(int(input()))
        if li[0] > 4 or li[0] < 1:
            raise(True)
        print("Greedy search ? yes | no \n" + "$>", end = ' ')
        li.append(str(input()))
        if li[1] == "yes" or li[1] == "y":
            li[1] = 1
        elif li[1] == "no" or li[1] == "n":
            li[1] = 0
        else:
            raise(True)
    except:
        print("Your input is not correct, Exiting...")
        sys.exit()
    return li

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle", type=str, help="must be a solvable puzzle and size >= 3")
    args = parser.parse_args()
    try:
        f = open(args.puzzle).read()
    except:
        print("Not a valid File, Exiting...")
        exit()
    board = reshape_board(f)
    state = init_state(board)
    solvability(state)
    p_item = PrioritizedItem(priority=0, state=init_state(board))
    user_input = get_input()
    #print("  ORIGINAL\n", np.array(p_item.state['board']))
    if user_input[0] == 1:
        a_star(p_item, heuristic.manhattan_dist, user_input[1])
    elif user_input[0] == 2:
        a_star(p_item, heuristic.hamming_dist, user_input[1])
    elif user_input[0] == 3:
        a_star(p_item, heuristic.K_double_rotor, user_input[1])
    elif user_input[0] == 4:
        a_star(p_item, heuristic.linear_conflict, user_input[1])
