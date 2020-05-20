# -*- coding: utf-8 -*-
## Starting in the top left corner of a 2×2 grid, and only being able to move
## to the right and down, there are exactly 6 routes to the bottom right corner.
## How many such routes are there through a 20×20 grid?
import math
import time

"""
This is a classic combinatorics problem. To get from the top left corner to the bottom right corner of an N*N grid,
it involves making exactly N moves right and N moves down in some order. Because each individual down or right move
is indistinguishable, there are exactly 2N choose N (binomial coefficient) ways of arranging these moves.

Formula = x!/(y!(x-y)!)

Soln: 137846528820 found in 3.59599995613 seconds
"""


start = time.time()

def compute():
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
    if y == x:
        print(1)
    elif y == 1:
        print(x)
    elif y > x:
        print(0)
    else:                # will be executed only if y != 1 and y != x and x >= y
        a = math.factorial(x)
        b = math.factorial(y)
        c = math.factorial(x-y)
        div = a // (b * c)
    return div


if __name__ == "__main__":
    div = compute()
    elapsed = (time.time() - start)
    print "%s found in %s seconds" % (div,elapsed)
