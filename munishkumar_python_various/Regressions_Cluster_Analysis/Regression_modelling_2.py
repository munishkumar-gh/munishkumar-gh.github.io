### Scales
global xaxisscale
global yaxisscale
global xaxislabel
global yaxislabel
global setlogscale

xaxisscale = 0.5
yaxisscale = 10000
xaxislabel = 'Porosity (V/V)'
yaxislabel = 'Permeability (mD)'
setlogscale = 0 ## set to 1 for log scale plots

#########################
"""
Regression Modelling: Munish Kumar (1/12/17)
Based on http://ipython-books.github.io/featured-04/
"""
import time
import numpy as np
import scipy.stats as st
from scipy.optimize import curve_fit
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import sys

start = time.time()

## Calculates the best straight line fit through the data
def fit_polynomial(x, y, exponent):
    if exponent == 0: # calculate polynomial; constrained
       # x needs to be a column vector instead of a 1D vector for this
        z = x[:,np.newaxis]
        aHat, _, _, _, = np.linalg.lstsq(z, y)
        print ('Fit equation through origin is :%4.4f*x' % (aHat))
        print ("----------------------------------------------------------------")
        f = np.poly1d([aHat,0])
    else:
        # calculate polynomial; unconstrained
        z = np.polyfit(x, y, exponent)     ## Least squared poly fit
        f = np.poly1d(z)                   ## Calculate new points
        aHat = z[0]
        bHat = z[1]
        # summarize the results
        print ('Unconstrained fit equation is :%4.4f*x + %4.4f' % (aHat,bHat))
        print ("----------------------------------------------------------------")
    return f

## Calculates the best polynomial fit through the data
def linear_regression(reg_model, a, b, f, x, y, xx, n):
    # linspace returns evenly spaced numbers over a specified interval.
    x_tr = np.linspace(0., xaxisscale, 200)
    y_tr = f(x_tr)
    ## Debugging
    #print x_tr[100], len(x_tr)
    #print y_tr[100], len(y_tr)

    # Create the model
    lr = lm.LinearRegression()

    ## Ordinary Least Squares regression through origin
    if reg_model == 0:
        lr = lm.LinearRegression(fit_intercept = False)
        reg_model = 1

    ## Ordinary Least Squares regression
    if reg_model == 1:
        # Train the model on the training dataset.
        lr.fit(x[:, np.newaxis], y);
        # Predict points with our trained model.
        y_lr = lr.predict(x_tr[:, np.newaxis])
        coef = lr.coef_
        intercept = lr.intercept_
        print ('Linear Regression - Total number of coefficients: ', len(lr.coef_))
        #print 'Coefficient: ' + (' '.join(['%.6f' % c for c in lr.coef_]))
        #print 'Intercept:' ,lr.intercept_
        y_tr_LCI, y_tr_UCI = confidence_interval(x_tr, y_tr, coef, intercept, x, y, xx, n)
        plotfigure(x_tr, y_tr, y_lr, y_tr_LCI, y_tr_UCI, 0, 1, x, y)

    ## Polynomial interpolation with linear regression
    ## Use Vandermonde matrix to pre-compute exponents of data points
    ## See http://math.stackexchange.com/questions/481845/regression-with-a-vandermonde-matrix
    if reg_model == 2:
        for deg, s in zip([a, b], ['-', '.']):
            lr.fit(np.vander(x, deg + 1), y);
            y_lr = lr.predict(np.vander(x_tr, deg + 1))
            coef = lr.coef_
            intercept = lr.intercept_
            print ('Polynomial interpolation with linear regression - Total number of coefficients: ', len(lr.coef_))
            #print 'Coefficient: ' + (' '.join(['%.6f' % c for c in lr.coef_]))
            #print 'Intercept:' ,lr.intercept_
            y_tr_LCI, y_tr_UCI = confidence_interval(x_tr, y_tr, coef, intercept, x, y, xx, n)
            plotfigure(x_tr, y_tr, y_lr, y_tr_LCI, y_tr_UCI, 1, deg, x, y)

    ## Ridge Regression = Polynomial interpolation with linear regression
    ## but with an additional regularization term to loss function
    if reg_model == 3:
        ridge = lm.RidgeCV()
        for deg, s in zip([a, b], ['-', '.']):
            ridge.fit(np.vander(x, deg + 1), y);
            y_lr = ridge.predict(np.vander(x_tr, deg + 1))
            coef = ridge.coef_
            intercept = ridge.intercept_
            print ('Ridge regression - Total number of coefficients: ', len(ridge.coef_))
            #print 'Coefficient: ' + (' '.join(['%.6f' % c for c in ridge.coef_]))
            #print 'Intercept:' ,ridge.intercept_
            y_tr_LCI, y_tr_UCI = confidence_interval(x_tr, y_tr, coef, intercept, x, y, xx, n)
            plotfigure(x_tr, y_tr, y_lr, y_tr_LCI, y_tr_UCI, 2, deg, x, y)
    return

