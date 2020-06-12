
## There are 16 positive integers that do not have a zero in their digits and that have a digital sum equal to 5, namely: 
## 5, 14, 23, 32, 41, 113, 122, 131, 212, 221, 311, 1112, 1121, 1211, 2111 and 11111.
## Their sum is 17891.
##
## Let f(n) be the sum of all positive integers that do not have a zero in their digits and have a digital sum equal to n.
##
## Find summation (from i=1 to 17) of f(13^i).
## Give the last 9 digits as your answer.
##
## Codded by Munish (12/14/2016)

## Check to see if the number contains a 0 in it
def containZero(num):
    if(num == 0):
        return True
    while(num > 0):
        if(num % 10 == 0):
            return True
        num /= 10
    return False;

## Check that the sum of digits = max; returns a list of digits
def digital_sum(n, no_list, max):
    z = 0
    number = 0
    
    for z in range(0,max,1):
        number += (n/10**z)%10
    if number == max:
        no_list.append(n)

    return no_list 

## Initialization of counters
counter = 0
i = 0
zz = 0
master_sum = 0
no_list = []

############ Only change these 2 variables #########################
int_req = 17   ## Number of integers that you want to sum over

max = 13       ## Maximum sum of digits
##################################################################

while counter <int_req:
    bool = containZero(i)
    if bool is False:
        no_list = digital_sum(i, no_list, max)
        counter = len(no_list)
        i += 1
    else:
        i += 1

## Sum of all the numbers in the list
for zz in range(len(no_list)):
    master_sum +=no_list[zz]

print "The first " ,int_req, " digits with no 0 and whose sum of digits is ",max
print no_list        
print "The sum of all the numbers is " ,master_sum

