# -*- coding: utf-8 -*-
## In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
## What is the greatest product of four adjacent numbers in the same direction (up, down,
## left, right, or diagonally) in the 20×20 grid?
## Munish Kumar (01/05/17)


#########################################################################
"""
Soln: 70600674

Utilization of brute force algorithm; check for 4 conditions:
1) L --> R
2) U --> D
3) SW facing diagonal
4) SE facing diagonal

"""
#########################################################################
import time
 
start = time.time()

array = []
max_pd = []

## Create a 20x20 matrix
table = [[0 for i in range(20)] for j in range(20)]

with open("PE11_matrix.txt", "r") as txt:
    for line in txt:
        print "First element and last element is %s and %s respectively," % (line[0]+line[1],line[-2]+line[-1]) 
    for numbersint in list(line.split(" ")):
        array.append(numbersint)
    for i in range(20):
        for j in range(20):
            try:
                table[i][j]=int(array[i*20+j])
            except ValueError:
                pass

## To display the table
##for row in table:
##    print row

for i in range(0,20):
    for j in range (0,20):
        try:
            multiple1 = table[i][j]*table[i][j+1]*table[i][j+2]*table[i][j+3] ## L--> R
            ##multiple2 = table[j][i]*table[j][i+1]*table[j][i+2]*table[j][i+3]  ## R--> L; redundant
            multiple3 = table[i][j]*table[i+1][j+1]*table[i+2][j+2]*table[i+3][j+3] ## SE facing diagonal
            multiple4 = table[i][j]*table[i-1][j+1]*table[i-2][j+2]*table[i-3][j+3] ## SW facing diagonal
            max_pd.append(max(multiple1, multiple3, multiple4))
        except IndexError:
            pass

max_prod = max(max_pd)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (max_prod,elapsed)
