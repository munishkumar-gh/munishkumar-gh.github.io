# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 22:20:54 2016

Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.

@author: Munish
"""

def no_duplicate_list(aa):
       bb = aa[:]
       cc = []
       
       for i in range (len(aa)):
              for j in range(len(bb)):
                     if aa[i] != bb[j] and aa[i] not in cc and bb[i] not in cc:
                            cc.append(aa[i])
       return cc
       
def no_dup_set(aa):
       names = set()
       for i in range(len(aa)):
              names.add(aa[i])
       names_ordered = list(names)
       return names_ordered

       
aa = []
aa = input("Enter a list of elements (strings or int):")
#Test cases
#aa = ['str', 12, 13, 15, 'str', 'monkey', 15, 'str', 200, 2000, 'monkey', 'str', 'super']
#aa = ['abc',0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0,'bca']
#aa = ['munish', 'is', 'here', '!', '!', '!', '!', '!', '!']

count = len(aa)
#print (count)

print(no_duplicate_list(aa))
print(no_dup_set(aa))