# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:40:03 2016
Load Martix V2
@author: Munish
"""

#############################################################
## Another technique to create 9x9 array
#############################################################
##$ cat string81_v2.py
##!/usr/bin/env python
import numpy as np

line = open("sudoku9927.txt").read()
## Strip removes all blank spaces
line = line.strip()
if len(line) != 81:
    raise SystemExit("ERROR: string does not have 81 characters!")

## create a 9x9 matrix full of 0
arr = np.zeros((9, 9))
for i in xrange(9):
    for j in xrange(9):
        arr[i, j] = int(line[i * 9 + j])

print arr
