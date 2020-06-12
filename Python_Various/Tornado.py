"""
Created on Thu Dec  1 18:12:00 2016

@author: Munish Kumar
"""

import numpy as np 
import matplotlib.pyplot as plt 

########### Global Variables ################################################
########### Editable ########################################################

## Assume the following hard-coded mid-pts
global a; a = 1.0
global m; m = 2.0
global n; n = 2.0
global PHIT; PHIT = 0.25
global RW; RW = 0.044 #RW @ 25 Deg C
global temp; temp = 175 #Temp is in Deg C

## hard-code hydrocarbon resistivity value
global RT; RT = 2

## Size of Distribution - larger the number, the more continuous the tornado plot appears
global no_cases; no_cases = 20

#############################################################################

def normalize(lst):
    a = []
    s = max(lst) - min(lst)
    for i in range (len(lst)):
        a.append((float(lst[i]) - min(lst))/s)
    return a

def Water_Sat_Calc(lst, calc_case_in):
    SWT_aa = []
    for i in range (len(lst)):
        if calc_case_in == 0: #a
            SWT_aa.append(((lst[i]*RW)/((PHIT**m)*RT))**(1/n))
        elif calc_case_in == 1: #m
            SWT_aa.append(((a*RW)/((PHIT**lst[i])*RT))**(1/n))
            #print lst[i]
        elif calc_case_in == 2: #n
            SWT_aa.append(((a*RW)/((PHIT**m)*RT))**(1/lst[i]))
        elif calc_case_in == 3: #PHIT
            SWT_aa.append(((a*RW)/((lst[i]**m)*RT))**(1/n))
        elif calc_case_in == 4: #RW
            SWT_aa.append(((a*lst[i])/((PHIT**m)*RT))**(1/n))
    for i in range (len(lst)):
        if SWT_aa[i] > 1:
            SWT_aa[i] = 1
    return SWT_aa

########################### Editable ##########################
## calc_case and/ or Calc_case_alpha indicate the following####
## 0 - plot a
## 1 - plot m
## 2 - plot n
## 3 - plot PHIT
## 4 - plot RW

calc_case = 1
calc_case_alpha = 4

##Archie = [ 
##    'a', 
##    'm', 
##    'n', 
##    'PHIT', 
##    'RW',
##    ] 
##############################################################

filename = 'Case_'
counter1 = 1
counter2 = 2
Archie = []
list2 = range(no_cases)    # random number, given len needed
for x in list2:
    counter1 = str(counter1)
    full_name = (filename+counter1)
    Archie.append(full_name)
    counter1 = counter2
    counter2+=1
    
num_Archie = len(Archie)

## Convert RW to correct Temp using Arps equation
RW = RW*(25+21.5)/(temp+21.5)
print 'Rw converted at reservoir temp of',temp, 'Deg C is ', RW, 'ohmm.'

## Determine Fractional change of Archie variables
Multiplier = np.random.uniform(low = 0.5, high=2.5, size=num_Archie)  # Extract multiplier frm uniform dist, multiply to Archie variable

## Calculate 1st saturation scenario based on Archie
SWT_base = ((a*RW)/((PHIT**m)*RT))**(1/n)
print 'SWT base case is', SWT_base

if calc_case == 0: #Vary a
    new_cases =  Multiplier*a # New cases
    new_cases.sort() # Sort ascending order
    nc = normalize(new_cases) # Normalize between 0 - 1
    SWT = Water_Sat_Calc(new_cases, calc_case)
elif calc_case == 1: #Vary m
    new_cases = Multiplier*m
    new_cases.sort()
    nc = normalize(new_cases)
    SWT = Water_Sat_Calc(new_cases, calc_case)
elif calc_case == 2: #Vary n
    new_cases =  Multiplier*n
    new_cases.sort()
    nc = normalize(new_cases)
    SWT = Water_Sat_Calc(new_cases, calc_case)
elif calc_case == 3: #Vary PHIT
    new_cases = Multiplier*PHIT
    new_cases.sort()
    nc = normalize(new_cases)
    SWT = Water_Sat_Calc(new_cases, calc_case)
elif calc_case == 4: #Vary RW
    new_cases = Multiplier*RW   
    new_cases.sort()
    nc = normalize(new_cases)
    SWT = Water_Sat_Calc(new_cases, calc_case)

## Calculate 2nd saturation scenario based on Archie
if calc_case_alpha == 0:
    new_cases_alpha =  Multiplier*a 
    new_cases_alpha.sort()
    nc_alpha = normalize(new_cases_alpha) 
    SWT_alpha = Water_Sat_Calc(new_cases_alpha, calc_case_alpha)
elif calc_case_alpha == 1:
    new_cases_alpha =  Multiplier*m 
    new_cases_alpha.sort()
    nc_alpha = normalize(new_cases_alpha)
    SWT_alpha = Water_Sat_Calc(new_cases_alpha, calc_case_alpha)
elif calc_case_alpha == 2:
    new_cases_alpha =  Multiplier*n 
    new_cases_alpha.sort()
    nc_alpha = normalize(new_cases_alpha)
    SWT_alpha = Water_Sat_Calc(new_cases_alpha, calc_case_alpha)
elif calc_case_alpha == 3:
    new_cases_alpha =  Multiplier*PHIT 
    new_cases_alpha.sort()
    nc_alpha = normalize(new_cases_alpha)
    SWT_alpha = Water_Sat_Calc(new_cases_alpha, calc_case_alpha)
