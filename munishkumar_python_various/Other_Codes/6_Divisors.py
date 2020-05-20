# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:30:39 2016
Create a program that asks the user for a number and 
then prints out a list of all the divisors of that number. 

(If you don’t know what a divisor is, it is a number that 
divides evenly into another number. For example, 13 is a 
divisor of 26 because 26 / 13 has no remainder.)

@author: Munish
"""
num = 0
x = int(input("Enter a number: "))

arr=[]

y  = range(1,x+1)
for element in y:
    num = num+1
#print y

for i in range(num):
    if (x % y[i] == 0):
        arr.append(y[i])
print arr, "is the divisor of" ,x        