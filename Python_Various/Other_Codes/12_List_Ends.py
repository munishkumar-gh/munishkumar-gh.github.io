# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:58:54 2016

Write a program that takes a list of numbers (for example, 
a = [5, 10, 15, 20, 25]) and makes a new list of only the 
first and last elements of the given list. 

For practice, write this code inside a function.

@author: Munish
"""

def list_out (aa):
       num_a = 0
       bb = []*2

       for element_a in aa:
              num_a = num_a+1
       print (num_a)

       for i in range(num_a):
              if i == 0:
                     bb.append(aa[i])
              elif i == num_a-1:
                     bb.append(aa[-1])
              else:
                     i +=1
       return bb
       
usr_lst = []
usr_lst = input("Please enter a series of numbers:" )
aa = eval(usr_lst) ## Using eval this way is very dangerous! But it works
#print (aa)

out = list_out(aa)
print (out)

