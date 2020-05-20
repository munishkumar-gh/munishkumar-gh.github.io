# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 17:54:05 2016

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@author: Munish
"""

num = 600851475143
max = 600851475143

counter = 0
list_prime_fac = []
product = 1

for counter in range(0,max,1):
       if counter == 0:
              counter += 1
              list_prime_fac.append(1)
       elif counter >0:
              if num % counter == 0:
                     list_prime_fac.append(counter)
                     num = num/counter
       else:
              counter += 1
       
       if num == 1:
              break

print (list_prime_fac)