# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:32:36 2016
Ask the user to input a list and prints out all the
elements of the list that are less than user input.
This is part of the command line argument
Prints out the data to an outfile

@author: Munish
"""
#import numpy as np
import sys
inFile = sys.argv[1]
#outFile = sys.argv[2]

num = 0

with open(inFile,'r') as i:
    #s = i.readlines() #Reads the whole line
    s = i.read()
    print s

array = map(int, s.split(','))

#a=np.zeros()
#for i in range():
#    a[i] = int(lines[i])
#print a
  
#ele = int(input("Enter a number: "))
#
#j = 0
#x=[]
#
#for i in range(num):
#     if a[i] < ele:
#        x.append(a[i])
#        j=j+1
#print x
#print "Elements <",input, 
#print "=", j           
        
#processedLines = manipulateData(lines)
#
#with open(outFile,'w') as o:
#    for line in processedLines:
#        o.write(line)