## Power law curve fit
def power_law(x, y):
    # get natural logarithmic data
    lx = np.log(x)
    ly = np.log(y)

    def f(x, N, a):
        return N * x ** (a)

    def f2(x, N, a):
        return N * np.exp(x * (a))

    def f3(x, N, a):
        return a * x ** N

    def f_log(x, lN, a):
        return lN + a * x

    def f_log3(x, N, lna):
        return lna + N * x

    # optimize using the appropriate bounds. Use functionf, pass in x and y, return to popt and pcov
    # popt[0] = N, popt[1] = a
    try:
        popt, pcov = curve_fit(f, x, y)
        print ('Power law: y = %s*x^%s' % (popt[0],popt[1]))
    except RuntimeError:
        popt = [0]*2
        print ('No convergence')
    try:
        popt_log, pcov_log = curve_fit(f_log, lx, ly)
        print ('Logarithamic Fit on x and y: ln y = ln %s + %s* ln x' % (np.exp(popt_log[0]),popt_log[1]))
    except RuntimeError:
        popt_log = [0]*2
        print ('No convergence')
    try:
        popt_log1, pcov_log1 = curve_fit(f_log, x, ly)
        print ('Exponential Fit/ Log fit on y: y = %s*e^(%s*x)' % (np.exp(popt_log1[0]),popt_log1[1]))
    except:
        popt_log1 = [0]*2
        print ('No convergence')
    try:
        popt_log2, pcov_log2 = curve_fit(f_log3, lx, y)
        print ('Logarithmic Fit on x: y = %s* ln x + %s' % (popt_log2[0], popt_log2[1]))
    except RuntimeError:
        popt_log2 = [0]*2
        print ('No convergence')
    print ("----------------------------------------------------------------")
    xnew = np.linspace(0., xaxisscale, 200)
    # plot the data
    plt.figure(figsize=(8,8));
    plt.title("Power Law Fit")
    plt.grid(True)
    if setlogscale == 1:
        plt.yscale('log')
    plt.plot(x, y, 'oy', ms=6);
    plt.plot(xnew, f(xnew, *popt), 'r',linewidth=3) ## Nx**a
    plt.plot(xnew, f(xnew, np.exp(popt_log[0]), popt_log[1]), '-k',linewidth=3)
    plt.plot(xnew, f2(xnew, np.exp(popt_log1[0]), popt_log1[1]), '--m',linewidth=3)
    plt.xlim(0., xaxisscale); ## User define upper and lower limit
    plt.ylim(0., yaxisscale);
    plt.xlabel(xaxislabel)
    plt.ylabel(yaxislabel)
    plt.legend(['Data', 'Nx^a','ln a + b* ln x', 'Ne^(xa)'], loc = 'lower right')
    plt.show()
    return

## Code to evaluate confidence intervals
def confidence_interval(x_tr, y_tr, coef, intercept, x, y, xx, n):
    alpha = 1 - 0.95
    b1 = coef  ## Gradient
    b0 = intercept ## Intercept
    s2 = 1./n * sum([(y[i] - b0 - b1 * x[i])**2 for i in range(n)]) ## Standard dev
    print ('Gradient:',str(b1), ', Intercept:',str(b0), ', Standard Deviation:',str(s2))
    print ("***************************************************************************************************************************")

    c = -1 * st.t.ppf(alpha/2.,n-2)
    bb1 = c * (s2 / ((n-2) * (xx.mean() - (x.mean())**2)))**.5
    lower_bb1 = b1-bb1
    upper_bb1 = b1+bb1
    print ('The 95% confidence interval of the exponents of the polynomial is: ',lower_bb1, upper_bb1)

    bb0 = c * ((s2 / (n-2)) * (1 + (x.mean())**2 / (xx.mean() - (x.mean())**2)))**.5
    lower_bb0 = min(b0-bb0)
    upper_bb0 = max(b0+bb0)
    print ('The 95% confidence interval of intercept is: ',lower_bb0, upper_bb0)

    c1 = st.chi2.ppf(alpha/2.,n-2)
    c2 = st.chi2.ppf(1-alpha/2.,n-2)
    lower_s2 = n*s2/c2
    upper_s2 = n*s2/c1
    print ('The 95% confidence interval of the standard deviation is: ',lower_s2, upper_s2)
    print ("***************************************************************************************************************************\n")

    x_tr_CI = x_tr
    y_tr_LCI = []
    y_tr_UCI = []
    ysum = 0
    yysum = 0
    m = len(b1)
    for i in range(len(x_tr)):
        for j in range (len(b1)):
            if m == 1:
                m+=1
            ysum += lower_bb1[j]*x_tr_CI[i]**(m-(j+1))
            yysum += upper_bb1[j]*x_tr_CI[i]**(m-(j+1))
            ## Debugging
            #print lower_bb1[0],lower_bb1[1], len(b1)-(j+1)
        ysum = ysum + lower_bb0
        yysum = yysum + upper_bb0
        y_tr_LCI.append(ysum)
        y_tr_UCI.append(yysum)
        ysum = 0
        yysum = 0
    ## Debugging
    #print x_tr_CI[100], len(x_tr_CI)
    #print y_tr_LCI[100], len(y_tr_LCI)
    #print y_tr_UCI[100], len(y_tr_UCI)
    return y_tr_LCI, y_tr_UCI

