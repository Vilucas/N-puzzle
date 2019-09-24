import numpy

class Matrix:
	def __init__( self, _size ):
		self.size = _size
		self.matrix = numpy.zeros(( _size, _size ))

	def moveRight( self,row,column ):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row][column + 1]
		self.matrix[row][column + 1] = buf
	
	def moveLeft( self,row,column ):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row][column - 1]
		self.matrix[row][column - 1] = buf
	
	def moveUp( self,row,column ):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row - 1][column]
		self.matrix[row - 1][column] = buf
	
	def moveDown( self,row,column ):
		buf = self.matrix[row][column]
		self.matrix[row][column] = self.matrix[row + 1][column]
		self.matrix[row + 1][column] = buf
	
	def setMatrix( self, matrix ):
		self.matrix = matrix
	
	def getMatrix( self ):
		return ( self.matrix )
	
	def getSize( self ):
		return ( self.size )
