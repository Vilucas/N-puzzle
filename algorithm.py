# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:00:58 by viclucas          #+#    #+#              #
#    Updated: 2019/09/20 14:01:39 by jcruz-y-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# initiate priority queue
# Enqueue the initial position
# Define came_from array
# Define cost_so_far
# Initiate came_from array
# Initiate cost_so_far
# state = a particular map configuration

from initial import find_zero
import numpy as np
import queue
import math
import operator
from dataclasses import dataclass, field
from typing import Any

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
        print('while', num)
        for j in range(s, state['size'] - n):  # ->
            if num >= state['size']**2:
                print("  GOAL\n", goal)
                return goal
            goal[n, j] = num
            print('right', num)
            num += 1
        if n >= 1:
            s += 1
        n += 1    
        x = state['size'] - n
        for i in range(n, state['size'] - t): # !
            if num >= state['size']**2:
                print("DOWN GOAL\n", goal)
                return goal
            goal[i, x] = num
            print('down', num)
            num += 1
        t += 1
        for z in range(x - 1, -1 + r, -1): # <-
            if num >= state['size']**2:
                print("LEFT GOAL\n", goal)
                return goal
            print('left', num)
            goal[x, z] = num
            num += 1
        r += 1
        for i in range(state['size'] - n - 1, 0 + n, -1): # ¡
            if num >= state['size']**2:
                print("UP GOAL\n", goal)
                return goal
            print('up', num)
            goal[i, n - 1] = num
            num += 1

    print("GOAL\n", goal)
    return goal

def     find_zero(state):
    pos = []
    for y in range(state["size"]):
        for x in range(state["size"]):
            if state["board"][y][x] == 0:
                pos = [y, x]
                break
    return pos

# for length 3 +230 states .4 s
def     manhattan_dist(cur_state, goal):
    cur_num = None
    cur_dist = 0
    distances = []
    for x in range(cur_state['size']):
        for z in range(cur_state['size']):
            cur_num = cur_state['board'][x][z]
            cur_pos = [x, z]
            for i in range(cur_state['size']):
                for j in range(cur_state['size']):
                    if (cur_num == goal[i][j]):
                        cur_dist = tuple(map(operator.sub, cur_pos, (i, j)))
                        cur_dist = abs(cur_dist[0]) + abs(cur_dist[1])
                        distances.append(cur_dist)
    return sum(distances)

# for length 3 +1500 states .646 s
def     hamming_dist(cur_state, goal):
    cur_dist = 0
    for x in range(cur_state['size']):
        for z in range(cur_state['size']):
            if cur_state['board'][x][z] != goal[x][z]:
                cur_dist += 1
    return cur_dist

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

def     a_star(start):
    frontier = queue.PriorityQueue()
    frontier.put((start.priority, start))
    came_from = {}    # dictionary containing states as keys and their origin state as value
    cost_so_far = {}  # dictionary with different states (map configs as tuples) that 
                      # have been explored as keys and their cost associated to get there as value
    came_from[start.state['board']] = start.state['board']
    cost_so_far[start.state['board']] = 0
    goal = make_goal(start.state)
    i = 0
    max_states = 0
    len_states = 0
    while not frontier.empty():
        #print("FRONTIER QUEUE\n\n", frontier.queue)
        p_item = frontier.get()
        #print('cur_prior', p_item[0])
        current = p_item[1].state
        #print("CURRENT", current, "\n\n")
        #print("current board\n",'\n'.join(' '.join(str(cell) for cell in row) for row in np.array(current["board"])))
        #print("current priority\n", p_item.priority)
        #print('equality\n', np.array(current["board"]), np.array(goal))
        #print("manhattan dist", manhattan_dist(current, goal))
        if np.array_equal(np.array(current["board"]), np.array(goal)):
            print("reached goal?")
            break
        len_states = len(list(frontier.queue))
        if (len_states > max_states):
            max_states = len_states 
        #print('total priorities', len_states)
        #for z in frontier.queue:
        #   print('prt', z[1].priority)

        for next in neighbors(current):
            #next = i.state
            # The costs so far include the costs to get to that particular state from the source
            new_cost = cost_so_far[current['board']] + 1 # 1 is step cost
            #print("new_cost")
            # We will add the state to the PQ if the new cost for getting to that state is less
            # than what was previously the cost for that state or if the state is not in the costs
            if next.state['board'] not in cost_so_far or new_cost < cost_so_far[next.state['board']]: 
                cost_so_far[next.state['board']] = new_cost
                next.priority = new_cost + manhattan_dist(next.state, goal)
                #next.priority = new_cost + hamming_dist(next.state, goal)
                #print('new_cost', new_cost)
                #print('manhattan dist', manhattan_dist(next.state, goal))
                frontier.put((next.priority, next))
                #frontier.sort(reversed=True)
                # We add to our dictionary 
                came_from[next.state['board']] = current['board']
                #print('NEXT', np.array(next.state['board']))
        #if i == 10:
        #    while not frontier.empty():
        #        print('prt', frontier.get()[1].priority)
        #    break
        i += 1
    print('start', np.array(start.state['board']))
    print('current', np.array(current['board']))
    while not np.array_equal(np.array(current['board']), np.array(start.state['board'])):
        print(np.array(current['board']))
        current = came_from[current['board']]

    print("LOOP: ", i)
    print(np.array(current['board']))
    print('MAX_STATES', max_states)