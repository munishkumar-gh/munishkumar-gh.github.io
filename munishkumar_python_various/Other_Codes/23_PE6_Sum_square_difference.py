# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:50:48 2016

The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.

@author: Munish 
"""

#######################Comments########################
"""
This solution is based on the following mathematical equations:

1) Sum of natural numbers = n(n+1)/2 where n is the number of terms
2) Sum of squares of natural numbers = (n)(n+1)(2n+1)/6
"""
#######################################################

def sum_natural_sq(max):
       sum_natural = max*(max+1)/2
       sum_nat_sq = sum_natural**2
       return sum_nat_sq

def sum_sq(max):
       squared = max*(max+1)*(2*max+1)/6
       return squared

max = 100
delta = sum_natural_sq(max) - sum_sq(max)
print (delta)