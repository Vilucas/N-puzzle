# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:00:58 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 19:49:19 by jcruz-y-         ###   ########.fr        #
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

# this can get more efficient if we are able to access the current number in the goal with math

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
    new_board[cur_state['zero_pos']] = num_to_swap
    new_board[new_zero] = 0
    neighbor = init_neighbor(cur_state['size'], new_board)
    return neighbor

def     make_goal(state):
    #goal = np.arange(arrlength)
    #goal = x.reshape(size, size)
    goal = np.zeros((state['size'], state['size']), dtype=int)
    #goal = np.array
    n = 0
    num = 1
    t = 0
    r = 0
    s = 0
    while num <= state['size']**2 + 1:
        print('while', num)
        for j in range(s, state['size'] - n):  # ->
            if num >= state['size']**2:
                print("GOAL\n", goal)
                return goal
            goal[n, j] = num
            print('right', num)
            num += 1
        if n >= 1:
            s += 1
        n += 1    
        x = state['size'] - n
        if num == state["size"]**2 - 1:
            print("s", s, "state['size'] - n", state['size'] - n)
            break
        for i in range(n, state['size'] - t): # !
            if num >= state['size']**2:
                print("GOAL\n", goal)
                return goal
            goal[i, x] = num
            print('down', num)
            num += 1
        if num == state["size"]**2 - 1:
            print("s =", s, "state['size'] - n =", state['size'] - n)
            break
        t += 1
        for z in range(x - 1, -1 + r, -1): # <-
            if num >= state['size']**2:
                print("GOAL\n", goal)
                return goal
            print('left', num)
            goal[x, z] = num
            num += 1
        r += 1
        for i in range(state['size'] - n - 1, 0 + n, -1): # ¡
            if num >= state['size']**2:
                print("GOAL\n", goal)
                return goal
            print('up', num)
            goal[i, n - 1] = num
            num += 1

    print("GOAL\n", goal)
    return goal
        

def     neighbors(cur_state):
    neighbors = []
    for move in cur_state["moves"]:
        if valid_move(cur_state, move):
            neighbor = init_neighbor_state(cur_state, move)
            neighbors.append(neighbor)
    return neighbors

    # neighbors method
    # check where zero is
    # get the map configs of where 0 could go
    # return those map configs as a tuple

def     a_star(start):
    frontier = queue.PriorityQueue()
    frontier.put(start)
    came_from = {}    # dictionary containing states as keys and their origin state as value
    cost_so_far = {}  # dictionary with different states (map configs as tuples) that 
                      # have been explored as keys and their cost associated to get there as value
    came_from[start['board']] = start['board']
    cost_so_far[start['board']] = 0
    goal = make_goal(start)
    while not frontier.empty():
        current = frontier.get()

        if np.array_equal(np.array(current["board"]), np.array(goal)):
            break

        for next in neighbors(current):
            new_cost = cost_so_far[current['board']] + 1 # 1 is step cost
            # We will add the state to the PQ if the new cost for getting to that state is less
            # than what was previously the cost for that state or if the state is not in the costs
            if next['board'] not in cost_so_far or new_cost < cost_so_far[next['board']]: 
                cost_so_far[next['board']] = new_cost
                priority = new_cost + manhattan_dist(next, goal)
                frontier.put(priority, next)
                # We add to our dictionary 
                came_from[next['board']] = current
                print(next['board'])