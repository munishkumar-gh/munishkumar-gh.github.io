# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 10:40:43 2018

@author: Munish Kumar
Curve of Best Fit

"""
#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv

def extrapolation_fit(x, y):
    # get natural logarithmic data
    lx = np.log(x)
    ly = np.log(y)
    
    def eqn33(x, a, b):
         return np.exp(a + b*x**0.5)
    def eqn7121(x, a, b, c):
        return ((a+c*x)/(1+b*x))**0.5
    def eqn51(x, a, b):
        return 1/(a+b*x**0.5*lx)
    
    # optimize using the appropriate bounds. Use functionf, 
    # pass in x and y, return to popt and pcov
    # popt[0] = a, popt[1] = b
    try:
        popt, pcov = curve_fit(eqn33, x, y)
        print ('Eqn 33: y = exp(%s + %sx^0.5)' % (popt[0],popt[1]))
    except RuntimeError:
        popt = [0]*2
        print ('No convergence')
    try:
        popt, pcov = curve_fit(eqn7121, x, y)
        print ('Eqn 7121: y = sqrt((%s + %sx)/(1+%sx))' % (popt[0],popt[2],popt[1]))
    except RuntimeError:
        popt = [0]*2
        print ('No convergence')
    
    print ("----------------------------------------------------------------")
    xnew = np.linspace(0., 1, 200)
    #plt.plot(xnew, eqn33(xnew, *popt), 'r',linewidth=3)
    plt.plot(xnew, eqn7121(xnew, *popt), 'r',linewidth=3)
    return

with open("1-017B.csv", "r") as f:
    data = [row for row in csv.reader(f)]
    xd = [float(row[0]) for row in data]
    yd = [float(row[1]) for row in data]

# sort the data - 
# sorted (...., key = lambda ii: xd[ii]) means 
# sorts xd based on the value of key as applied 
# to each element of the list. 
# lambda signifies an anonymous function. In this case, 
# this function takes the single argument ii and returns 
# xd[ii] (i.e. the item at index ii in xd).
reorder = sorted(range(len(xd)), key = lambda ii: xd[ii])
xd = [xd[ii] for ii in reorder]
yd = [yd[ii] for ii in reorder]

# make the scatter plot
plt.scatter(xd, yd, s=30, alpha=0.15, marker='o')

# determine best fit line
#par = np.polyfit(xd, yd, 1, full=True)
#
#slope=par[0][0]
#intercept=par[0][1]
#xl = [min(xd), max(xd)]
#print (slope)
#print (intercept)
#yl = [slope*xx + intercept  for xx in xl]

extrapolation_fit(xd, yd)


### Not needed
# coefficient of determination, plot text
#variance = np.var(yd)
#residuals = np.var([(slope*xx + intercept - yy)  for xx,yy in zip(xd,yd)])
#Rsqr = np.round(1-residuals/variance, decimals=2)
#plt.text(.9*max(xd)+.1*min(xd),.9*max(yd)+.1*min(yd),'$R^2 = %0.2f$'% Rsqr, fontsize=30)
#
plt.xlabel("X Description")
plt.ylabel("Y Description")
#
## error bounds
#yerr = [abs(slope*xx + intercept - yy)  for xx,yy in zip(xd,yd)]
#par = np.polyfit(xd, yerr, 2, full=True)
#
#yerrUpper = [(xx*slope+intercept)+(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]
#yerrLower = [(xx*slope+intercept)-(par[0][0]*xx**2 + par[0][1]*xx + par[0][2]) for xx,yy in zip(xd,yd)]

#plt.plot(xl, yl, '-r')
#plt.plot(xd, yerrLower, '--r')
#plt.plot(xd, yerrUpper, '--r')
plt.show()

