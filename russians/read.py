import sys
import copy
from object.Matrix import *

def 	Error(string):
	print string
	sys.exit(1)

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
    return True

def 	readFile(nameFile):
	try:
		f = open(nameFile, 'r')
		res = f.read()
		return res.split('\n')
	except:
		Error("Read file error.")

def 	deleteSpace(resultRead):
	if (len(resultRead[0])) == 1 and resultRead[0] == ' ':
		del resultRead[0]
	for x in resultRead:
		try:
			resultRead.remove('')
		except:
			pass
	try:
		resultRead.remove('')
	except:
		pass
	string = ''
	i = 0
	size = len(resultRead)
	try:
		for x in resultRead:
			s = x.strip()
			x = s
			if ((len(x)) == 1 and x[0] == ' '):
				pass
			else:
				old = '0'
				for k in x:
					if k == ' ' and old != ' ':
						string = string + k
						old = ' '
					elif k != ' ':
						old = '0'
						string = string + k
				if (i + 1 != size):
					string = string + "\n"
			i += 1
		string = string.split('\n')
		return string
	except:
		Error("Error in deleteSpace.")

def 	validation(string):
	if (isInt(string[0])) == False:
		Error("Error size map")
	sizeMatrix = int(string[0])
	validationSizeLineHeight(sizeMatrix, string)
	validationSizeLineWeight(sizeMatrix, string)
	validationOnlyDigital(string)
	validationNegative(string)
	validationMaxInt(sizeMatrix, copy.copy(string))
	validationMapDouble(sizeMatrix, copy.copy(string))

def 	validationSizeLineHeight(sizeMatrix, string):
	start = 0
	y = 0
	for c in string:
		if (start == 0):
			start += 1
		else:
			if ((len(c)) >= 1 and c[0] != ' '):
				y += 1
			elem = c.split(' ')
			if (y > sizeMatrix):
				Error("Too big hight matrix")
	if (y < sizeMatrix):
		Error("size y != size map")

def 	validationSizeLineWeight(sizeMatrix, string):
	start = 0
	y = 1
	for c in string:
		if start == 0:
			start += 1
		else:
			c = c.strip()
			s = c.split(' ')
			string[y] = s
			size = len(s)
			y += 1
			if size != sizeMatrix:
				Error("Error size line Weight")

def 	validationOnlyDigital(string):
	for x in string:
		for c in x:
			if ((isInt(c)) == False):
				Error("Error is not digital")

def 	validationNegative(string):
	for x in string:
		for c in x:
			i = int(c)
			if i < 0:
				Error("Error is negative")

def 	validationMaxInt(sizeMatrix, s):
	del s[0]
	maxIntInMatrix = sizeMatrix * sizeMatrix - 1
	for x in s:
		for c in x:
			i = int(c)
			if (i > maxIntInMatrix):
				Error("too big digital in Matrix")

def 	validationMapDouble(sizeMatrix, s):
	del s[0]
	array = numpy.zeros(sizeMatrix * sizeMatrix)
	i = 0
	for x in s:
		for c in x:
			i = int(c)
			if array[i] == -1:
				Error("double digital")
			array[i] -= 1

def 	convertInMatrix(resultRead):
	i = 0
	for c in resultRead:
		res = c.find("#")
		if (res == -1):
			pass
		elif (res == 0):
			resultRead[i] = " "
		else:
			Error("Error string in #")
		i += 1
	res = deleteSpace(resultRead)
	validation(res)
	m = createMatrix(res)
	return m

def 	createMatrix(list):
	m = Matrix(int(list[0]))
	if (m.size < 3):
		Error("Error map")
	if (len(list) == 1): # last
		Error("Error size map")
	sizeX = len(list[1])
	y = 0
	x = 0
	start = 0
	for x in list:
		if start == 0:
			start += 1
			pass
		else:
			s = x
			x = 0
			for n in s:
				m.matrix[y][x] = int(n)
				x += 1
			y += 1
	return m
