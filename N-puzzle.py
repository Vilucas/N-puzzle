# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    N-puzzle.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:01:05 by viclucas          #+#    #+#              #
#    Updated: 2019/09/17 18:43:24 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import argparse
import heapq
import numpy as np

from algorithm import algorithm 
from generator import make_goal, make_puzzle

#def     node_can_be_moved(head, head_empty, size):
   
def     init_list(tmp, size):
    index, x1, y = 0, 0, 0 
    arrlength = len(tmp)
    board = []

    x = np.arange(arrlength)
    x = x.reshape(size,size)
    otherb = np.empty_like(x)
    #otherb = np.array([size, size])
    while index < arrlength: 
        otherb[y][x1] = tmp[index]
        x1 += 1
        index += 1
        if (x1 == size):
            x1 = 0
            y += 1
    return otherb
         
def     create_coord_in_dico(name, y, x, dico):
    coord = []
    coord.append(x)
    coord.append(y)
    dico[name] = coord
    return dico

def     get_data(board, y, x, size):
    right, left, up, down = -1, -1, -1, -1 
    dico_data = {}

    if y != 0:
        create_coord_in_dico("up", y - 1, x, dico_data)    
    if x + 1 != size:
        create_coord_in_dico("right", y, x + 1, dico_data)    
    if y + 1 != size:
        create_coord_in_dico("down", y + 1, x, dico_data)    
    if x != 0:
        create_coord_in_dico("left", y, x + 1, dico_data)    
    return dico_data 

def     surounded_by(board, size):
    for y in range(0, size):
        for x in range(0, size):
            if board[y][x] == 0:
                data = get_data(board, y, x, size)
                break
    data.size = size
    data.init = board[y][x]
    return data

if __name__ == "__main__":
    size = 5
    tmp = make_puzzle(size, 1, 10000);
    board = init_list(tmp, size);
    data = surounded_by(board, size)
    algorithm(data, size)

    print(data)
