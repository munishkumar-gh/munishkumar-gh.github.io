# -*- coding: utf-8 -*-
## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
## Find the sum of all the primes below two million.
##
## Munish Kumar (01/03/17)

#########################################################################
"""
I used the sieve of Eratosthenes formulation BUT it only works up
to 19999. The main problem is the array gets too large.

"""
#########################################################################

##import time
##
##start = time.time()
##
##num_list = []
##start = 0
##end = 199999
##el = 2
##product = 0
##
##for i in range(start, end):
##    num_list.append(el)
##    el +=1
##num_list.pop(end-1)
##
##print ("Start of list:", num_list[start])
##print ("End of list:", num_list[-1])
##print ("Length of list:", len(num_list))
##
##for num in range(2, int((end)**0.5)):
##    if num_list[num] > 0: 
##        for j in range(num**2, end, num):
##            try:
##                num_list.remove(j)
##            except ValueError:
##                pass
##print("Third element of prime list:", num_list[-3])
##print("Second element of prime list:", num_list[-2])
##print("Last element of prime list:", num_list[-1])
##
##for i in range (0, len(num_list)):
##    product +=num_list[i]
##
##print("Sum of all primes in list less than 2 million:", product)
###print("Product: {}".format(num * dig * i))
##elapsed = (time.time() - start)              
##print("Time: {:.5f} secconds".format(elapsed))

#########################################################################
"""
Nayuki uses a solution using the eulerlib function (which I did not know about)

"""
#########################################################################
##import eulerlib
##
### Call the sieve of Eratosthenes and sum the primes found.
##def compute():
##	ans = sum(eulerlib.list_primes(1999999))
##	return str(ans)
##
##
##if __name__ == "__main__":
##	print(compute())

#########################################################################
"""
Jason uses a solution based on a prime sieve, which is similar to my approach
but implemented corrected and more elegently

The idea is that we’ll make a list having length longer than the
expected value of the largest prime, then we’ll set the value of items in the
list to True or False depending on whether they are known to be prime in the
following way: Set 2 to True, but then set all multiples of 2 to False. Set 3
to True, but then set all multiples of 3 to False. And so on.

In the end, we’ll simply look for the item in the list having value True, as
this will be the primes needed to get the sum.

"""
#########################################################################
import time

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            # sieve out non-primes by multiples of known primes
            # // is floor division where digits after decimal pt
            # are removed
            # The list is spliced; start at ind*2, and get every
            # other ind.
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum
 
start = time.time()
sum = prime_sum(2000000)
elapsed = (time.time() - start)
 
print "found %s in %s seconds" % (sum,elapsed)


        

        
        
        
        

    
    
