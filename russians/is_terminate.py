#!/usr/bin/env python

import sys
from object.Matrix import *
import numpy as np

def check_row_right(matrix,row,column,size):
    global flag,max
    val = matrix[row][column]
    while(column < size):
        if matrix[row][column] != val:
            if matrix[row][column] == 0 and (column - 1) >= 0:
                if matrix[row][column - 1] == max:
                    flag = 1
            return (True)
        val += 1
        column += 1
    return (False)

def check_row_left(matrix,row,column,size):
    global flag,max,sz
    val = matrix[row][column]
    while(column >= size):
        if matrix[row][column] != val:
            if matrix[row][column] == 0 and (column + 1) < sz:
                if matrix[row][column + 1] == max:
                    flag = 1
            return (True)
        val += 1
        column -= 1
    return (False)

def check_column_down(matrix,row,column,size):
    global flag,max
    val = matrix[row][column]
    while(row < size):
        if matrix[row][column] != val:
            if matrix[row][column] == 0 and (row - 1) >= 0:
                if matrix[row - 1][column] == max:
                    flag = 1
                return (True)
        val += 1
        row += 1
    return (False)

def check_column_up(matrix,row,column,size):
    global flag,max,sz
    val = matrix[row][column]
    while(row > size):
        if matrix[row][column] != val:
            if matrix[row][column] == 0 and (row + 1) < sz:
                if matrix[row + 1][column] == max:
                    flag = 1
                return (True)
        val += 1
        row -= 1
    return (False)

def check_solve(matrix):
    global flag,max,sz
    flag = 0
    count = 1
    sz = size = len(matrix)
    max = size * size - 1
    row = 0
    column = 0
    i = 1
    j = 0
    while (True):
        if check_row_right(matrix,row,column,size - j):
            if flag:
                print "one"
                return (True)
            return (False)
        if check_column_down(matrix,row,size - i,size - j):
            if flag:
                print "two"
                return (True)
            return (False)
        if check_row_left(matrix,size - i,size - i,j):
            if flag:
                print "three"
                return (True)
            return (False)
        if check_column_up(matrix,size - i,column,j):
            if flag:
                print "four"
                return (True)
            return (False)
        row += 1
        column = column + j
        j += 1
        i += 1
    return (True)
