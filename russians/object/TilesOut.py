import sys
from Heuristic import *
from Matrix import *
from State import *
from Manhattan import *
import numpy as np
import copy
from ManhattanAndLinearConflict import *

class   TilesOut(ManhattanAndLinearConflict):

    def __init__( self, manhattan, stateCorrect):
        ManhattanAndLinearConflict.__init__(self, manhattan, stateCorrect)

    def getTilesOutCoef( self, stateCorrect, stateCurrent ):
        dictRight = self.getIndexRightState( stateCorrect )
        dictRurr = self.getIndexRightState( stateCurrent )
        tcoef = 0
        for dig in dictRight:
            if dictRurr[dig][0] != dictRight[dig][0]:
                tcoef += 1
            if dictRurr[dig][1] != dictRight[dig][1]:
                tcoef += 1
        return tcoef
    
    def getH( self, state, stateCorrect ):
        return ( ManhattanAndLinearConflict.getH(self, state, stateCorrect ) + self.getTilesOutCoef(stateCorrect.getMatrixArray(), state.getMatrixArray() ))