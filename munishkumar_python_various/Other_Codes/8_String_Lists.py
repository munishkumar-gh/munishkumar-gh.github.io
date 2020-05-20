# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:47:35 2016

Ask the user for a string and print out whether this 
string is a palindrome or not. (A palindrome is a 
string that reads the same forwards and backwards.)

NOTES:
# creates a string of any length depending on x
mkstring = lambda(x): "".join(map(chr, (ord('a')+(y%26) for y in range(x))))
print mkstring (50)

mod_string = []
mod_string.append(x_string)

# if x_string is passed to mod_string, it becomes 
# 1 element in the string
for e in mod_string:
    print mod_string
print len(mod_string)

# if x_string is just treated as a list of char
# then it has 'n' no of chars. But does not let you handle
# individual elements in the string
for e in x_string:
    print x_string
print len(x_string)   

@author: Munish
"""
## Soln 1:
count = 0
count2 = 0

xx_string = str(raw_input("Enter a statement:").lower())
x_string=''.join(xx_string.split())
count = len(x_string)

## Only way to create a new string, as string are immutable i.e. tuples
mkstring=''.join(reversed((x_string)))
print mkstring, x_string
count2 = len(mkstring)

if count != count2:
    print "Error in lengths of strings"
else: 
    for i in range(count):
        print x_string[i], mkstring[i]
        if mkstring[i] != x_string[i]:
            print "This is not a palindrome"
            break
        if i == count-1:
            print "This is a palindrome"

###########################################################################

## Soln 2:
#a = str(raw_input("enter a word "))
#
#if a[:] == a[::-1]:
#    print("This is a palindrome")
#else:
#    print("This is not a palindrome")

     
