# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:34:28 2016

Write a password generator in Python. Be creative with how you generate 
passwords - strong passwords have a mix of lowercase letters, uppercase 
letters, numbers, and symbols. The passwords should be random, generating 
a new password every time the user asks for a new password. 

Include your run-time code in a main method.

Ask the user how strong they want their password to be. 
For weak passwords, pick a word or two from a list.

@author: Munish
"""
import random
import string
import timeit

WORDLIST_FILENAME = "words.txt"

##Load a random word

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
        Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def is_word(wordlist, word):
    """
    Determines if word is a valid word.
    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def length_password(pass_lvl):
       while True:       
              try:
                     n = int(input("Select password length (min = 10, max = 30): "))
              except ValueError: # just catch the exceptions you know!
                     print 'That\'s not a number!'
              else:
                     if 10 <= n <= 30:
                            break
                     else:
                            print 'Out of range. Try again'
       return n

def password_generator(n, pass_lvl):
       i = 0
       if pass_lvl == 2:
              pass_word_gen = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(n))
       else:
              pass_word_gen = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation) for i in range(n))
              pass_word_gen = pass_word_gen.strip(" ")
       return pass_word_gen

def diff_time(t0, t1):
       total = t1 - t0       
       print "Your Password took ", total, "micro-secs to generate"
       return total

  
## Making sure the user enters a number in a certain range
while True:
   try:
       pass_lvl = int(input("Select password strength [1 - Weak, 2 - Moderate, 3 - Strong]: "))
   except ValueError: # just catch the exceptions you know!
       print 'That\'s not a number!'
   else:
       if 1 <= pass_lvl <= 3:
           break
       else:
           print 'Out of range. Try again'

## Will also time the execution of the code
t0 = timeit.default_timer()
## Generate a weak password
if pass_lvl == 1:
       wordlist = load_words()
       word = random_word(wordlist)
       if is_word(wordlist, word):
              print "Your Password of strength [Weak] is: ",word
else:
       n = length_password(pass_lvl)                      
       pass_word_gen = password_generator(n, pass_lvl)
       print pass_word_gen

t1 = timeit.default_timer()
diff_time(t0,t1)
       












                      
