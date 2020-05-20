# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:56:57 2016

Let’s say I give you a list saved in a variable: 
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 

Write one line of Python that takes this list 
a and makes a new list that has only the even 
elements of this list in it.

@author: Munish
"""
## Method 1
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#print a

#str = []

#for element in a:
#    if element%2 ==0:
#        str.append(element)
#print str

## Method 2 - modified so that asks for user input to the list
# Line does not work as expected - it strips all the commas and combines
#numbers to single str
#aa = str(raw_input("Enter a list of numbers:" )).replace(',','')

aa = raw_input("Enter a list of numbers:" )
aa = eval(aa) ## Using eval this way is very dangerous! But it works

b = [element for element in aa if element % 2 == 0]
print b


