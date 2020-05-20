# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:57:58 2016

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only 
the elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure 
this out at this point - we’ll get to it soon)

@author: Munish
"""
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#num=[]
#for i in a:
#    if i in b and i not in num :
#        num.append(i)
#print(num)

import random
a=random.sample(range(100),10)
b=random.sample(range(100),15)

c = []
d = []

print (a)
print (b)

num_a = 0
num_b = 0
num_c = 0

for element_a in a:
    num_a = num_a+1
#print num_a

for element_b in b:
    num_b = num_b+1
#print num_b

for i in range(num_a):
    for j in range(num_b):
        if (a[i] == b[j] and a[i] not in c):
            c.append(b[j])
print (c)

