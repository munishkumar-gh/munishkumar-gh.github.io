# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:25:16 2019

@author: Munish Kumar

Potex Erosion and Reload Waterfall Plot
Requires the calling of a waterfall_chart library in Python 3.7+

GLobal Variables are editable; the rest of the code can be modified
but requires a bit more advanced knowledge of python 
"""
# Global Variables - change values as needed
PNG_Mailu = 592
Farm_down_PNG = 0.5

MM_YWB = 40
Farm_down_MM = 0.6

China_Taiyang = 113/0.49
Farm_down_China = 0.3

########### Master Code - Modify ###########
############ if Necessary Only ###########
import matplotlib.pyplot as plt
import waterfall_chart
import seaborn as sns

OPNG = PNG_Mailu
FDPNG = Farm_down_PNG
c1 = -(OPNG*FDPNG)

OMM = MM_YWB
FDMM = Farm_down_MM
c2 = -(OMM*FDMM)

OCH = China_Taiyang
FDCH = Farm_down_China
c3 = -(OCH*FDCH)

#FD = c1 + c2 + c3
FD=-365

a= ['CURRENT POTEX', 'AFTER FARM OUTS  (2019)', '2019 DRILLING (FIRM)','2020 DRILLING (FIRM)',
    '2021 DRILLING (FIRM)', '2022 DRILLING (FIRM)','RELINQUISHMENT','SUCCESS DEP.POTEX']
b= [1454, FD, -141, -231, 0, 0, 0, 125.4]

# Function
my_plot=waterfall_chart.plot(a,b, rotation_value=-90,formatting = "{:,.1f}", net_label="REMAINING POTEX", other_label="MISC",
            Title="Potex Erosion and Reload", x_lab = " ", y_lab = "Risked Resources PG SEC (Mboe)", 
            blue_color = "lightblue", green_color = "darkgreen", red_color = 'darkorange', font = 10)

# Utilize seaborn for visualization
sns.set()
sns.set_style('ticks')
sns.despine()
sns.set_context("notebook", font_scale=0.8, rc={"lines.linewidth": 2.5})
plt.ylim(0,None)
plt.show()