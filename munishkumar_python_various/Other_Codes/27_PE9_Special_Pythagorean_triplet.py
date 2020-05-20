# -*- coding: utf-8 -*-
## A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##
## a^2 + b^2 = c^2
## For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
##
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.
##
## Munish Kumar (12/20/16)

#########################################################################
"""
was not able to solve this :(

The trick was 2 'for' loops but the second for loop uses a decrementing window
within range (which I forgot you could do!!)
"""
#########################################################################

import time

start = time.time()

for num in range(1, 1000):
    for dig in range(num, 1000 - num):
        i = 1000 - num - dig
        if num * num + dig * dig == i * i:
            print(num, dig, i)
            print("Product: {}".format(num * dig * i))

elapsed = time.time() - start               
print("Time: {:.5f} seconds".format(elapsed))








        

        
        
        
        

    
    
