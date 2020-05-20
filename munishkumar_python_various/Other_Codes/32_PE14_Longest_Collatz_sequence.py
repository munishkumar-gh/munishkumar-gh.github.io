# -*- coding: utf-8 -*-
## The following iterative sequence is defined for the set of positive integers:
## n → n/2 (n is even)
## n → 3n + 1 (n is odd)
##
## Using the rule above and starting with 13, we generate the following sequence:
##
## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
## It can be seen that this sequence (starting at 13 and finishing at 1)
## contains 10 terms. Although it has not been proved yet (Collatz Problem),
## it is thought that all starting numbers finish at 1.
##
## Which starting number, under one million, produces the longest chain?
##
## NOTE: Once the chain starts the terms are allowed to go above one million.
## Munish Kumar (01/10/17)

#########################################################################
"""
Soln: 524 found in 45.4700000286 seconds
837799 is the value for this max length

"""
#########################################################################
import time

start = time.time()

n0 = 999999
n = n0
n1 = n0
count = 0
counter_list = []

while (n0 > 0):
    while (n1>1):
        if n1%2 == 0:
            n1 = n1/2
            count +=1
        elif n1%2 == 1:
            n1 = 3*n1+1
            count +=1
        else:
            print "Error"
    if (n1 == 1):
        counter_list.append(count)
        count = 0
        n1 = n0 - 1
        n0 = n1
    #print len(counter_list)

max_len = max(counter_list)
value = n - counter_list.index(max(counter_list))
elapsed = (time.time() - start)
print "%s found in %s seconds" % (max_len,elapsed)
print "%s is the value for this max length" % (value)

## More efficient solution
## Cache any Collatz numbers for integers below one million. The idea is
## that we can use the cached values to make calculations of new Collatz numbers
## more efficient. But, we don’t want to record every single number in the Collatz
## sequences that we’ll be using, because some of the sequences actually reach up
## into the hundreds of millions. We’ll make a list called TO_ADD, and we’ll only
## populate that with numbers for which Collatz lengths are unknown. Once known,
## the Collatz lengths will be stored for repeated use.

#import time
#
#start = time.time()
#
#limit = 1000000
#collatz_length = [0] * limit
#collatz_length[1] = 1 # Create a list, at index 1, let value = 1
#max_length = [1,1]    # Another list, at index 0 and 1, let value = 1 each
#
#for i in range(1,1000000):
#    n,s = i,0
#    TO_ADD = [] # collatz_length not yet known
#    while n > limit - 1 or collatz_length[n] < 1:
#        TO_ADD.append(n)
#        if n % 2 == 0: n = n/2
#        else: n = 3*n + 1
#        s += 1
#    # collatz_length now known from previous calculations
#    p = collatz_length[n]
#    for j in range(s):
#        m = TO_ADD[j]
#        if m < limit:
#            new_length = collatz_length[n] + s - j
#            collatz_length[m] = new_length
#            if new_length > max_length[1]: max_length = [i,new_length]
#
#elapsed = (time.time() - start)
#print "found %s at length %s in %s seconds" % (max_length[0],max_length[1],elapsed)
