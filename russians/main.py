import hashlib
import sys
from object.Matrix import *
import numpy as np
from is_terminate import *
from fcoefficientsearch import *
from read import *
from object.Rules import *
from object.State import *
from object.Astar import *
from object.Manhattan import *
from object.ManhattanAndLinearConflict import *
from object.Misplaced import *
from object.TilesOut import *
from UnsolOrSol import *

def printArray(m):
	for line in m:
		for x in line:
			if (x != 0):
				sys.stdout.write(" " + str(int(x)) + " ")
			else:
				sys.stdout.write(Bcolors.OKGREEN + " " + str(int(x)) + " " + Bcolors.ENDC)
		sys.stdout.write("\n")

def printUsage(stringUsage):
	for x in stringUsage:
		print x

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    OKRED = '\033[91m'
    ENDC = '\033[0m'

stringUsage = list()
stringUsage.append(Bcolors.OKYELLOW + "Usage python main.py maps/anyoneMaps [-g=true or -g=false] [-m or -ml or -mi or -to] [-f=true or -f=false]" + Bcolors.ENDC)
stringUsage.append(Bcolors.OKGREEN + "-m == Manhattan heuristic" + Bcolors.ENDC)
stringUsage.append(Bcolors.OKGREEN + "-ml == Manhattan heuristic + LinearConflict heuristic" + Bcolors.ENDC)
stringUsage.append(Bcolors.OKGREEN + "-to == Manhattan heuristic + LinearConflict heuristic + TilesOut heuristic" + Bcolors.ENDC)
stringUsage.append(Bcolors.OKGREEN + "-mi == Misplaced heuristic" + Bcolors.ENDC)
stringUsage.append(Bcolors.OKGREEN + "-f if true then no steps else steps will be print " + Bcolors.ENDC)
stringUsage.append(Bcolors.OKGREEN + "-g if == false then uniform-cost else greedy searches" + Bcolors.ENDC)

if (len(sys.argv) != 5):
    printUsage(stringUsage)
    sys.exit(1)
if (sys.argv[2] != "-g=true" and sys.argv[2] != "-g=false"):
    printUsage(stringUsage)
    sys.exit(1)
if (sys.argv[3] != "-m" and sys.argv[3] != '-ml' and sys.argv[3] != "-mi" and sys.argv[3] != "-to"):
    printUsage(stringUsage)
    sys.exit(1)
if (sys.argv[4] != "-f=true" and sys.argv[4] != "-f=false"):
    printUsage(stringUsage)
    sys.exit(1)

resultRead = readFile(sys.argv[1])
m = convertInMatrix(resultRead)
sOrigin = State(m)

if (sys.argv[3] == "-m"):
	heuristic = Manhattan(sOrigin)
elif (sys.argv[3] == "-ml"):
	heuristic = ManhattanAndLinearConflict(Manhattan(sOrigin), sOrigin)
elif (sys.argv[3] == "-mi"):
	heuristic = Misplaced()
elif (sys.argv[3] == "-to"):
	heuristic = TilesOut(Manhattan(sOrigin), sOrigin)

if (sys.argv[2] == "-g=false"):
	rules = Rules(sOrigin, heuristic, 0)
else:
	rules = Rules(sOrigin, heuristic, 1)

astar = Astar(rules)
print Bcolors.HEADER, "Start State:", Bcolors.ENDC
printArray(sOrigin.getMatrixArray())

if (isSolvable(sOrigin.getMatrixArray(), rules.stateCorrect.getMatrixArray() ) == False):
	print Bcolors.OKRED, "Unsolvable puzzle", Bcolors.ENDC
	sys.exit(1)

a = astar.search(sOrigin)
size = len(a)
i = size - 1
step = 1

while i > 0:
	if (i != 0 and sys.argv[4] != "-f=true"):
		print Bcolors.OKYELLOW, "step" + Bcolors.ENDC, Bcolors.OKRED, step, Bcolors.ENDC
		printArray(a[i])
	i -= 1
	step += 1
print Bcolors.OKGREEN, "Solution:", Bcolors.ENDC
printArray(a[0])
print Bcolors.OKBLUE, "Total number of states:", Bcolors.ENDC, astar.totalSizeState
print Bcolors.OKBLUE, "Max number of states:", Bcolors.ENDC, astar.totalMaxSizeState
if (astar.totalMaxSizeState == 0 and astar.totalSizeState == 0):
	print Bcolors.OKBLUE, "Count step move:", Bcolors.ENDC, 0
else:
	print Bcolors.OKBLUE, "Count step move:", Bcolors.ENDC, size