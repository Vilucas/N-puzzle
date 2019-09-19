# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    N-puzzle.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:01:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/18 21:20:42 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import heapq
import numpy as np

#from algorithm import algorithm 
from generator import make_goal, make_puzzle

def     create_node(cost, parent_node, coord):
    node = {}
    node['g'] = cost
    node['h'] = 5
    node['f'] = node['g'] + node['h']
    node['coord'] = coord
    node['old_cord'] = None
   # if parent_node['coord']:
    #    node['old_cord'] = parent_node;
    return node

def     find_your_neighbours(movements, cost, parent_node)
    node = []
    while (limit_tester(movements) == True)
        create_node(cost, parent_node, 

def     algorithm(movements):
    close_list = []

    open_list = find_your_neighbours(movements)
    print(open_list)
#   close_list = ft_choosen_one(open_list)


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

def     init_movements(size, board):
    
    data = {}

    data['up'] = (1, 0)
    data['right'] = (0, 1)
    data['down'] = (- 1, 0)
    data['left'] = (0, - 1)
    data['size_of_map'] = size
    data['init'] = find_depart(board, size)
    return data

if __name__ == "__main__":
    general_data = {}

    size = 5
    tmp = make_puzzle(size, 1, 10000);
    board = init_list(tmp, size);
    print(board)
    movements = init_movements(size, board);
    print(movements)
    algorithm(movements)