## Code to plot figure
def plotfigure(x_tr, y_tr, y_lr, y_tr_LCI, y_tr_UCI, reg_model, deg, x, y):
    plt.figure(figsize=(8,8))
    if (reg_model == 0):
        plt.title("Linear regression");
    if (reg_model == 1) or (reg_model == 2) :## 1 = w/o Regularization, 2 = w Regularization
        plt.title("Polynomial Regression: Degree " +str(deg))
    if setlogscale == 1:
        plt.yscale('log')
    plt.plot(x, y, 'oy', ms=6)
    plt.plot(x_tr, y_tr, '--k',linewidth=3)
    plt.plot(x_tr, y_lr, 'g',linewidth=3)
    plt.plot(x_tr, y_tr_LCI, 'b--',linewidth=1)
    plt.plot(x_tr, y_tr_UCI, 'b--',linewidth=1)
    #plt.xlim(0, x.max()+1)
    #plt.ylim(0, y.max()+1)
    plt.xlim(0., xaxisscale) ## User define upper and lower limit
    plt.ylim(0., yaxisscale)
    plt.xlabel(xaxislabel)
    plt.ylabel(yaxislabel)
    plt.grid(True)
    plt.legend(['Data', 'Constrained','Unconstrained','Confidence limit (95%)'], loc = 'lower right')
    plt.show()
    return

def getgoing(fName, clus_fit, exponent, reg_model, a, b, clus_tot):
    ##----------------Input Data----------------##
    ## 3 column format - x, y and cluster label
    ## CSV file with comma seperated variables
    #dataset = np.genfromtxt('C:\\Users\\mkumar7\\Desktop\\Pyt\\To_Test\\cluster_label_sorted.csv', delimiter=',', skip_header=1)
    dataset = np.genfromtxt(fName, delimiter=',', skip_header=1)
    x_ori = dataset[:, 0]
    y_ori = dataset[:, 1]
    clus_label = dataset[:, 2]
    value = clus_fit ## Cluster under investigation

    ## Creates a mask and only plot over the clustered intervals
    xtemp = np.ma.masked_array(x_ori, mask = (clus_label != value))
    ytemp = np.ma.masked_array(y_ori, mask = (clus_label != value))
    x = xtemp.compressed()
    y = ytemp.compressed()

    xx = x*x
    n = len(x)
    ##Debugging:
    #print "Core porosity:\n%s\n\n Log Porosity:\n%s" % (x,y)
    print ("Number of points loaded:" ,n)
    print ("Fitting through Cluster:" ,value)
    print ("----------------------------------------------------------------")

    ## 0 = Estimate solution through origin
    ## 1 = linear regression, unconstrained
    ## Note: exponent = 0/1 and reg_model = 0/1 will give the same answer
    ## Keep exponent to '0' as default
    #exponent = 0
    if clus_tot > 1:
        f = fit_polynomial(x, y, exponent)

    ## 0 = linear regression through origin,
    ## 1 = linear regression (unconstrained),
    ## 2 = Polynomial interpolation (w/o regualarization),
    ## 3 = Polynomial Regression (w regularization)
    ## Set a and b to get range of polynomial fits e.g. a = 1 is 1st order polynomial
    ## Output will be the exponents for the regression
    ## Reg_model = '3', a=2 and b=3 is default
    #linear_regression(reg_model = 3, a=1, b=2)
    if clus_tot > 1:
        linear_regression(reg_model, a, b, f, x, y, xx ,n)

    ## Compute a power law fit through data
    if clus_tot > 1:
        power_law(x, y)

    ## All the data, respective of the cluster
    if clus_tot-value == 1:
        xx_ori = x_ori*x_ori
        n_ori = len(x_ori)
        f_ori = fit_polynomial(x_ori, y_ori, exponent)
        linear_regression(reg_model, a, b, f_ori, x_ori, y_ori, xx_ori ,n_ori)
        power_law(x_ori, y_ori)
    return

if __name__ == "__main__":
    getgoing(fName, clus_fit, exponent, reg_model, a, b, clus_tot)
    count = "Solution"
    elapsed = (time.time() - start)
    print ("%s found in %s seconds" % (count,elapsed))
