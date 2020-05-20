# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:04:01 2016

@author: Munish
"""
n=10
filename = 'Case_'
counter1 = 1
counter2 = 2
list1 = []
list2 = range(n)    #random number, given len needed
for x in list2:
    counter1 = str(counter1)
    full_name = (filename+counter1)
    list1.append(full_name)
    counter1 = counter2
    counter2+=1

for x in list1:
    print(x)