# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    heuristic.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/20 19:01:45 by viclucas          #+#    #+#              #
#    Updated: 2019/09/23 18:24:16 by jcruz-y-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import operator

def     num_in_goal_row(cur_state, cur_num, cur_pos, goal):
    for j in range(cur_state['size']):
        if (goal[cur_pos[0]][j] == cur_num):
            return True 
    return False 
    
def     num_in_goal_col(cur_state, cur_num, cur_pos, goal):
    for i in range(cur_state['size']):
        if (goal[i][cur_pos[1]] == cur_num):
            return True
    return False 

def     num_in_the_way_col(cur_state, num_to_switch, s_pos, goal, cur_pos, cur_num):
    # if col is on the right half numbers increase else viceversa
    # if col on the right and num_to_switch is smaller than cur_num and num_to_switch 
    # is lower in the col than cur_num 

    # numbers are in conflict if one of them needs to go down and the other up and viceversa and
    # if one of them needs to go left and the other right
    for i in range(cur_state['size']):
        if goal[i][s_pos[1]] == num_to_switch:
            s_goal_row = i

    for x in range(cur_state['size']):
        if goal[x][cur_pos[1]] == cur_num:
            c_goal_row = x

    if s_goal_row > c_goal_row and s_goal_row > s_pos[0] and s_pos[0] < cur_pos[0]:
        return True
    
    if s_goal_row < c_goal_row and s_goal_row < s_pos[0] and s_pos[0] > cur_pos[0]:
        return True

    return False

def     num_in_the_way_row(cur_state, num_to_switch, s_pos, goal, cur_pos, cur_num):
    for j in range(cur_state['size']):
        if goal[s_pos[0]][j] == num_to_switch:
            s_goal_col = j

    for z in range(cur_state['size']):
        if goal[cur_pos[0]][z] == cur_num:
            c_goal_col = z

    if s_goal_col > c_goal_col and s_goal_col > s_pos[1]:
        return True

    if s_goal_col < c_goal_col and s_goal_col < s_pos[1]:
        return True

    return False

def     get_dist(cur_state, cur_num, cur_pos, goal):
    cur_dist = 0
    for i in range(cur_state['size']):
        for j in range(cur_state['size']):
            if (cur_num == goal[i][j]):
                cur_dist = tuple(map(operator.sub, cur_pos, (i, j)))
                cur_dist = abs(cur_dist[0]) + abs(cur_dist[1])
                return cur_dist

#   3 heuristics available for the user
class   heuristic:

    def     hamming_dist(cur_state, goal):
        cur_dist = 0
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] != goal[x][z]:
                    cur_dist += 1
        return cur_dist

    # 230 states
    def     manhattan_dist(cur_state, goal):
        cur_num = None
        distance = 0
        #if 
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] != goal[x][z]:
                    cur_num = cur_state['board'][x][z]
                    cur_pos = [x, z]
                    #distances.append(get_dist(cur_state, cur_num, cur_pos, goal))
                    distance += get_dist(cur_state, cur_num, cur_pos, goal)
        return distance

#   This function has being inspired by the recent work of
#   the french PhD Armand Gnakouri aka Kaaris
    def     K_double_rotor(cur_state, goal):
        cur_dist = 0
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] > goal[x][z]:
                    cur_dist += 1
        return cur_dist

    # 170 states, .33s
    def      linear_conflict(cur_state, goal):
        cur_dist = 0
        conf_pairs = {}
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] != goal[x][z] and cur_state['board'][x][z] != 0:
                    cur_num = cur_state['board'][x][z]
                    cur_pos = [x, z]
                    if num_in_goal_row(cur_state, cur_num, cur_pos, goal):
                        for j in range(cur_state['size']):
                            num_to_switch = cur_state['board'][x][j] 
                            s_pos = [x, j]
                            if num_to_switch != cur_num and (num_to_switch, cur_num) not in conf_pairs and num_to_switch != 0 and num_in_goal_row(cur_state, num_to_switch, s_pos, goal) and num_in_the_way_row(cur_state, num_to_switch, s_pos, goal, cur_pos, cur_num):
                               # print('ROW cur_num', cur_num, 'flipping', num_to_switch)
                                cur_dist += 1
                                conf_pairs[(cur_num, num_to_switch)] = (cur_num, num_to_switch)
                                break # maybe the break shouldn't be here if its bigger than 3 
                    elif num_in_goal_col(cur_state, cur_num, cur_pos, goal):
                        for i in range(cur_state['size']):
                            num_to_switch = cur_state['board'][i][z] 
                            s_pos = [i, z]
                            if num_to_switch != cur_num and (num_to_switch, cur_num) not in conf_pairs and num_to_switch != 0 and num_in_goal_col(cur_state, num_to_switch, s_pos, goal) \
                            and num_in_the_way_col(cur_state, num_to_switch, s_pos, goal, cur_pos, cur_num):
                                #print('COL cur_num', cur_num, 'flipping', num_to_switch)
                                cur_dist += 1
                                conf_pairs[(cur_num, num_to_switch)] = (cur_num, num_to_switch)
                                break
        #print('linear conflicts', cur_dist)
        #print(np.array(cur_state['board']))
        return cur_dist
