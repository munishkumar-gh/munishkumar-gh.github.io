"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Munish (3/27/17)
"""
###################################################################################
"""
Final solution: 171 found in 0.0 seconds

Use the "Gaussian Method" to detemine day of the week
Based on https://cs.uwaterloo.ca/~alopez-o/math-faq/node73.html
"""
###################################################################################
import time
from math import floor

start = time.time()

## To display table
def distab(rows):
    for row in rows:
        print row
    return

"""
Compute the number of months starting on a given day of the week in a century
"""
def calc_proper_days(day,st_yr,end_yr):
    total = 0
    delta_yr = end_yr - st_yr
    delta_month = 13
    for year in range(delta_yr+1):
        for month in range(1,delta_month):
            if day == calc_greg_cal(1, month, year):
                total += 1
    return total

def calc_greg_cal(day,month, year):
    """
    Formula: w = (d + floor(2.6*m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) mod 7 where

    d = day of the month (question ask us to start on 1st, goes to 31st)
    m = month (1 = Mar,..., 12 = Feb; Treat Jan & Feb as months of the preceding year)
    y = last 2 digits of the year (1987 has Y = 87 except Y = 86 for Jan & Feb)
    c = century (1987 has C = 19)
    w = week day (0 = sunday, ..., 6 = saturday)
    """

    d = day
    m = (month-3) % 12  ## shift the month by 3
    if m > 10: ## To account for Jan and Feb, which is in the previous year
        Y = year - 1
    else:
        Y = year
    y = Y % 100
    c = (Y - (Y % 100)) / 100

    w = (d + floor(2.6*m - 0.2) - 2*c + y + floor(y/4) + floor(c/4)) % 7
    return int(w)

st_yr = 1901
end_yr = 2000
day = 0 ## Sunday = 0, Saturday = 6
count = calc_proper_days(day,st_yr,end_yr)
elapsed = (time.time() - start)
print "Final solution: %s found in %s seconds" % (count,elapsed)
