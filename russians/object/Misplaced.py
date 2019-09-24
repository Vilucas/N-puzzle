import sys
from IHeuristic import *
from Matrix import *
from State import *

class   Misplaced(IHeuristic):

    def getH( self, state, stateCorrect ):
        def coefCount( matrix_correct, matrix_current ):
            size = 0
            for i,j in enumerate(matrix_correct):
                    for k,l in enumerate(j):
                        if matrix_correct[i][k] != matrix_current[i][k]:
                            size += 1
            return size
        return ( coefCount( state.getMatrixArray(), stateCorrect.getMatrixArray() ))