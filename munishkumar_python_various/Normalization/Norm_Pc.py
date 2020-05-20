## Code by Munish (08/06/17)
## Norm_Pc.py for normalization of Pc curve
## Reference: Oil & Gas Science and technology, S.E.M.D Desouky
## "A New Method for Normalization of Capillary Pressure Curves"
## Rev IFP, vol 58(2003), No. 5, pp 551-556
global fName
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import plot
from scipy.cluster.vq import kmeans,vq
from scipy.optimize import curve_fit

##r tells it to read the string as is
path = r'C:\Users\mkumar7\Desktop\Pyt\To_Test\Norm_Pc_codes'
file = '\Norm_Pc'
extension='.csv'
fName = path+file+extension
fs=18
lw = 3.0
deg=1
#kclu = K-means no of clusters to test
kclu = 4

start = time.time()

## Function to read input file
def input_file_in(fName):
    modat = open(fName)                         # open file with names in
    rbfile = modat.readline()                   # read data file name
    print rbfile

    Sc1 = np.genfromtxt(fName, delimiter=',', skip_header = 2, names = ["Depth", "Por", "Perm"])
    md = Sc1["Depth"]
    por = Sc1["Por"]/100
    perm = Sc1["Perm"]
    #print "Saturation:\n%s\n\n SH Saturation:\n%s\n\n High:\n%s\n\n Low:\n%s\n\n" % (SW,SPC,SPCHi,SPCLo)
    return md, por, perm
    
## Function to fit line    
def line_fit(x,y,deg,logscale):
    if logscale == "FT":
        m,b = np.polyfit(x,np.log(y),deg)
        b = np.exp(b)
        print "Gradient = %s, Intercept = %s" % (m,b)
    elif logscale == "TF":
        m,b = np.polyfit(np.log(x),y,deg)
    elif logscale == "TT":
        #m,b = np.polyfit(np.log(x),np.log(y),deg)
        popt, pcov = curve_fit(func, np.log(x),np.log(y))
        m = popt[0]
        b = popt[1]
        b = np.exp(b)
        print "Gradient = %s, Intercept = %s" % (m,b)        
    else:
        m,b = np.polyfit(x,y,deg)
    return m,b

def func(x, m, c):
    m=1 ## Force-fit unity gradient
    return m * x + c

## Optimal number of centtroids based on Elbow plot    
def number_clusters(kclu):
    K=range(1,10)
    K_plot=[K[k]-1 for k in range(len(K))]
    KM = [kmeans(RQI,k) for k in K]
    #centroids = [cent for (cent,var) in KM]   # cluster centroids
    avgWithinSS = [var for (cent,var) in KM] # mean within-cluster sum of squares

    ##### plot ###
    kIdx = kclu

    # elbow curve
    fig = plt.figure(1, figsize=(12,12), facecolor="white")
    ax = fig.add_subplot(111)
    ax.cla()   #Updates the previously open plots 
    ax.plot(K_plot, avgWithinSS, 'k^--', markersize=fs, linewidth=lw)
    ax.plot(K[kIdx-1], avgWithinSS[kIdx], 'o', markersize=fs+10, 
        markeredgewidth=2, markeredgecolor='k', markerfacecolor='None')
    plt.grid(True)
    plt.xlabel('Number of clusters', fontsize=fs)
    plt.ylabel('Average within-cluster sum of squares', fontsize=fs)
    plt.title('Elbow for KMeans clustering', fontsize=fs)
    plt.show()
    
    return kclu
           
print "----------------------------------------------------------------"
md, por, perm = input_file_in(fName)
print "Number of points:" ,len(md)
print "----------------------------------------------------------------"

RQI = np.sqrt(perm/por)
NPI = por/(1-por)
kclu=number_clusters(kclu)
print "Number of clusters:", kclu

plt.figure(2, figsize=(12,12), facecolor="white")

plt.subplot(211)
plt.plot(por, perm, 'ro',ms=fs)
print "----------------------------------------------------------------"
m,b = line_fit(por,perm,deg=deg, logscale = "FT")
print "----------------------------------------------------------------"
plt.plot(por, b*np.exp(m*por),'b--', linewidth=lw)
plt.xscale('linear')
plt.yscale('log')
plt.xlabel("Porosity (V/V)", fontsize=fs)
plt.ylabel("Permeability (mD)", fontsize=fs)
plt.title("Porosity vs Permeability", fontsize=fs)
plt.legend(loc='upper left', fontsize=fs)
plt.grid(True)

plt.subplot(212)
plt.plot(NPI, RQI, 'ro', ms=fs)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Normalized Porosity ", fontsize=fs)
plt.ylabel("Reservoir Quality Index (microns)", fontsize=fs)
plt.tick_params(axis="both",which="both",length=6, labelcolor="k")
plt.legend(loc='upper left', fontsize=fs)
plt.grid(True)
plt.twinx()
plt.yscale('log')
plt.ylabel("Reservoir Quality Index (microns)", fontsize=fs)
plt.tick_params(axis="y",which="both",length=6, labelcolor="k")

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.tight_layout()
plt.show()

## form 2D matrix    
data = np.vstack((NPI, RQI)).T
centroids,_ = kmeans(data,kclu)
idx,_ = vq(data,centroids)

## For colour mapping - can use other color schemes for pts
cmap = matplotlib.cm.rainbow

print "----------------------------------------------------------------"
for i in range(kclu):
    cs = cmap(i / float(kclu))
    for j in range(kclu):
        try:
            # some plotting using numpy's logical indexing - data[idx==i,j]=x-values and data[idx==i,j+1]=y-values
            plot(data[idx==i,j],data[idx==i,j+1],'o',color=cs,ms=fs)
            m,b = line_fit(data[idx==i,j],data[idx==i,j+1],deg=deg, logscale = "TT")
            #plt.plot(centroids[:,0],centroids[:,1],'sm',ms=fs)
            xtrplt = np.linspace(0.1, 1, len(NPI))
            plt.plot(xtrplt, b*xtrplt**m,'--', color=cs, linewidth=lw)
            plt.annotate('FZI={:.2f}'.format(b), xy=(np.max(NPI)*1.2, b*0.95), color=cs, fontsize=fs*0.8)
        except IndexError:
            break
print "----------------------------------------------------------------"
print "Centroids:\n" ,centroids

# save specifying required format (tab separated values)
extension ='.tsv'
fOut = path+file+'_NPI_RQI'+extension
np.savetxt(fOut, np.transpose([md, por, perm, NPI, RQI, idx]), fmt='%10s\t',
    header="MD (ft)\tPorosity (%)\tPermeability (mD)\tNorm Porosity (a.u.)\tRes Qlty Indx (um)\tCluster ID", 
    comments='')

elapsed = (time.time() - start)
print "Final solution found in %s seconds" % (elapsed)