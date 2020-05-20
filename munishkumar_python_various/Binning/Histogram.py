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
fName = r'C:\Users\mkumar7\Desktop\Pyt\To_Test\Sc1.csv'             

modat = open(fName)                         # open file with names in
rbfile = modat.readline()                   # read data file name
print rbfile
print "----------------------------------------------------------------"
Sc1 = np.genfromtxt(fName, delimiter=',', skip_header = 2, names = ["SWT", "SW_PC", "SW_PC_HIGH", "SW_PC_LOW"])
SW = Sc1["SWT"]
SPC = Sc1["SW_PC"]
SPCHi = Sc1["SW_PC_HIGH"]
SPCLo = Sc1["SW_PC_LOW"]
#print "Saturation:\n%s\n\n SH Saturation:\n%s\n\n High:\n%s\n\n Low:\n%s\n\n" % (SW,SPC,SPCHi,SPCLo)
print "Number of points:" ,len(SW)
print "----------------------------------------------------------------"

a = 0.5                 # Filter for Saturation
b = 50                  # Filter for Bins 
lc_SW = 'cornflowerblue'
lc_SPC = 'orange'
lc_SPCHi = 'red'
lc_SPCLo = 'darkred'
linewidth = 3.0
fontsize = 16

## SW[SW < a] filters the data to only range considered
print "SWT"
nn, min_max, mean, var, skew, kurt, st_dev, median = statistics(SW[SW < a])
print "SW_PC"
nnc, min_maxc, meanc, varc, skewc, kurtc, st_devc, medianc = statistics(SPC[SPC < a])
print "SW_Pc_Hi"
nnh, min_maxh, meanh, varh, skewh, kurth, st_devh, medianh = statistics(SPCHi[SPCHi < a])
print "SW_Pc_Lo"
nnl, min_maxl, meanl, varl, skewl, kurtl, st_devl, medianl = statistics(SPCLo[SPCLo < a])

plt.figure(figsize=(10,10), facecolor="white")
plt.grid(True)

## Count each element (frequency) and put into bin
## Then sum(frequency*diff(bin)) is calculated where diff[n] = a[n+1] - a[n] for each element in array 
## If normed = 0, sum(frequency*diff(bin)) >> 1 i.e. the integral > 1
## If normed = 1, output = frequency/sum(frequency*diff(bin))
## Then output can still be > 1 but the sum(frequency*diff(bin)) = 1
n, bins, patches = plt.hist(SW[SW < a], bins=b, normed=1, alpha=1, label='SWT', histtype='stepfilled', color=lc_SW)
y = matplotlib.mlab.normpdf(bins, mean, st_dev)
plt.plot(bins, y, linestyle=':', color=lc_SW, linewidth = linewidth)

nc, binsc, patchesc = plt.hist(SPC[SPC < a], bins=b, normed=1, alpha=0.8, label='SW_PC', histtype='stepfilled', color=lc_SPC)
yc = matplotlib.mlab.normpdf(binsc, meanc, st_devc)
plt.plot(binsc, yc, linestyle='-.', color=lc_SPC, linewidth = linewidth)

nh, binsh, patchesh = plt.hist(SPCHi[SPCHi < a], bins=b, normed=1, alpha=0.6, label='SW_PC_HIGH', histtype='stepfilled', color=lc_SPCHi)
yh = matplotlib.mlab.normpdf(binsh, meanh, st_devh)
plt.plot(binsh, yh, linestyle='--', color=lc_SPCHi, linewidth = linewidth)

nl, binsl, patchesl = plt.hist(SPCLo[SPCLo < a], bins=b, normed=1, alpha=0.4, label='SW_PC_LOW', histtype='stepfilled', color=lc_SPCLo)
yl = matplotlib.mlab.normpdf(binsl, meanl, st_devl)
plt.plot(binsl, yl, linestyle='-', color=lc_SPCLo, linewidth = linewidth)

max_lim = int(max(np.maximum.reduce([n,nc,nh,nl]))+5)
plt.ylim(0,max_lim)

plt.vlines(mean, 0, max_lim, color=lc_SW, linewidth=linewidth)
plt.annotate('SWT={:.2f}'.format(mean), xy=(meanl+0.01, 0.95*max_lim), color=lc_SW, fontsize=fontsize)
plt.vlines(meanc, 0, max_lim, color=lc_SPC, linewidth=linewidth)
plt.annotate('SW_PC={:.2f}'.format(meanc), xy=(meanl+0.01, 0.9*max_lim), color=lc_SPC, fontsize=fontsize)
plt.vlines(meanh, 0, max_lim, color=lc_SPCHi, linewidth=linewidth)
plt.annotate('SW_PC_High={:.2f}'.format(meanh), xy=(meanl+0.01, 0.85*max_lim), color=lc_SPCHi, fontsize=fontsize)
plt.vlines(meanl, 0, max_lim, color=lc_SPCLo, linewidth=linewidth)
plt.annotate('SW_PC_Low={:.2f}'.format(meanl), xy=(meanl+0.01, 0.8*max_lim), color=lc_SPCLo, fontsize=fontsize)


plt.title("Histogram of Water Saturation", fontsize=fontsize)
plt.xlabel("Value", fontsize=fontsize)
plt.ylabel("Normalized Frequency", fontsize=fontsize)
plt.legend(loc='upper left', fontsize=fontsize)

plt.tight_layout()
plt.show()

elapsed = (time.time() - start)
print "Final solution found in %s seconds" % (elapsed)
