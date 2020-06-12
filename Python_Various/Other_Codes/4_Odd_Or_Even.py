# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:00:46 2016

Ask the user for a number. Depending on whether 
the number is even or odd, print out an appropriate message 
to the user.

Extras:
a) If the number is a multiple of 4, print out a different message.
b) Ask the user for two numbers: one number to check (call it num) 
and one number to divide by (check). If check divides evenly 
into num, tell that to the user. If not, print a 
different appropriate message.

@author: Munish
"""
digit = int(input("Enter a number: "));
print digit

if digit % 2 == 0:
    print digit, "is an even number";
    if digit % 4 == 0:
        print digit, "is also a multiple of 4";
else:
    print digit, "is an odd number";
    
num = int(raw_input("Enter a second number: "));

if digit % num == 0:
        print digit, "is evenly divisible by ",num
else:
    print digit, "is not evenly divisible by ",num
    
