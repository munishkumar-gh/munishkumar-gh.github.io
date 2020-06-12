# -*- coding: utf-8 -*-
## Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (in txt file)
## Munish Kumar (01/10/17)

#########################################################################
"""
Soln: 5537376230 (0.0499999523163 seconds)
Loaded in the numbers in matrix format; then used list comprehension to
convert each line of matrix from str to int and sum over each line

Total number generated was:
5537376230390876637302048746832985971773659831892672


"""
#########################################################################
import time

start = time.time()

## Concatenate via list comprehensions
def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s
    
array = []
count = 0

## Create a 50x100 matrix
table = [[0 for i in range(50)] for j in range(100)]

with open("PE13_Large_Sum.txt", "r") as txt:
    for line in txt:
        #print "First and last element is %s and %s respectively," % (line[0]+line[1],line[-2]+line[-1]) 
        for numbersint in list(line.rstrip('\n')):
            array.append(numbersint)    
    print "Number of elements read in array:", len(array)
    #print array
    for i in range(100):
        for j in range(50):
            try:
                table[i][j]=int(array[i*50+j])
            except IndexError:
                pass

## Pass each row in table to function which concatenates and sums 
for row in table:
    s = magic(row)
    count +=s

elapsed = (time.time() - start)
print "%s found in %s seconds" % (count,elapsed)
