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

## Returns a list of valid words.
def load_words():
    
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

## Load a random word
def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

## Words are strings of lowercase letters.
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

## Ask user for password length
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

## Generate the password
def password_generator(n, pass_lvl):
       word = random_word(wordlist)
       wordup = word.upper().replace('A','a').replace('E','e').replace('I','i').replace('O','o').replace('U','u')

       i = 0
       c = len(word)
       
       if pass_lvl == 2:
           #pass_word_gen = word[c:inc].join(random.choice(string.ascii_lowercase + string.digits) for i in range(n))
           #random_char = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(n))
           random_char = ''.join(random.choice(string.digits) for i in range(n))
           pass_word_gen = ''.join(word[:c] + random_char[c:])
           print "Your Password of strength [Moderate] is: ",pass_word_gen
       else:
           #pass_word_gen = ''.join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation) for i in range(n))
           random_char = ''.join(random.choice(string.digits + string.punctuation) for i in range(n))
           pass_word_gen = ''.join(wordup[:c] + random_char[c:])
           pass_word_gen = pass_word_gen.strip(" ")
           print "Your Password of strength [Strong] is: ",pass_word_gen
       return pass_word_gen

## Execution Time
def diff_time(t0, t1):
       total = t1 - t0       
       print "Your Password took ", total, "micro-secs to generate"
       return total
  
## Determine strength of password
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

## Start time of code
t0 = timeit.default_timer()

## Generate a weak password
wordlist = load_words()
if pass_lvl == 1:
        word = random_word(wordlist)
        if is_word(wordlist, word):
              print "Your Password of strength [Weak] is: ",word
else: ## moderate and strong password
       n = length_password(pass_lvl)                      
       password_generator(n, pass_lvl)

## End time of code
t1 = timeit.default_timer()
diff_time(t0,t1)
       












                      
