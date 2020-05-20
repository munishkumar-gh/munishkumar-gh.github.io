## If we list all the natural numbers below 10 that are multiples of 3 or 5,
## we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
## Find the sum of all the multiples of 3 or 5 below 1000.
##
## Code Written by Munish (12/15/2016)
##

## Function to get multiples of input(num) and output to list
def get_multiple(num, list_no):
    num_ch1 = 3 ## Editable
    num_ch2 = 5 ## Editable
 
    if num % num_ch1 == 0 or num % num_ch2 == 0:
        list_no.append(num)

    return list_no

max = 1000 ## Editable
list_no = []
num = 1
multiple = 0

while num < max:
    list_no = get_multiple(num, list_no)
    num += 1
#print list_no

# Sum of elements in list
for i in range(len(list_no)):
    multiple += list_no[i]

print "The sum of all the multiples is" ,multiple
