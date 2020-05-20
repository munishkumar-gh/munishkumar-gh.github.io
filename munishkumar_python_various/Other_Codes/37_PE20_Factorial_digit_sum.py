# -*- coding: utf-8 -*-
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Munish (3/27/17)
"""
###################################################################################
"""
Final solution: 648 found in 0.0 seconds
"""
###################################################################################
import time

start = time.time()

## To display table
def distab(rows):
    for row in rows:
        print row
    return

def magic(interim):
    sum_tot = 0
    list_num = [int(i) for i in str(interim)] ##using list comprehensions
    for k in range(len(list_num)):
        sum_tot +=list_num[k]
    return sum_tot

def factorial(n):
    new_res = 1
    for i in range(1,n+1):
        new_res *= i
    return new_res

interim = factorial(100)
print(interim)
count = magic(interim)

elapsed = (time.time() - start)
print "Final solution: %s found in %s seconds" % (count,elapsed)
