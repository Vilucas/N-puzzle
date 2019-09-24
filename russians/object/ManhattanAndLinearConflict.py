import sys
from Heuristic import *
from Matrix import *
from State import *
from Manhattan import *
import numpy as np
import copy

class   ManhattanAndLinearConflict(Heuristic):

    def __init__( self, manhattan, stateCorrect ):
        self.manhattan = manhattan
        self.dictRight = self.getIndexRightState( stateCorrect.getMatrixArray() )
        self.size = len(stateCorrect.getMatrixArray())

    def getLinearCoef( self, stateCurrent ):
        dictCurr = self.getIndexRightState( stateCurrent )

        lst = []
        for dig in self.dictRight:
            if dictCurr[dig][0] != self.dictRight[dig][0] and dictCurr[dig][1] != self.dictRight[dig][1]:
                lst.append(dig)
        dict_curr_full = copy.copy(dictCurr)
        for i in lst:
            dictCurr.pop(i)
        row_m = 0
        linear_coef = 0
        while (row_m < self.size):
            i = -1
            while (i >= -self.size):
                digit = int(stateCurrent[row_m][i])
                if digit in dictCurr:
                    col = i - 1
                    while (col >= -self.size):
                        chekd = int(stateCurrent[row_m][col])
                        if (self.dictRight[digit][1] <= self.dictRight[chekd][1]) and (self.dictRight[chekd][0] == dictCurr[digit][0]):
                            linear_coef += 1
                        col -= 1
                i -= 1
            row_m += 1
        return linear_coef
    def getH( self, state, stateCorrect ):
        return ( self.manhattan.getH( state, stateCorrect ) + self.getLinearCoef( state.getMatrixArray() ) )