# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solvability.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/19 11:59:49 by viclucas          #+#    #+#              #
#    Updated: 2019/09/19 12:51:34 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def     solvability(size):
    if size < 3:
        print("size of the square is too little")
    elif size > 5:
        print("size of the game is too big")
        
