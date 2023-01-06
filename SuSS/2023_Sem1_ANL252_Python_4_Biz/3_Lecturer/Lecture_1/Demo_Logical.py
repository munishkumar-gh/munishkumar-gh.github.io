# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 08:12:25 2022

@author: mkumar
"""

# Python program to demonstrate
# logical and operator
  
a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("At least one number is not greater than 0")