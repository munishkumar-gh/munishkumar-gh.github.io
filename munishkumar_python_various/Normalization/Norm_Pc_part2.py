import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import itertools

start = time.time()

## Part 1: Read a file, plot the Pc curves as clustered data
path = r'C:\Users\mkumar7\Desktop\Pyt\To_Test\Norm_Pc_codes'
file = '\Norm_Pc_P2'
extension='.csv'
fName = path+file+extension

n = 1000
inc = 3
skip_header = 6
fs = 18
lw = 3

conc_RPC  = np.array(0,dtype = 'f8')
conc_SW  = np.array(0, dtype = 'f8')
conc_CN = np.array(0, dtype = 'f8')
tempData = []

## Quick read to get all data 3 cols at a time as well as max cluster
for i in range(0,n,inc):
    try:
         wb = np.genfromtxt(fName, delimiter=',', skip_header = skip_header, 
                            usecols=(i,i+1,i+2), 
                            names = ["res_pc", "Sw", "cluster"])
         tempData.append(wb)
         CN = wb["cluster"]
         RPC = wb["res_pc"]
         conc_CN = np.append(conc_CN, CN)
         conc_RPC = np.append(conc_RPC, RPC)
    except  (IndexError, ValueError):
        MAX_cn = int(np.nanmax(conc_CN[1:]))
        a = np.nanmin(conc_RPC[1:])
        b = np.nanmax(conc_RPC[1:])+100
        print "Maximum cluster number:" ,MAX_cn
        print "Min and Max Pc: (%s, %s)" %(a,b)
        break
        
## allData is a 2D array, with each index in the array determined 
## by allData[i][j], with max j = 2
allData = np.concatenate(tempData)
print "length of Array:",len(allData)

## Fill missings
for i in range(len(allData)):
    if np.isnan(allData[i][2]) == False:
        elem = allData[i][2]
    else:
        allData[i][2] = elem

## For colour mapping - can use other color schemes for pts
cmap = matplotlib.cm.rainbow
kclu = MAX_cn+1
marker = itertools.cycle(('o', '*', '8', 'd', 'h', 'x', 'p', '^', '+', 'v', '<', '>'))
label = []

for i in range(kclu):
    cZ= allData[allData['cluster']==i]
    cs = cmap(i / float(kclu))
    label.append("Flow unit "+str(i))
    mc=marker.next()
    
    ##------------------
    fig = plt.figure(1,figsize=(12,12), facecolor="white")
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(cZ['Sw'], cZ['res_pc'], linestyle='None', marker=mc, color=cs, markersize=fs/2,
             linewidth=lw, label=label[i])
    ## NOT EFFICIENT - plots each and very point vs using the structured array
    #for j in range(len(cZ)):
    #    ax1.plot(cZ[j][1], cZ[j][0], marker=mc, color=cs, 
    #            markersize=fs/2, linewidth=lw, label=label[i])
    ax1.set_ylim(a,b)
    ax1.set_yscale('log')
    ax1.set_xlabel('Wetting Phase Saturation (V/V)', fontsize=fs)
    ax1.set_ylabel('Reservoir Pressure (Air-Brine) (psi)', fontsize=fs)    
    ax2=ax1.twinx()
    ax3=ax1.twiny()
    ax2.set_yscale('log')
    ax2.set_ylabel('Reservoir Pressure (Air-Brine) (psi)', fontsize=fs)
    ax2.set_ylim(a,b)
    plt.title('Capillary Pressure Curve', fontsize=fs)
    plt.grid(True)
    legend = ax1.legend(loc='upper right', shadow=True)
    plt.tight_layout()
    plt.show()
    ##------------------

##----------------------------------------------------------------------------
## Part 2: Read a 2nd file with RQI data, calculate J-fn

topline= np.genfromtxt(fName, delimiter=',',  max_rows = 1)
temp_tl = topline[np.logical_not(np.isnan(topline))]
combData = []

file2 = '\Norm_Pc_NPI_RQI'
extension='.tsv'
fName2=path+file2+extension
wb2 = np.genfromtxt(fName2, delimiter='\t', skip_header = 1, usecols=(0,4), 
                    names = ['MD','RQI'])
combData.append(wb2)
xy_val = np.concatenate(combData)
RQI_data = np.array(0, dtype = 'f8')

for i in range(len(allData)):
    for j in range(len(temp_tl)):
        try:
            if xy_val[i][0] == temp_tl[j]:
                RQI_data = np.append(RQI_data,xy_val[i][1])
        except IndexError:
            break

sigma = 72
theta = 0
Swr = 0
i=1
calc=[] 
calc2=[] 
J_data=[]

## tempdata is a 3 index structured array
## tempData[0] selects the first array element in the structured array
## tempData[0][0] selects the first list of the first array element 
## tempData[0][0][0] selects the first item within the first list 
## USEFUL trick - indexing a structured array
## J[:,0] means take all the rows and copy the first column only
for j in range(len(tempData)):
    calc.append(0.21654*(tempData[j]['res_pc']*RQI_data[i])/(sigma*np.cos(theta)))
    calc2.append((tempData[j]['Sw']-Swr)/(1-Swr))
    i+=1

calc=np.concatenate(calc)
calc2=np.concatenate(calc2)
J_data = np.column_stack((calc,calc2,allData['cluster']))

for i in range(kclu):
    cZ= J_data[J_data[:,2]==i]
    cs = cmap(i / float(kclu))
    label.append("Flow unit "+str(i))
    mc=marker.next()
    
    ##------------------
    fig = plt.figure(2,figsize=(12,12), facecolor="white")
    ax2 = fig.add_subplot(1,1,1)
    ax2.plot(cZ[:,1], cZ[:,0], linestyle='None', marker=mc, color=cs, markersize=fs/2,
             linewidth=lw, label=label[i])
    ax2.set_ylim(a,b)
    ax2.set_yscale('log')
    ax2.set_xlabel('Normalized Water Saturation (au)', fontsize=fs)
    ax2.set_ylabel('Values of J (au)', fontsize=fs)    
    ax2=ax1.twinx()
    ax3=ax1.twiny()
    ax2.set_yscale('log')
    ax2.set_ylabel('Values of J (au)', fontsize=fs)
    ax2.set_ylim(a,b)
    plt.title('J-fn vs Normalized Sw', fontsize=fs)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    ##------------------

## Write File Out
#fOut = path+file+'_testtest'+extension
#np.savetxt(fOut, np.transpose([allData]), fmt='%10s\t',
#    header="MD (ft)\tPorosity (%)\tPermeability (mD)\tNorm Porosity (a.u.)\tRes Qlty Indx (um)\tCluster ID", 
#    comments='')            

elapsed = (time.time() - start)
print "Final solution found in %s seconds" % (elapsed)