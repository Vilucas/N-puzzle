# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    heuristics.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/20 19:01:45 by viclucas          #+#    #+#              #
#    Updated: 2019/09/20 21:03:38 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import operator

#   3 heuristics available for the user
class   heuristic:

    def hamming_dist(cur_state, goal):
        cur_dist = 0
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] != goal[x][z]:
                    cur_dist += 1
        return cur_dist


    def manhattan_dist(cur_state, goal):
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

#   This function has being inspired by the recent work of
#   the french PhD Armand Gnakouri aka Kaaris
    def K_double_rotor(cur_state, goal):
        cur_dist = 0
        for x in range(cur_state['size']):
            for z in range(cur_state['size']):
                if cur_state['board'][x][z] > goal[x][z]:
                    cur_dist += 1
        return cur_dist

