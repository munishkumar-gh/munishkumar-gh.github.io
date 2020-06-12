# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:32:36 2016
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the
elements of the list that are less than 5.

Extras:

a) Instead of printing the elements one by one, make a new 
list that has all the elements less than 5 from this 
list in it and print out this new list.
b) Write this in one line of Python.
c) Ask the user for a number and return a list that contains 
only elements from the original list a that are smaller 
than that number given by the user.

@author: Munish
"""
num = 0
j = 0

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print a
for element in a:
    num = num+1

input = int(input("Enter a number: "))
    
x = []

for i in range(num):
     if a[i] < input:
        #x = a[i]
        x.append(a[i])
        j=j+1
print x
print "Elements <",input, 
print "=", j

