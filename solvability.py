# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solvability.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 11:59:49 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 15:35:17 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



def     first_checks(state):
    board, flag = state['board'], 0
    
    print(board)
    if state['size'] < 3 or state['size'] > 5:
        print("size of the puzzle has to be between 3x3 and 5x5")
        sys.exit()
    for i in range(state['size'] * state['size']):
        for y in range(state['size']):
            for x in range(state['size']):
                if board[y][x] == i:
                    flag += 1
        if flag != 1:
            print("Invalid Map")
            sys.exit()
        flag = 0
    return True

def     solvability(state):
    first_checks(state)
    print("MAP CORRECT")
    return True
