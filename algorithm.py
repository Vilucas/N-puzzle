# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/16 19:00:58 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 15:43:11 by jcruz-y-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# initiate priority queue
# Enqueue the initial position
# Define came_from array
# Define cost_so_far
# Initiate came_from array
# Initiate cost_so_far
# state = a particular map configuration

#from n_puzzle import init_state
import numpy as np
import queue
import math


# this can get more efficient if we are able to access the current number in the goal with math

def     manhattan_dist(cur_state, goal):
    cur_num = None
    cur_dist = 0
    distances = []
    for x in range(cur_state.size):
        for z in range(cur_state.size):
            cur_num = cur_state.board[x][z]
            cur_pos = [x, z]
            for i in range(cur_state.size):
                for j in range(cur_state.size):
                    if (cur_num == goal[i][j]):
                        cur_dist = sum(abs((cur_pos) - (i, j)))
                        distances.append(cur_dist)
    return sum(distances)


def     valid_move(cur_state, move):
    if ((cur_state.board[cur_state.zero] + move)[0] < cur_state.size and 
    (cur_state.board[cur_state.zero] + move)[1] < cur_state.size and 
    (cur_state.board[cur_state.zero] + move)[0] >= 0 and 
    (cur_state.board[cur_state.zero] + move)[1] >= 0):
        return True
    return False

def     init_neighbor(size, new_board):
    state = {}
    state['board'] = new_board
    state['size'] = size
    state['moves'] = ((1, 0), (0, 1), (-1, 0), (0, -1))
    state['zero_pos'] = find_zero(state)
    return state

def     init_neighbor_state(cur_state, movement):
    neighbor = {}
    new_board = list(cur_state.board)
    new_zero = cur_state.zero + movement 
    num_to_swap = new_board[new_zero] #[]?
    new_board[cur_state.zero] = num_to_swap
    new_board[new_zero] = 0
    neighbor = init_neighbor(cur_state.size, new_board)
    return neighbor

def     make_goal(state):
    #goal = np.arange(arrlength)
    #goal = x.reshape(size, size)
    goal = np.empty_like(state.size, state.size)
    #goal = np.array
    n = 0
    num = 1

    while num < math.sqrt(state.size):
        for j in range(state.size + n):  # ->
            goal[n][j] = num
            num += 1
        n += 1    
        j = state.size - n
        for i in range(n, state.size): # !
            goal[i][state.size - n] = num
            num += 1
        for j in range (state.size - n, 0): # <-
            goal[state.size - n][j] = num
            num += 1
        for i in range(state.size, 0 + n): # ¡
            goal[i][-1 + n] = num
            num += 1
    return goal
        

def     neighbors(cur_state):
    neighbors = []
    for move in cur_state.moves():
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
    came_from[start["board"] = start["board"]
    cost_so_far[start] = 0
    goal = make_goal(start)
    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in neighbors(current):
            new_cost = cost_so_far[current] + 1 # 1 is step cost
            # We will add the state to the PQ if the new cost for getting to that state is less
            # than what was previously the cost for that state or if the state is not in the costs
            if next.board not in cost_so_far or new_cost < cost_so_far[next.board]: 
                cost_so_far[next.board] = new_cost
                priority = new_cost + manhattan_dist(next, goal)
                frontier.put(next, priority)
                # We add to our dictionary 
                came_from[next.board] = current



#if __name__ == "__main__":