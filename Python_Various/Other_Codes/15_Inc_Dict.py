# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:33:20 2016

@author: Munish
"""
import collections

d={}
n=10
for x in range(1,n):
        d["Case {0}".format(x)]=x

od = collections.OrderedDict(sorted(d.items()))

#For older Python versions
#for k, v in od.iteritems():

#For Python 3 only
for k, v in od.items(): 
       print (k, v)
       