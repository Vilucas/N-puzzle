import sys
from Rules import *
from State import *

class 	Astar:

# Creates an object to find the terminal state by the specified rules.
	def 	__init__( self, rules ):
		self.closedStates = 0
		self.rules = rules
		self.totalSizeState = 0
		self.totalMaxSizeState = 0

# Applies the algorithm A * to find the shortest path to the terminal state from the indicated.
# return @param a sequence of states from a given state to a terminal state.
	def 	search( self, startState ):
		closeList = list()
		openList = list()
		openList.append( startState )
		startState.setG( 0 )
		startState.setH( self.rules.getH( startState ))
		startState.mathHash()
		while ( len( openList )!= 0 ):
			current,i = self.getStateWithMinF( openList )
			# print current.getMatrixArray()
			if 	self.rules.isTerminate( current ):
				listState = list()
				return ( self.completeSolution( current, listState ))
			openList.pop( i )
			closeList.append( current )
			neighborsListState = self.rules.getNeighbors( current )
			for next in neighborsListState:
				next.mathHash()
				if (( self.find( next, closeList )) == True ):
					continue
				gScope = current.getG() + self.rules.getDistance()
				isGBetter = False
				if (( self.find( next, openList )) == False ):
					next.setH( self.rules.getH( next ))
					openList.append( next )
					self.totalSizeState += 1
					count = len(openList)
					if (count > self.totalMaxSizeState):
						self.totalMaxSizeState = count
					isGBetter = True		
				else:
					isGBetter = gScope <= next.getG()
				if ( isGBetter == True ):
					next.setStateParent( current )
					next.setG( gScope )
		return 0;

	def 	find( self, state, listState ):
		for currentState in listState:
			if ( currentState == state ):
				return ( True )
		return ( False )

	def 	getStateWithMinF( self, openList ):
		min = sys.maxsize - 1
		i = 0
		i_res = 0
		for state in openList:
			if state.getF() <= min:
				min = state.getF()
				i_res = i
			i += 1
		return ( openList[i_res], i_res )

	def 	completeSolution( self, terminate, listState):
			listState.append(terminate.getMatrixArray())
			tmp = terminate.getStateParent()
			while tmp.countParent != 0:
				listState.append(tmp.getMatrixArray())
				tmp = tmp.getStateParent()
			return (listState)











