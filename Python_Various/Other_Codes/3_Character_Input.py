# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:44:09 2016
@author: Munish

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)

"""
import datetime
now = datetime.datetime.now()
print "We are in the year", now.year;

x = str(raw_input("Please enter your name: "));
y = str(raw_input("Please enter your year of birth: "));
z = (int(y) + 100) - int(now.year)
print x, " will turn 100 in ",z, "years, in the year", int(y)+100

i = int(raw_input("Please enter a number from 1-9: "));
for j in range(i):
    print x, " will turn 100 in ",z, "years, in the year", int(y)+100

