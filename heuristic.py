# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    heuristic.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jcruz-y- <jcruz-y-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/20 19:01:45 by viclucas          #+#    #+#              #
#    Updated: 2019/09/23 21:29:19 by jcruz-y-         ###   ########.fr        #
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

def     manhattan_dist_2(cur_state, goal):
    cur_num = None
    distance = 0
    for x in range(cur_state['size']):
        for z in range(cur_state['size']):
            if cur_state['board'][x][z] != goal[x][z]:
                cur_num = cur_state['board'][x][z]
                cur_pos = [x, z]
                distance += get_dist(cur_state, cur_num, cur_pos, goal)
    return distance


#   4 heuristics available for the user
class   heuristic:
    # Returns the number of misplaced tiles
    def     hamming_dist(cur_state, goal):
        cur_dist = 0
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] != goal[x][z]:
                    cur_dist += 1
        return cur_dist

    # Returns the taxicab distance from the current tile pos to the tile goal pos
    def     manhattan_dist(cur_state, goal):
        cur_num = None
        distance = 0
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] != goal[x][z]:
                    cur_num = cur_state['board'][x][z]
                    cur_pos = [x, z]
                    distance += get_dist(cur_state, cur_num, cur_pos, goal)
        return distance

    # This function has being inspired by the recent work of
    # the french PhD Armand Gnakouri aka Kaaris
    def     K_double_rotor(cur_state, goal):
        cur_dist = 0
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] > goal[x][z]:
                    cur_dist += 1
        return cur_dist

    # This function is always paired with Manhattan and returns the number of 
    # conflicting tiles (same row or col of their goal and interferring with goal trajectory)
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
                                cur_dist += 1
                                conf_pairs[(cur_num, num_to_switch)] = (cur_num, num_to_switch)
                                break 
                    elif num_in_goal_col(cur_state, cur_num, cur_pos, goal):
                        for i in range(cur_state['size']):
                            num_to_switch = cur_state['board'][i][z] 
                            s_pos = [i, z]
                            if num_to_switch != cur_num and (num_to_switch, cur_num) not in conf_pairs and num_to_switch != 0 and num_in_goal_col(cur_state, num_to_switch, s_pos, goal) \
                            and num_in_the_way_col(cur_state, num_to_switch, s_pos, goal, cur_pos, cur_num):
                                cur_dist += 1
                                conf_pairs[(cur_num, num_to_switch)] = (cur_num, num_to_switch)
                                break
        cur_dist += manhattan_dist_2(cur_state, goal)
        return cur_dist
