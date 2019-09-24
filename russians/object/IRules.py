from abc import ABCMeta, abstractmethod, abstractproperty

class IRules():
	__metaclass__=ABCMeta
	#  Returns a list of states that can be migrated from the status field.
	#  @param currentState - The current state for which the neighboring are revealed

	@abstractmethod
	def getNeighbors( self, currentState ):
		pass
		# @return the list of states in which the transition from specified state.
	
	# Returns the distance between the specified states.
	@abstractmethod
	def getDistance( self ):
		pass

	#  Calculates a heuristic estimate of the distance from the specified state to the final.
	@abstractmethod
	def getH( self, state ):
		pass

	# Checks whether the state is finite.
	@abstractmethod
	def isTerminate( self, state ):
		# return bool
		pass
