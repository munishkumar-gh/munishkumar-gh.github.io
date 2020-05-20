import time
import numpy as np
import math
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

## Truncates array to end-1 elements
def average(arr1, arr2, arr3, n):
    end =  n * int(len(arr1)/n)
    ##1st array
    trunc1 = arr1[:end].reshape(-1, n)
    nn1, min_max1, mean1, var1, skew1, kurt1, st_dev1, median1 = statistics (trunc1)

    trunc2 = arr2[:end].reshape(-1, n)
    nn2, min_max2, mean2, var2, skew2, kurt2, st_dev2, median2 = statistics (trunc2)

    trunc3 = arr3[:end].reshape(-1, n)
    nn3, min_max3, mean3, var3, skew3, kurt3, st_dev3, median3 = statistics (trunc3)

    ## Weightage to apply to output
    num = np.sum(st_dev3)
    den = st_dev3
    weightage = num/den
    print "Weightage of each point:", weightage.astype(int)
    for i in range (len(weightage)):
        out1 = np.repeat(np.mean(trunc1, 1),weightage[i])
        out2 = np.repeat(np.mean(trunc2, 1),weightage[i])
        out3 = np.repeat(np.mean(trunc3, 1),weightage[i])
    return out1, out2, out3

##----------------Input Data----------------##
## Multiple column format
## CSV file with comma seperated variables
dataset = np.genfromtxt('C:\\Users\\mkumar7\\Desktop\\Pyt\\To_Test\\all_pts.csv', dtype = None, delimiter=',', skip_header=2, names = ["a", "b", "c", "d", "e", "f"])
# sort column 1 and column 0
dataset.sort(order=["b", "d"])

well_ori = dataset['a']   ## a
tops_ori = dataset['b']   ## b
md_ori = dataset['c']     ## c
tvdss_ori = dataset['d']  ## d
cpor_ori = dataset['e']   ## e
ckha_ori = dataset['f']   ## f
value = 'Lower Miocene' ## Field under investigation
value2 = 'Upper Miocene'
value3 = 'Middle Miocene'

### Creates a mask and only plot over the clustered intervals
mask = (tops_ori != value) & (tops_ori != value2) & (tops_ori != value3)

#welltemp = np.ma.masked_array(well_ori, mask = (tops_ori != value))
welltemp = np.ma.masked_array(well_ori, mask)
topstemp = np.ma.masked_array(tops_ori, mask)
mdtemp = np.ma.masked_array(md_ori, mask)
tvdsstemp = np.ma.masked_array(tvdss_ori, mask)
cportemp = np.ma.masked_array(cpor_ori, mask)
ckhatemp = np.ma.masked_array(ckha_ori, mask)

### Creates a mask and only plot over the clustered intervals
well = welltemp.compressed()
tops = topstemp.compressed()
md = mdtemp.compressed()
tvdss = tvdsstemp.compressed()
cpor = cportemp.compressed()
ckha = ckhatemp.compressed()

##Debugging:
print "Showing tops: %s, %s" % (value, value2)
print "Number of points loaded:" , len(tops)
print "----------------------------------------------------------------"
ds_md, ds_tvdss, ds_cpor = average(md.astype(float), tvdss.astype(float), cpor.astype(float), 10)

# save specifying required format (tab separated values)
#np.savetxt("C:\\Users\\mkumar7\\Desktop\\Pyt\\To_Test\\sorted.tsv", np.transpose([ds_md, ds_tvdss, ds_cpor, ds_ckha]), fmt='%10s\t', header="MD (ft)\tTVDSS (ft)\tPorosity (%)\tPermeability (mD)", comments='')
np.savetxt("C:\\Users\\mkumar7\\Desktop\\Pyt\\To_Test\\sorted.tsv", np.transpose([ds_md, ds_tvdss, ds_cpor]), fmt='%10s\t', header="MD (ft)\tTVDSS (ft)\tPorosity (%)\t", comments='')

count = "Solution"
elapsed = (time.time() - start)
print "%s found in %s seconds" % (count,elapsed)
