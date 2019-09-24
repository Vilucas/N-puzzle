from Matrix import *
import hashlib

class 	State:

	def __init__( self, matrix, count=0):
		self.matrix = matrix
		self.g = 0
		self.h = 0
		self.f = 0
		self.countParent = 0
		self.hash = ""
		if (count == 0):
			self.parent = State(Matrix(1), 1)

	def getG( self ):
		return ( self.g )

	def getF( self ):
		return ( self.g + self.h )

	def getH( self ):
		return ( self.h )

	def setH( self, h ):
		self.h = h

	def setG( self, g ):
		self.g = g

	def getStateParent( self ):
		return ( self.parent )

	def setStateParent( self, stateParent ):
		self.countParent += 1
		self.parent = stateParent

	def getMatrixArray( self ):
		return ( self.matrix.matrix )

	def getMatrixObject( self ):
		return ( self.matrix )

	def __eq__( self, state ):
		return ( self.hash == state.hash )

	def 	mathHash( self ):
		hashObj = hashlib.md5()
		size = self.matrix.size
		i = 0
		string = ""
		array = self.getMatrixArray()
		while ( i < size ):
			j = 0
			while j < size:
				string = string + str( array[i][j] )
				j += 1
			i += 1
		hashObj.update( string )
		self.hash = hashObj.hexdigest()