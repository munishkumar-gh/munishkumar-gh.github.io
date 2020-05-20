## Code by Munish (1/23/17)
## Histogram.py interface for rapidly plotting histograms
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as sp

start = time.time()

def statistics (y_delta):
    nn, min_max, mean, var, skew, kurt = sp.describe(y_delta)
    st_dev = np.sqrt(var)
    median = np.median(y_delta)
    print 'Number of elements: ' ,nn
    print 'Min: %s, Max: %s ' % (min_max[0] ,min_max[1])
    print 'Mean: ',mean
    print 'Median: ' ,median
    print 'Standard Deviation: ' ,st_dev
    print 'Variance: ',var
    print 'Skew: ',skew
    print 'Kurtosis: ',kurt
    print "----------------------------------------------------------------"
    return nn, min_max, mean, var, skew, kurt, st_dev, median

# r tells it to read the string as is
path = r'C:\Users\mkumar7\Desktop\Pyt\To_Test\Dory'
file = '\ROP_Dory_1'
extension ='.csv'
fName = path+file+extension

modat = open(fName)                         # open file with names in
rbfile = modat.readline()                   # read data file name
print rbfile
print "----------------------------------------------------------------"
D1 = np.genfromtxt(fName, delimiter=',', skip_header = 1, names = ["Depth", "TVD", "TVDSS", "ROP"])
MD = D1['Depth']
TVD = D1['TVD']
TVDSS = D1['TVDSS']
ROP = D1['ROP']
#print "MD:\n%s\n\n TVD:\n%s\n\n TVDSS:\n%s\n\n ROP:\n%s\n\n" % (MD,TVD,TVDSS,ROP)
print "Number of points:" ,len(ROP)
print "----------------------------------------------------------------"

a = 200               # Filter for ROP
b = 50                # Filter for Bins
increment = 1000        # Filter for Depth frame
lc_SPCLo = 'darkred'
linewidth = 3.0
fontsize = 16
file2 = '\Figure_'
fOut = path+file2

#--------------------------
ZZ = np.min(D1['TVD'])

while ZZ < np.max(D1['TVD']):
    
    ##Within the array D1, look for D1['ABX'] and do something. If there are
    ## 2 conditions it needs to satisfy () & () is the correct syntax
    ## (D1['ABX'] < a) filters the data to only range considered
    ## D1[(D1['ABX'] < a)]['ABX'] only plots the 'ABX' data and not all data
    DD = D1[(D1['ROP'] < a) & (D1['TVD'] < ZZ + 100) & (D1['TVD'] >= ZZ )]['ROP']
    
    print "ROP"
    nnl, min_maxl, meanl, varl, skewl, kurtl, st_devl, medianl = statistics(DD)

    plt.figure(figsize=(10,10), facecolor="white")
    plt.grid(True)

    ## Count each element (frequency) and put into bin
    ## Then sum(frequency*diff(bin)) is calculated where diff[n] = a[n+1] - a[n] for each element in array 
    ## If normed = 0, sum(frequency*diff(bin)) >> 1 i.e. the integral > 1
    ## If normed = 1, output = frequency/sum(frequency*diff(bin))
    ## Then output can still be > 1 but the sum(frequency*diff(bin)) = 1
    nl, binsl, patchesl = plt.hist(DD, bins=b, normed=1, alpha=0.4, label='ROP',
                                   histtype='stepfilled', color=lc_SPCLo)
    
    yl = matplotlib.mlab.normpdf(binsl, meanl, st_devl)
    plt.plot(binsl, yl, linestyle='-', color=lc_SPCLo, linewidth = linewidth)
   
    max_lim = (max(np.maximum.reduce([nl]))*1.1)
    plt.ylim(0,max_lim)
    
    plt.vlines(meanl, 0, max_lim, color=lc_SPCLo, linewidth=linewidth)
    plt.annotate('ROP={:.2f} m/hr'.format(meanl), xy=(meanl+0.01, 0.8*max_lim), color=lc_SPCLo, fontsize=fontsize)
    
    plt.title("Histogram of ROP per 100 m increment", fontsize=fontsize)
    plt.xlabel("Value", fontsize=fontsize)
    plt.ylabel("Normalized Frequency", fontsize=fontsize)
    plt.legend(loc='upper left', fontsize=fontsize)
    
    plt.tight_layout()
    plt.savefig(fOut + str(ZZ) + '.png', dpi=150, format='png')
    ZZ += increment
    #plt.show()

elapsed = (time.time() - start)
print "Final solution found in %s seconds" % (elapsed)
