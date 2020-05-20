## Code by Munish (1/23/17)
## Main.py interface for running other programs
"""
Step 0:
----------
Data prep. Run Log-Lan 'filter-data'; this will generate a csv file. Then edit said csv as follows:

1) Delete all blanks as follows (if any):
Select the entire column. On 'Home' tab in excel, click "Find & Select" and choose Go To Special.
Select "Blanks" and click OK. Right-click on one of the empty calls, and choose Delete... from the menu.
Select Entire row, and click the OK button.

1a) Convert to V/V or % (if necessary)

1b) Copy and paste 2 columns of interest into txt file. Call it "run_step_a.txt"

Now open cmd in MS-DOS and go to path where script main.py is located (will also need the other 2 py scripts
or executables). Run as follows:
python main.py >> summary.log

Step 1:
----------
Run k-means clustering; it tells you the optimal number of clusters, based on an elbow plot.
The code iterates from 1 to 20 possible clusters (clus_tot); 2 is the minimum

Default is clus_tot = 3 (this will give 3 clusters); this number is variable depening on the results
[Check the result by running k_means_tk_0 (external to script)]
Input: clust_tot, <myFiles>.txt. 2 columns only
Output: cluster_label_sorted.csv

Step 2:
----------
Regression Analysis through generated Clusters

**At this stage, open the csv document and do a text to column, delimited, with all the options selected.
Under others, use ']'

Exponent:
0 = Estimate solution through origin [default]
1 = linear regression, unconstrained

Reg_model:
0 = linear regression through origin,
1 = linear regression (unconstrained),
2 = Polynomial interpolation (w/o regualarization),
3 = Polynomial Regression (w regularization) [default]
Set a and b to get range of polynomial fits e.g. a = 1 is 1st order polynomial
[Default: a=2, b=3]
Note: exponent = 0/1 and reg_model = 0/1 will give the same answer

"""

## To Edit
run_step_a = 'T'                ## 'T' for Step 1 - 'F' for run Step 2
myFiles_load = ['Core_PT1ST1.txt']      ## File Name
clus_tot = 5                    ## Change number of cluster
k0 = 1                          ## minimum cluster size
kn = 20                         ## minimum cluster size
exponent = 0                    ## Linear Model
reg_model = 3                   ## Regression Model
a = 1                           ## Poly order
b = 2                           ## Poly order

##---------------DO NOT EDIT except where marked-----------------------
import k_means_Elbow_plot_1
import Regression_modelling_2
import os

def run_code(myFiles):
    pathlen = os.getcwd()
    for filename in myFiles:
        fName = os.path.join(pathlen, filename)
        print (fName)
    return fName

if __name__ == '__main__':
    if run_step_a == 'T':
        run_step_b = 'F'
    else:
        run_step_b = 'T'

    if run_step_a == 'T':
        fName = run_code(myFiles_load)
        if clus_tot > 0:
            k_means_Elbow_plot_1.getgoing(fName, clus_tot-1, k0, kn)
        else:
            print ('Invalid Cluster number')

    if run_step_b == 'T':
        """
        Loads the cluster file generated from step 1 - remember to follow ** under step 2
        """
        myFiles = ['cluster_label_sorted.csv'] ## Edit file name (if needed)
        fName = run_code(myFiles)


        for clus_fit in range(0, clus_tot):
            (Regression_modelling_2.getgoing(fName, clus_fit, exponent, reg_model, a, b, clus_tot))
              
