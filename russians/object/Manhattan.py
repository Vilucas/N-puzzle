import sys
from IHeuristic import *
from Matrix import *
from State import *

class   Manhattan(IHeuristic):
    def __init__(self, state):
        self.max = len( state.getMatrixArray() ) * len( state.getMatrixArray() )

    def getH( self, state, stateCorrect ):
        def getIndex( matrix, digit ):
            for row, j in enumerate( matrix ):
                for column,l in enumerate( j ):
                    if l == digit:
                        return ( row, column )
        h = 0
        for digit in range( self.max ):
            indSt = getIndex( state.getMatrixArray(), digit )
            indCor = getIndex( stateCorrect.getMatrixArray(), digit )
            h += abs( indSt[0] - indCor[0] ) + abs( indSt[1] - indCor[1] )
        return (h)