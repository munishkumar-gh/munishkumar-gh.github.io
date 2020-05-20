# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:26:43 2016

Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. Take this opportunity to think about how you can 
use functions. Make sure to ask the user to enter the number of numbers in 
the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of 
numbers where the next number in the sequence is the sum of the previous 
two numbers in the sequence. The sequence looks like 
this: 1, 1, 2, 3, 5, 8, 13, …)

@author: Munish
"""

def fibnac(seq):
       if seq == 0 or seq == 1:
              return 1
       else:
              return fibnac(seq-1) + fibnac(seq-2)
                     

def testfib(seq):
       bb = []
       for i in range(seq):
#              print ("The Fibonacci sequence for" ,seq, "is " , fibnac(i))
              bb.append(fibnac(i))
       return (bb)

aa = []
seq = int(input("How many Fibonnaci numbers do you want to generate?: "))
aa = testfib(seq)
print (aa)