#!/usr/bin/env python

import sys
from object.Matrix import *
import numpy as np
#from read import *

def fill_row_right(matrix,row,column,size):
    global flag,max,gval
    val = matrix[row][column]
    while(column <= size):
        if val == max:
            return (True)
        matrix[row][column] = val
        val += 1
        column += 1
    gval = val
    if val >= max and matrix[row + 1][column - 1] != 0:
        return (True)
    return (False)

def fill_row_left(matrix,row,column,size):
    global flag,max,sz,gval
    val = matrix[row][column]
    while(column >= size):
        if matrix[row][column] == max:
            return (True)
        matrix[row][column] = val
        val += 1
        column -= 1
    gval = val
    if val >= max and matrix[row - 1][column + 1] != 0:
        return (True)
    return (False)

def fill_column_down(matrix,row,column,size):
    global flag,max,gval
    val = matrix[row][column]
    while(row <= size):
        if matrix[row][column] == max:
            return (True)
        matrix[row][column] = val
        val += 1
        row += 1
    gval = val
    if val >= max:
        return (True)
    return (False)

def fill_column_up(matrix,row,column,size):
    global flag,max,sz,gval
    val = matrix[row][column]
    while(row > size):
        if matrix[row][column] == max:
            return (True)
        matrix[row][column] = val
        val += 1
        row -= 1
    gval = val
    if val >= max:
        return (True)
    return (False)

def fill_matrix(matrix_in):
    global flag,max,sz,gval
    flag = 0
    count = 1
    sz = size = len(matrix_in)
    matrix = numpy.zeros((sz, sz))
    max = size * size - 1
    size -= 1
    row = 0
    column = 0
    gval = matrix[row][column] = 1
    i = 1
    j = 0
    l = 0
    z = 0
    while (True):
        if fill_row_right(matrix,row,column,size - j):
            return (matrix)
        if fill_column_down(matrix,row,size - j,size - j):
            return (matrix)
        if fill_row_left(matrix,size - j,size - j,j):
            return (matrix)
        if fill_column_up(matrix,size - j, j, j):
            return (matrix)
        row += 1
        if j == 0:
            column = 0
        else:
            column += j
        if column >= row and j != 0:
            column = row - 1
        j += 1
    return (matrix)
