# -*- coding: utf-8 -*-
##The four adjacent digits in the 1000-digit number that have the greatest
##product are 9 × 9 × 8 × 9 = 5832
##
##ind the thirteen adjacent digits in the 1000-digit number that have the
##greatest product.
##
##What is the value of this product?
##
##Munish Kumar (12/20/16)

#########################################################################
"""
This solution implements 2 duplicate arrays and checks one against the other
The 2 arrays are spliced to 13 digits each, and the products compared
This solution is not as elegent as solution 2, but it is quite fast 
"""
#########################################################################

def find_product(list_first_13, list_mv_1):
    product_list_first_13 = 1
    product_list_mv_1 = 1

    for ii in range(len(list_first_13)):
        product_list_first_13 *= list_first_13[ii]
        product_list_mv_1 *= list_mv_1[ii]
    #print (product_list_first_13)
    #print (product_list_mv_1)
    return product_list_first_13, product_list_mv_1


i = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
#print (i)

array = [int(i) for i in str(i)]
dup_array1 = array[:]
dup_array2 = array[:]
start = 0
end = 13

list_first_13 = dup_array1[start:end]
list_mv_1 = dup_array2[start+1:end+1]
print ("______Start__________")
print ("First 13 elements:", list_first_13)
print ("Move 1 element over:", list_mv_1)
print ("---------------------")

product_list_first_13, product_list_mv_1 = find_product(list_first_13, list_mv_1)

try:
    while (len(list_first_13) + len (list_mv_1)) == 26:
        if product_list_first_13 <= product_list_mv_1:
            list_first_13.pop(start) # Remove first element in first list
            dup_array1.pop(start)    # Remove first element in first duplicate list
            list_first_13.append(dup_array1[end])   # Append last element in first duplicate list to first list   
            #print ("Change 1: Next longest 13 elements:", list_first_13)
            product_list_first_13, product_list_mv_1 = find_product(list_first_13, list_mv_1)
        else:
            list_mv_1.pop(start)    # Remove first element in second list
            dup_array2.pop(start)   # Remove first element in second duplicate list
            list_mv_1.append(dup_array2[end])   # Append last element in second duplicate list to second list    
            #print ("Change 2: Next longest 13 elements:", list_mv_1)
            product_list_first_13, product_list_mv_1 = find_product(list_first_13, list_mv_1)
except IndexError:
    print ("______Solution______")
    print ("Largest String 1:", ''.join(str(x) for x in list_first_13))
    print ("Product 1:", product_list_first_13)
    print (" ")
    print ("Largest String 2:", ''.join(str(x) for x in list_mv_1))
    print ("Product 2:", product_list_mv_1)
    print ("--------------------")
    

################################################################################################
"""
Very elegent implementation
"""
################################################################################################
       
# 
# Solution to Project Euler problem 8
# by Project Nayuki
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 


# We implement a straightforward algorithm that examines every substring of length 13.
##def compute():
##	ans = max(digit_product(NUMBER[i : i + ADJACENT]) for i in range(len(NUMBER) - ADJACENT + 1))
##	return str(ans) 
##    
##
##
##def digit_product(s):
##	result = 1
##	for c in s:
##		result *= int(c)
##	return result
##
##
##NUMBER = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
##ADJACENT = 13
##
##
##if __name__ == "__main__":
##	print(compute())
        
    
    

    



    

