import sys
import argparse
import heapq
import numpy as np
import math

from initial import init_state
from solvability import solvability 
from generator import make_goal, make_puzzle
from algorithm import a_star



if __name__ == "__main__":
    
   # user_input = get_input()
    parser = argparse.ArgumentParser()
    parser.add_argument("puzzle", type=str, help="must be a solvable puzzle and size >= 3")
    args = parser.parse_args()
    f = open(args.puzzle).read()
    print(f)
    state = init_state(f)
    #solvability(state)
    print (state["board"])
    a_star(state)
