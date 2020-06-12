# -*- coding: utf-8 -*-
## 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
## What is the sum of the digits of the number 21000?
import math
import time

"""
Soln:

Use List comprehension to convert num to string to individual digits

"""
start = time.time()

def compute(n, pow):
    sum = 0
    num = n**pow
    a = [int(d) for d in str(num)]
    print a
    for i in range(len(a)):
        sum +=a[i]
    return sum

if __name__ == "__main__":
    div = compute(2, 1000)
    elapsed = (time.time() - start)
    print "%s found in %s seconds" % (div,elapsed)
