# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:52:30 2016

Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except 
with the words in backwards order. For example, say I type the string:

My name is Michele

Then I would see the string:

Michele is name My

shown back to me.

@author: Munish
"""

def reverse_order(result):
       counter = 0
       listofstrings = []

       counter = len((result))

       for i in range(0,counter):
              listofstrings.append(result[counter-1-i])
#              print (result[i])
#              print (listofstrings[i])
       output = " ".join(listofstrings)
       return output


string1 = input("Enter a string: ")
result = string1.split(" ")
#print (result[0]) ##prints first element in string1 - test
#print (len(result)) ##prints length of split string - test

output = reverse_order(result)
print (output)