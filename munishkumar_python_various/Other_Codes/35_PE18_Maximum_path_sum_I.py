# -*- coding: utf-8 -*-
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
Munish (3/27/17)
"""
###################################################################################
"""
Final solution: 1074 found in 0.00999999046326 seconds

The sums traveling from top to bottom will be the same as the sums traveling from
bottom to top. Start at the second to bottom row, and for each number $N$ in that
row, do the following: Take the maximum of the numbers directly down and left or
down and right from $N$, and add that to $N$. Now do the same for the third-to-last
row, then fourth-to-last, and so on. We’re modifying the triangle as we go to
produce maximum partial sums from the bottom, and the last stage will be to
replace to top number in the triangle, which will then be the maximum sum.

Solution is based on work from:
http://code.jasonbhill.com/python/project-euler-problem-18/

"""
###################################################################################
import time

start = time.time()

def sumrows(rowsnew,rowlen):
    # Counting elements in a single row
    for i in range(len(rowsnew[rowlen])):
        rowsnew[rowlen][i] += max(rowsnew[rowlen+1][i], rowsnew[rowlen+1][i+1])
    distab(rowsnew)
    # Base case
    if len(rowsnew[rowlen]) == 1:
        return rowsnew[rowlen][0]
    else:
        return sumrows(rowsnew, rowlen-1)

## To display table
def distab(rows):
    for row in rows:
        print row
    return

# read in the data
rows = []
with open("PE18_triangle.txt", "r") as txt:
    for line in txt:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
    #print rows
    print "Number of lines in matrix: ", len(rows)

distab(rows)

count = sumrows(rows, len(rows)-2)
#count = "Solution"
elapsed = (time.time() - start)
print "Final solution: %s found in %s seconds" % (count,elapsed)
