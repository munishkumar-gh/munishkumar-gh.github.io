# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:36:02 2019

@author: Munish Kumar

The code hre takes taxt that has been input in a text file,
and turns it into csv of individual words for use with
software like Power BI for word clouds

The code removes numbers, special chracters
like (*&-//.,!?), and converts everything to lower case

"""
from collections import Counter

file = open(r"C:/Users/J0501553/AnacondaProjects/Q4_wordcount.txt", "r+", encoding="utf-8-sig")

wordcount={}
wordcount = Counter((file.read().split()))
file.close()

with open("C:/Users/J0501553/AnacondaProjects/Q4_wordcount.csv", "w") as file:
    for word, count in wordcount.items():
        if word.isalpha(): # isalpha() checks if there are only alphabetic characters in a word
            print(word.lower(), count, sep='\t,\t', file=file) #lower() will convert it to lower case



