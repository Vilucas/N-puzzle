# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:00:58 by viclucas          #+#    #+#              #
#    Updated: 2019/09/23 18:23:08 by jcruz-y-         ###   ########.fr        #
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

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    state: Any=field(compare=False)

# this can get more efficient if we are able to access the current number in the goal with math
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

def     find_zero(state):
    pos = []
    for y in range(state["size"]):
        for x in range(state["size"]):
            if state["board"][y][x] == 0:
                pos = [y, x]
                return pos

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

## both heuristics 23000 states, 1 min

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

def     neighbors(cur_state):
    neighbors = []
    for move in cur_state["moves"]:
        if valid_move(cur_state, move):
            neighbor = PrioritizedItem(priority=0, state=init_neighbor_state(cur_state, move))
            neighbors.append(neighbor)
    return neighbors

    # neighbors method
    # check where zero is
    # get the map configs of where 0 could go
    # return those map configs as a tuple

def     a_star(start, user_input):
    frontier = queue.PriorityQueue()
    frontier.put((start.priority, start))
    came_from = {}    # dictionary containing states as keys and their origin state as value
    cost_so_far = {}  # dictionary with different states (map configs as tuples) that 
                      # have been explored as keys and their cost associated to get there as value
    came_from[start.state['board']] = 0 # start.state['board']
    cost_so_far[start.state['board']] = 0
    goal = make_goal(start.state)
    i = 0
    max_states = 0
    len_states = 0
    fn_len = len
    while not frontier.empty():
        #print("FRONTIER QUEUE\n\n", frontier.queue)
        p_item = frontier.get()
        current = p_item[1].state
        #print("current board\n",'\n'.join(' '.join(str(cell) for cell in row) for row in np.array(current["board"])))
        if np.array_equal(np.array(current["board"]), np.array(goal)):
            break
        len_states = fn_len(list(frontier.queue))
        if (len_states > max_states):
            max_states = len_states 

        for next in neighbors(current):
            #next = i.state
            # The costs so far include the costs to get to that particular state from the source
            new_cost = cost_so_far[current['board']] + 1 # 1 is step cost
            #print("new_cost")
            # We will add the state to the PQ if the new cost for getting to that state is less
            # than what was previously the cost for that state or if the state is not in the costs
            if next.state['board'] not in cost_so_far or new_cost < cost_so_far[next.state['board']]: 
                cost_so_far[next.state['board']] = new_cost
                if user_input[0] == 1:
                    next.priority = new_cost + heuristic.manhattan_dist(next.state, goal) 
                elif user_input[0] == 2:
                    next.priority = new_cost + heuristic.hamming_dist(next.state, goal)
                elif user_input[0] == 3:
                    next.priority = new_cost + heuristic.K_double_rotor(next.state, goal)
                elif user_input[0] == 4:
                    next.priority = new_cost + heuristic.manhattan_dist(next.state, goal) + heuristic.linear_conflict(next.state, goal)
                frontier.put((next.priority, next))
                # We add to our dictionary of traced boards
                came_from[next.state['board']] = [current['board'], p_item[0]]
        #if i == 10:
        #    while not frontier.empty():
        #        print('prt', frontier.get()[1].priority)
        #    break
        i += 1
    print('start\n', np.array(start.state['board']))
    print('current', np.array(current['board']))
    print('MAX_STATES', max_states)
    print("LOOP: ", i)
    print('TRAJECTORYYY')
    traj = 0
    trajectory = []
    #trajectory.append([current['board'], came_from[current['board'][1]]])
    trajectory.append([current['board'], 0])
    while True:
        if np.array_equal(np.array(current['board']), np.array(start.state['board'])):
            break
        trajectory.append(came_from[current['board']])
        current['board'] = came_from[current['board']][0]
        traj += 1
    j = 0
    for i in range(len(trajectory) - 1, 0, -1):
        print('P_Score:',  trajectory[i][1], 'Depth: ', j)
        j += 1
        print(np.array(trajectory[i][0]), '\n')

    print('P_Score:', trajectory[0][1], 'Depth: ', j)
    print(np.array(trajectory[0][0]), '\n')
    print('STEPS:', traj)

    #print(np.array(current['board']))