elif calc_case_alpha == 4:
    new_cases_alpha =  Multiplier*RW 
    new_cases_alpha.sort()
    nc_alpha = normalize(new_cases_alpha)
    SWT_alpha = Water_Sat_Calc(new_cases_alpha, calc_case_alpha)

# force these values where the labels happen to make sure they are positioned nicely 
##nc_alpha[-1] = 0.8 
##nc_alpha[-2] = 0.6 
##SWT_alpha[-1] = 0.7 

# bars centered on the y axis 
pos = np.arange(num_Archie) + .5 

# make the left and right axes 
fig = plt.figure(facecolor='white', edgecolor='none')
ax_minusSw = fig.add_axes([0.05, 0.1, 0.35, 0.8]) 
ax_plusSw = fig.add_axes([0.6, 0.1, 0.35, 0.8]) 

ax_minusSw.set_xticks(np.arange(0, 1.01, 0.1)) 
ax_plusSw.set_xticks(np.arange(0, 1.01, 0.1)) 

# turn off the axes spines except on the inside y-axis 
for loc, spine in ax_minusSw.spines.iteritems(): 
    if loc!='right': 
        spine.set_color('none') # don't draw spine 

for loc, spine in ax_plusSw.spines.iteritems(): 
    if loc!='left': 
        spine.set_color('none') # don't draw spine 

# just tick on the top 
ax_minusSw.xaxis.set_ticks_position('top') 
ax_plusSw.xaxis.set_ticks_position('top') 

# make the -ve graphs 
ax_minusSw.barh(pos, nc, align='center', 
facecolor='#DBE3C2', edgecolor='None') 
ax_minusSw.barh(pos, SWT, align='center', facecolor='#7E895F', 
height=0.5, edgecolor='None') 
ax_minusSw.set_yticks([]) 
ax_minusSw.invert_xaxis() 

# make the +ve graphs 
ax_plusSw.barh(pos, nc_alpha, align='center', facecolor='#D8E2E1', 
edgecolor='None') 
ax_plusSw.barh(pos, SWT_alpha, align='center', facecolor='#6D7D72', 
height=0.5, edgecolor='None') 
ax_plusSw.set_yticks([])

# labels to be centered in the fig coord system and 
# centered w/ respect to the bars; use a custom transform 
import matplotlib.transforms as transforms 
transform = transforms.blended_transform_factory( 
    fig.transFigure, ax_plusSw.transData) 
for i, label in enumerate(Archie): 
    ax_plusSw.text(0.5, i+0.5, label, ha='center', va='center', 
transform=transform) 

# the axes titles are in axes coords, so x=0, y=1.025 is on the left 
# side of the axes, just above, x=1.0, y=1.025 is the right side of the 
# axes, just above 
if calc_case == 0:
    ax_minusSw.set_title('Normalized a', x=1.0, y=1.025, fontsize=12) 
elif calc_case == 1:
    ax_minusSw.set_title('Normalized Cementation exponent, m', x=1.0, y=1.025, fontsize=12)
elif calc_case == 2:
    ax_minusSw.set_title('Normalized Saturation exponent, n', x=1.0, y=1.025, fontsize=12)
elif calc_case == 3:
    ax_minusSw.set_title('Normalized Porosity, PHIT', x=1.0, y=1.025, fontsize=12)
elif calc_case == 4:
    ax_minusSw.set_title('Normalized Water Resistivity, RW', x=1.0, y=1.025, fontsize=12)

if calc_case_alpha == 0:
    ax_plusSw.set_title('Normalized a', x=0.0, y=1.025, fontsize=12)
elif calc_case_alpha == 1:
    ax_plusSw.set_title('Normalized Cementation exponent, m', x=0.0, y=1.025, fontsize=12)
elif calc_case_alpha == 2:
    ax_plusSw.set_title('Normalized Saturation exponent, n', x=0.0, y=1.025, fontsize=12)
elif calc_case_alpha == 3:
    ax_plusSw.set_title('Normalized Porosity, PHIT', x=0.0, y=1.025, fontsize=12)
elif calc_case_alpha == 4:
    ax_plusSw.set_title('Normalized Water Resistivity, RW', x=0.0, y=1.025, fontsize=12)

# the fig suptile is in fig coords, so 0.98 is the far right; we right align the text 
fig.suptitle('Uniform Dist [0.5, 2.5] applied to obtain multiplier for Archie variables; '
             'these are then normalized [0,1] for plotting purposes\n'
             'Base Case - SWT~0.29 (a=1, m=n=2, RT=2 ohmm, RW=0.01 ohmm  at 175 Deg C, PHIT=0.25)', ha='center', fontsize = 12
             )
#fig.suptitle('Base Case', y=0.18, ha='center', fontsize = 10)

# now add the annotations 
ax_plusSw.annotate('Normalized', xy=(0.95*nc_alpha[-1], num_Archie-0.5), 
                xycoords='data', 
                xytext=(20, 0), textcoords='offset points', 
                size=10, 
                va='center', 
                arrowprops=dict(arrowstyle="->"), 
                ) 

# a curved arrow for the annotation 
ax_plusSw.annotate('SWT', xy=(0.95*SWT_alpha[-1], num_Archie-0.5), 
                xycoords='data', 
                xytext=(40, -20), textcoords='offset points', 
                size=10, 
                va='center', 
                arrowprops=dict(arrowstyle="->", 

connectionstyle="angle,angleA=0,angleB=90,rad=3"), 

                ) 

plt.show() 
