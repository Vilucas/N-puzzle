# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:00:58 by viclucas          #+#    #+#              #
#    Updated: 2019/09/23 21:39:02 by jcruz-y-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# initiate priority queue
# Enqueue the initial position
# Define came_from array
# Define cost_so_far
# Initiate came_from array
# Initiate cost_so_far
# state = a particular map configuration

import numpy as np
import queue
import math
import operator
from dataclasses import dataclass, field
from typing import Any
from heuristic import heuristic
import time

# Class to ignore the dictionary fields of our state dictionary but compare priority
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    state: Any=field(compare=False)

# Creates the final map
def     make_goal(state):
    goal = np.zeros((state['size'], state['size']), dtype=int)
    n = 0
    num = 1
    t = 0
    r = 0
    s = 0
    while num <= state['size']**2:
        for j in range(s, state['size'] - n):  # ->
            if num >= state['size']**2:
                return goal
            goal[n, j] = num
            num += 1
        if n >= 1:
            s += 1
        n += 1    
        x = state['size'] - n
        for i in range(n, state['size'] - t): # !
            if num >= state['size']**2:
                return goal
            goal[i, x] = num
            num += 1
        t += 1
        for z in range(x - 1, -1 + r, -1): # <-
            if num >= state['size']**2:
                return goal
            goal[x, z] = num
            num += 1
        r += 1
        for i in range(state['size'] - n - 1, 0 + n, -1): # ¡
            if num >= state['size']**2:
                return goal
            goal[i, n - 1] = num
            num += 1
    return goal

# Find zero in the map 
def     find_zero(state):
    pos = []
    for y in range(state["size"]):
        for x in range(state["size"]):
            if state["board"][y][x] == 0:
                pos = [y, x]
                return pos

# Validate the move
def     valid_move(cur_state, move):
    new_pos = tuple(map(operator.add, cur_state['zero_pos'], move))
    board = cur_state['board']
    size = cur_state['size']
    if (new_pos[0] < size and 
    new_pos[1] < size and 
    new_pos[0] >= 0 and 
    new_pos[1] >= 0):
        return True
    return False


def     init_neighbor(size, new_board):
    state = {}

    state['board'] = tuple(map(tuple, new_board))
    state['size'] = size
    state['moves'] = ((1, 0), (0, 1), (-1, 0), (0, -1))
    state['zero_pos'] = find_zero(state)
    return state

def     init_neighbor_state(cur_state, move):
    neighbor = {}
    new_board = np.array(cur_state['board'])
    new_zero = tuple(map(operator.add, cur_state['zero_pos'], move))
    num_to_swap = new_board[new_zero] #[]?
    new_board[cur_state['zero_pos'][0]][cur_state['zero_pos'][1]] = num_to_swap
    new_board[new_zero] = 0
    neighbor = init_neighbor(cur_state['size'], new_board)
    return neighbor

# Returns all possible neighbors the current state could have 
# (maps with valid places where zero could move)
def     neighbors(cur_state):
    neighbors = []
    for move in cur_state["moves"]:
        if valid_move(cur_state, move):
            neighbor = PrioritizedItem(priority=0, state=init_neighbor_state(cur_state, move))
            neighbors.append(neighbor)
    return neighbors


def     a_star(start, user_input, greedy):
    frontier = queue.PriorityQueue()
    frontier.put((start.priority, start))
    came_from = {}    # dictionary containing states as keys and their origin state as value
    cost_so_far = {}  # dictionary with different states (map configs as tuples) that 
                      # have been explored as keys and their cost associated to get there as value
    came_from[start.state['board']] = 0 
    cost_so_far[start.state['board']] = 0
    goal = make_goal(start.state)
    loop = 0
    max_states = 0
    len_states = 0
    fn_len = len
    time_start = time.time()
    while not frontier.empty():
        p_item = frontier.get()
        current = p_item[1].state
        if np.array_equal(np.array(current["board"]), np.array(goal)):
            break
        len_states = fn_len(list(frontier.queue))
        if (len_states > max_states):
            max_states = len_states 

        for next in neighbors(current):
            # The costs so far include the costs to get to that particular state from the source
            # 1 is the step cost
            new_cost = cost_so_far[current['board']] + 1
            # We will add the state to the PQ if the new cost for getting to that state is less
            # than what was previously the cost for that state or if the state is not in the costs
            if next.state['board'] not in cost_so_far or new_cost < cost_so_far[next.state['board']]: 
                cost_so_far[next.state['board']] = new_cost
                if greedy == 1:
                   next.priority = user_input(next.state, goal)  
                elif greedy == 0:
                    next.priority = new_cost + user_input(next.state, goal) 
                came_from[next.state['board']] = [current['board'], p_item[0]]
                frontier.put((next.priority, next))
                loop += 1
    time_end = time.time()
    print('TRAJECTORY\n')
    traj = 0
    trajectory = []
    trajectory.append([current['board'], 0])
    while True:
        if np.array_equal(np.array(current['board']), np.array(start.state['board'])):
            break
        trajectory.append(came_from[current['board']])
        current['board'] = came_from[current['board']][0]
        traj += 1
    j = 0
    for i in range(len(trajectory) - 1, 0, -1):
        print('Depth:', j, 'P_score:',  trajectory[i][1])
        j += 1
        print('\n'.join(' '.join(str(cell) for cell in row) for row in np.array(trajectory[i][0])) + '\n')

    print('P_Score:', trajectory[0][1], 'Depth: ', j)
    print('\n'.join(' '.join(str(cell) for cell in row) for row in np.array(trajectory[0][0])))
    print('Solved in:', time_end - time_start)
    print('STEPS:', traj)
    print('Space complexity (Max states in mem):', max_states)
    print("Time complexity: ", loop)
   
