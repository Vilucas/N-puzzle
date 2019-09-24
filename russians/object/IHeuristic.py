import sys
from abc import ABCMeta, abstractmethod, abstractproperty

class IHeuristic:
	__metaclass__=ABCMeta

	@abstractmethod
	#  Calculates a heuristic estimate of the distance from the specified state to the final.
	def getH():
		pass