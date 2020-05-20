# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 13:25:50 2016

Make a two-player Rock-Paper-Scissors game. 

(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)


@author: Munish
"""
import random

def rockpapersci(x):
       ## Function to compare human input vs computer input
       global ans_p1, ans_p2
       comp_mv = random.randint(1, 3)

       ## Player 1 selects rock
       ## Player 2 selects paper
       if x == 1 and comp_mv == 2:
              print ("Oops - Player 2 has chosen " , comp_mv, "You Lose!")
              ans_p2 +=1
       ## Player 2 selects scissors
       elif x == 1 and comp_mv == 3:
              print ("Congratulations - Player 2 has chosen " , comp_mv, "You Win!")
              ans_p1 +=1
       
       ## Player 1 selects Paper
       ## Player 2 selects Scissors
       elif x == 2 and comp_mv == 3:
              print ("Oops - Player 2 has chosen " , comp_mv, "You Lose!")
              ans_p2 +=1
       ## Player 2 selects Scissors
       elif x == 2 and comp_mv == 1:
              print ("Congratulations - Player 2 has chosen " , comp_mv, "You Win!")
              ans_p1 +=1
       
       ## Player 1 selects Scissors
       ## Player 2 selects Rock
       elif x == 3 and comp_mv == 1:
              print ("Oops - Player 2 has chosen " , comp_mv, "You Lose!")
              ans_p2 +=1
       ## Player 2 selects Paper
       elif x == 3 and comp_mv == 2:
              print ("Congratulations - Player 2 has chosen " , comp_mv, "You Win!")
              ans_p1 +=1              
       else:
              print ("Its a tie.")
       return ans_p1, ans_p2

print ("______________________________________")
print ("Welcome to rock-paper-scissors. You are player 1")
print ("Your opponent is the computer - Player 2")

continue_game = 0
ans_p1 = 0
ans_p2 = 0

while continue_game == 0:
       s = int(input("Player 1: enter 1 for rock, 2 for paper or 3 for scissors: "))
       ans_p1, ans_p2 = rockpapersci(s)
#       print (ans_p1, ans_p2)
       cont = str(input("Player 1 do you want to continue [Y/N]:"))
       if cont is 'n' or cont is 'N':
              continue_game = 1

print ("______________________________________")
print ("The score is: Player 1 has" , ans_p1, "points and Player 2 has" , ans_p2)
if ans_p1 > ans_p2:
       print ("You beat the computer")
elif ans_p1 < ans_p2:
       print ("Better luck next time")
else:
      print ("You are tied")
print ("______________________________________")