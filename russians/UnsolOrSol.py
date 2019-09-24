import sys

def getIndex( matrix, digit ):
    for row, j in enumerate( matrix ):
        for column,l in enumerate( j ):
            if l == digit:
                return row
def inversion( State ):
    lst_goal = []
    lst = []
    for row, j in enumerate( State ):
        for column, l in enumerate( j ):
            if l == 0:
                pass
            else:
                lst.append(l)
    for row, j in enumerate( State ):
        for column, l in enumerate(j):
            if l == 0:
                pass
            else:
                lst_goal.append(l)
    inv_count = 0
    for comp in lst_goal:
        del lst[0]
        for itera in lst:
            if (comp > itera):
                inv_count += 1
    return inv_count
def isSolvable( startState, goalState ):
    size = len(startState)
    inv = 0
    inv += inversion( startState )
    inv += inversion( goalState )
    if size % 2 == 0:
        inv += getIndex(startState, 0)
        inv += getIndex(goalState, 0)
    if not inv % 2 == 0:
        return False
    return True