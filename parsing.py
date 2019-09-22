# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parsing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: viclucas <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/21 13:58:51 by viclucas          #+#    #+#              #
#    Updated: 2019/09/21 17:01:30 by viclucas         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Return the whole number
def     whole_number(s, i):
    p = ""

    while i < len(s) and (s[i] >= '0' and s[i] <= '9'):
        p += s[i]
        i += 1
    return i, p

# False if only comment and spaces until '\n' (it means its the size indicator so we don't store it)
# the whole number if other real number in the line so I have to store this one aswell 
# otherwise its garbage, file isn't well formated, we exit
def     path_clear(s, i):
    while (s[i] >= '0' and s[i] <= '9') and i < len(s):
        i += 1
    while i < len(s):
        if s[i] == '#' or s[i] == '\n':
            return i, False
        if s[i] >= '0' and s[i] <= '9':
            return i, True 
        #if s[i] != ' ' and s[i] != ',' and (s[i] < '0' or s[i] > '9'):
        #    print("Argument file type not reconized, Exiting...")
        #   exit()
        i += 1
    return i, True


# Move to next existing num that isn't in a comment
# return index pos
def     move_to_num(s, i):
    flag = 0

    while i < len(s):
        while i < len(s) and (s[i] < '0' or s[i] > '9'):
            if s[i] == '#':
                flag = 1;
            elif s[i] == '\n':
                flag = 0
            i += 1
        if i == len(s):
            return i
        if (s[i] >= '0' and s[i] <= '9') and flag == 0:
            return i
        i += 1
    return i 
# Reshape board to make it like the generator output
def     reshape_board(s):
    start, flag, board = 0, 0, ""
    i = 0
    num = ""

    i = move_to_num(s, i)
    if (i < len(s)):
        i, start = path_clear(s, i)
        if start != False:
            tmp, board = whole_number(s, 0)
            flag = 1
    while (i < len(s)):
        i = move_to_num(s, i)
        if i == len(s):
            break
        if (flag):
            board += ", "
        i, num = whole_number(s, i)
        board += num
        flag = 1
    return board
