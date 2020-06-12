# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:25:50 2016

MGenerate a random number between 1 and 9 (including 1 and 9). Ask the user 
to guess the number, then tell them whether they guessed too low, too high, 
or exactly right.  

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and 
when the game ends, print this out.


@author: Munish
"""
import random

cmpr1 = random.randint(0,9)
print (cmpr1)

num1 = 10
count = 1

while num1 != cmpr1:
       s1 = str(input("Pls enter your guess (0 to 9) [type 'exit' to quit]: "))
       if s1 is 'exit' or s1 is 'EXIT':
              break
       else:
              num1 = int(s1)
       
       if (num1 > cmpr1):
              print ("Your guess is high")
              count +=1
       elif (num1 < cmpr1):
              print ("Your guess is low")
              count +=1
       else:
              print ("You guessed correctly")
print ("It took you ", count, " guesses")