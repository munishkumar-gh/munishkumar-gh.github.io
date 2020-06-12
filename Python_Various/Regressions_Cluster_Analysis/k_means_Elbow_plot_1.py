"""
K-means Cluster Analysis: Munish Kumar (1/16/17)
2 different cluster methods applied
Results appear to be the same

Explanation of Elbow Plot:

Used with K-means, which is a simple unsupervised machine learning algorithm 
that groups a dataset into a user-specified number (k) of clusters. 
The K-means algorithm is naive i.e it clusters the data into k clusters, even 
if k is not the right number of clusters to use. Therefore, when using k-means 
clustering, the right number of clusters need to be tested for.

The method implemented here to validate the number of clusters is the 
elbow method. The idea is to run k-means clustering on the dataset for a 
range of values of k (say, k from 1 to 10 in the examples above), and for 
each value of k calculate the sum of squared errors (SSE).

A line chart of the SSE for each value of k is tehn plotted. If the line chart 
looks like an arm, then the "elbow" on the arm is the value of k that is the 
best. The goal is a small SSE; however, SSE tends to decrease toward 0 as we 
increase k. Ultimately, there comes a point of diminishing return. k should 
be small enought such that it has a low SSE, and this is usually the elbow.


"""
global xlblname
global ylblname

xlblname = 'Porosity (V/V)'
ylblname = 'Permeability (mD)'

import time
import numpy as np
from scipy.cluster.vq import kmeans,vq, whiten
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import sys

start = time.time()

def getgoing(fName, clus_tot, k0, kn):
    # load the dataset
    ## Debugging
    #fName = 'C:\\Users\\mkumar7\\Desktop\\Pyt\\To_Test\\stmalo4_nd.txt'
    fp = open(fName)
    X = np.loadtxt(fp,skiprows=2)
    fp.close()
    print ('Total number of points loaded: ', len(X))

    ##### cluster data into K=1..N clusters #####
    K = range(k0,kn)

    # scipy.cluster.vq.kmeans; whiten normalizes data so each feature has unit variance
    #KM = [kmeans(whiten(X),k) for k in K]
    KM = [kmeans(X,k) for k in K]
    centroids = [cent for (cent,var) in KM]   # cluster centroids
    avgWithinSS = [var for (cent,var) in KM] # mean within-cluster sum of squares

    # alternative: scipy.spatial.distance.cdist
    #D_k = [cdist(whiten(X), cent, 'euclidean') for cent in centroids]
    D_k = [cdist(X, cent, 'euclidean') for cent in centroids]
    cIdx = [np.argmin(D,axis=1) for D in D_k]
    dist = [np.min(D,axis=1) for D in D_k]
    #avgWithinSS = [sum(d)/X.shape[0] for d in dist]

    ##### plot ###
    kIdx = clus_tot

    # elbow curve
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(K, avgWithinSS, 'b*-')
    ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=18,
        markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
    plt.grid(True)
    plt.xlabel('Number of clusters')
    plt.ylabel('Average within-cluster sum of squares')
    plt.title('Elbow for KMeans clustering')

    # scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)
    clr = ['b','g','r','c','m','y','k','orange','azure','ivory','indigo','gold','maroon','lime','salmon','plum','tan','silver','teal','olive','violet' ]
    for i in range(K[kIdx]):
        ind = (cIdx[kIdx]==i)
        ax.scatter(X[ind,0],X[ind,1], s=30, c=clr[i], label='Cluster %d'%i)
        #ax.set_yscale('log')
    plt.xlabel(xlblname)
    plt.ylabel(ylblname)
    plt.title('KMeans clustering with K=%d' % K[kIdx])
    plt.legend(loc=2)
    plt.grid(True)
    plt.show()

    ###write out the data; verbose = 1 for details of process
    km = KMeans(n_clusters=kIdx+1, init='random', max_iter=100, n_init=1, verbose=0)
    km.fit(X)
    labels = km.predict(X)
    clusters = {}
    n = 0
    for item in labels:
        if item in clusters:
            clusters[item].append(X[n])
        else:
            clusters[item] = [X[n]]
        n +=1

    with open('cluster_label_sorted.csv', 'w') as f:
        f.write("NA X Y Cluster_Label\n")
        for item in clusters:
            #print "Cluster ", item
            for i in clusters[item]:
                #print i
                f.write("%-10s %-10s\n" % (str(i), str(item)))

    count = "Solution"
    elapsed = (time.time() - start)
    print ("%s found in %s seconds" % (count,elapsed))
    return

if __name__ == "__main__":
    getgoing(fName, clus_tot)
