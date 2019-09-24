import sys
from IHeuristic import *

class Heuristic(IHeuristic):
    def getIndexRightState( self, state ):
        def getIndex( matrix, digit ):
            for row, j in enumerate( matrix ):
                    for column,l in enumerate( j ):
                        if l == digit:
                           return row, column
        dict = {}
        for row, j in enumerate( state ):
            for column,l in enumerate( j ):
                list = getIndex(state, l)
                dict.update({int(l): list})
        return dict