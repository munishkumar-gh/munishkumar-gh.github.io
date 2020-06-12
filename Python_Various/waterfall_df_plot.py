# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:55:45 2020

@author: Munish Kumar

A function that attempts to generate a standard waterfall chart in generic Python. Requires two sequences,
one of labels and one of values, ordered accordingly.


"""
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import seaborn as sns
import os
#import glob

# Functions for the waterfall plot
#------------------------------------------
def pass_file_path(myFiles):
    pathlen = os.getcwd()
    for filename in myFiles:
        fName = os.path.join(pathlen, filename)
    print (fName)
    return fName, pathlen

def readinputfile(pt, a):
    print ("File Read In: ", a)
    df_excel = pd.read_excel(pt,
                             sep='\s*,\s*',
                             sheet_name = a,
                             skiprows = 0 # header data
                             )
    print("Completed Reading input file: ", pt)
    return df_excel



def plot(index, data, Title=" ", x_lab="", y_lab="",
              formatting = "{:,.1f}", green_color='#29EA38', red_color='#FB3C62', blue_color='#24CAFF',
             sorted_value = False, threshold=None, other_label='other', net_label='net',
             rotation_value = 30, font = 12):
    '''
    Given two sequences ordered appropriately, generate a standard waterfall chart.
    Optionally modify the title, axis labels, number formatting, bar colors,
    increment sorting, and thresholding. Thresholding groups lower magnitude changes
    into a combined group to display as a single entity on the chart.
    '''

    #convert data and index to np.array
    index=np.array(index)
    data=np.array(data)

    #sorted by absolute value
    if sorted_value:
        abs_data = abs(data)
        data_order = np.argsort(abs_data)[::-1]
        data = data[data_order]
        index = index[data_order]

    #group contributors less than the threshold into 'other'
    if threshold:

        abs_data = abs(data)
        threshold_v = abs_data.max()*threshold

        if threshold_v > abs_data.min():
            index = np.append(index[abs_data>=threshold_v],other_label)
            data = np.append(data[abs_data>=threshold_v],sum(data[abs_data<threshold_v]))

    changes = {'amount' : data}

    #define format formatter
    def money(x, pos):
        'The two args are the value and tick position'
        return formatting.format(x)
    formatter = FuncFormatter(money)

    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)

    #Store data and create a blank series to use for the waterfall
    trans = pd.DataFrame(data=changes,index=index)
    blank = trans.amount.cumsum().shift(1).fillna(0)

    trans['positive'] = trans['amount'] > 0

    #Get the net total number for the final element in the waterfall
    total = trans.sum().amount
    trans.loc[net_label]= total
    blank.loc[net_label] = total

    #The steps graphically show the levels as well as used for label placement
    step = blank.reset_index(drop=True).repeat(3).shift(-1)
    step[1::3] = np.nan

    #When plotting the last element, we want to show the full bar,
    #Set the blank to 0
    blank.loc[net_label] = 0

    #define bar colors for net bar
    trans.loc[trans['positive'] > 1, 'positive'] = 99
    trans.loc[trans['positive'] < 0, 'positive'] = 99
    trans.loc[(trans['positive'] > 0) & (trans['positive'] < 1), 'positive'] = 99

    trans['color'] = trans['positive']

    trans.loc[trans['positive'] == 1, 'color'] = green_color
    trans.loc[trans['positive'] == 0, 'color'] = red_color
    trans.loc[trans['positive'] == 99, 'color'] = blue_color

    my_colors = list(trans.color)

    # connecting lines - figure out later
    #my_plot = lines.Line2D(step.index, step.values, color = "gray")
    #my_plot = lines.Line2D((3,3), (4,4))

    #Plot and label
    my_plot = plt.bar(range(0,len(trans.index)), blank, width=0.5, color='white')
    plt.bar(range(0,len(trans.index)), trans.amount, width=0.6,
             bottom=blank, color=my_colors, edgecolor='black')

    #axis labels
    plt.xlabel("\n" + x_lab)
    plt.ylabel(y_lab + "\n")

    #Get the y-axis position for the labels
    y_height = trans.amount.cumsum().shift(1).fillna(0)

    temp = list(trans.amount)

    # create dynamic chart range
    for i in range(len(temp)):
        if (i > 0) & (i < (len(temp) - 1)):
            temp[i] = temp[i] + temp[i-1]

    trans['temp'] = temp

    plot_max = trans['temp'].max()
    plot_min = trans['temp'].min()

    #Make sure the plot doesn't accidentally focus only on the changes in the data
    if all(i >= 0 for i in temp):
        plot_min = 0
    if all(i < 0 for i in temp):
        plot_max = 0

    if abs(plot_max) >= abs(plot_min):
        maxmax = abs(plot_max)
    else:
        maxmax = abs(plot_min)

    pos_offset = maxmax / 40

    plot_offset = maxmax / 15 ## needs to be cumulative sum dynamic

    #Start label loop
    loop = 0
    for index, row in trans.iterrows():
        # For the last item in the list, we don't want to double count
        if row['amount'] == total:
            y = y_height[loop]
        else:
            y = y_height[loop] + row['amount']
        # Determine if we want a neg or pos offset
        if row['amount'] > 0:
            y += (pos_offset*2)
            plt.annotate(formatting.format(row['amount']),(loop,y),ha="center", color = 'darkblue', fontsize=font)
        else:
            y -= (pos_offset*4)
            plt.annotate(formatting.format(row['amount']),(loop,y),ha="center", color = 'orange', fontsize=font)
        loop+=1

    #Scale up the y axis so there is room for the labels
    plt.ylim(plot_min-round(3.6*plot_offset, 7),plot_max+round(3.6*plot_offset, 7))

    #Rotate the labels
    plt.xticks(range(0,len(trans)), trans.index, rotation=rotation_value, wrap=True)

    #add zero line and title
    plt.axhline(0, color='black', linewidth = 0.6, linestyle="dashed")
    plt.title(Title)
    plt.tight_layout()

    return plt

def create_image(a, b, input1):
    my_plot= plot(a, b, rotation_value = 0,formatting = "{:,.0f}", net_label="Final\n", other_label="MISC",
                Title="POTEX Erosion & Reload", x_lab = " ", y_lab = "Technical POTEX (Mboe)",
                blue_color = "lightblue", green_color = "darkgreen", red_color = 'darkorange', font = 12)

    # Utilize seaborn for visualization
    sns.set()
    sns.set_style('ticks')
    sns.despine()
    sns.set_context("talk", font_scale=0.5, rc={"lines.linewidth": 2.5})
    #sns.set(font_scale=0.5)
    #plt.subplots(figsize=(25, 8))
    plt.ylim(0,None)

    #------------------------------------------
    #Annotation for aach part of the graph

    x1 = 1.
    y1 = (POTEX_TOTAL+FD)/3.
    x2 = 2.
    y2 = (y1*3+DF_2020)/3.
    x3 = 3.
    y3 = (y2*3+DF_2021)/3.
    x4 = 4.
    y4 = (y3*3+DF_2022)/3.
    x5 = 5.
    y5 = (y4*3+DF_2023)/3.
    x6 = 6.
    y6 = (y5*3+Relinquish)/3.
    x7 = 7.
    y7 = (y6*3+NV)/3.
    x8 = 8.
    y8_f = (y7*3+Failure)/3.
    y8_s = (y7*3+Success)/3.

    shift = 80
    fct = 2.15
    fontsize = 5.5

    plt.text(x1, y1, 'PPL576 (50%)\nPPL589 (50%)\nTaiyang (26%)',
            {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
            'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
             )
#    plt.annotate(" ", xy = (x1, y1+shift), xytext=(x1, y1*fct+shift),
#            textcoords='data', ha="center", va='bottom',color='blue',
#            arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#                 )

    plt.text(x2, y2, 'Mailu\nShwe Nadi',
            {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
            'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
             )
#    plt.annotate("", xy = (x2, y2+shift), xytext=(x2, y2*fct+shift),
#            textcoords='data', ha="center", va='bottom',color='blue',
#            arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#                 )

    plt.text(x3, y3, 'Tepat NW\nYaqut',
            {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
            'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
             )
#    plt.annotate("", xy = (x3, y3+shift), xytext=(x3, y3*fct+shift),
#            textcoords='data', ha="center", va='bottom',color='blue',
#            arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#                 )

    plt.text(x5, y5, 'Antelope\nSouth',
            {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
            'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
             )
#    plt.annotate("", xy = (x5, y5+shift), xytext=(x5, y5*fct+shift),
#            textcoords='data', ha="center", va='bottom',color='blue',
#            arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#                 )

    plt.text(x6, y6, 'DW2E\nMD2\nCA1\nWA-343',
            {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
            'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
             )
#    plt.annotate("", xy = (x6, y6+shift), xytext=(x6, y6*fct+shift),
#            textcoords='data', ha="center", va='bottom',color='blue',
#            arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#                 )

    plt.text(x7, y7, 'PRMB\nSB-2K\nPeri PRL-15',
            {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
            'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
             )
#    plt.annotate("", xy = (x7, y7+shift), xytext=(x7, y7*fct+shift),
#            textcoords='data', ha="center", va='bottom',color='blue',
#            arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#                 )

    plt.tight_layout()

    if (input1 == 1):
        plt.text(x8, y8_s, '(Pg uplift)\nPPL 576/\nPPL 589\n(Mailu)',
        {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
        'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
         )
#        plt.annotate("", xy = (x8, y8_s+shift), xytext=(x8, y8_s*fct+shift),
#        textcoords='data', ha="center", va='bottom',color='blue',
#        arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#             )
        plt.savefig('waterfall_success_plot.png', format='png', dpi=1200)
        plt.show()
    elif (input1 == 2):
        plt.text(x8, y8_f, 'Mailu 3 & 5\nTepat Deep',
        {'color': 'black', 'fontsize': fontsize, 'ha': 'center', 'va': 'center',
        'bbox': dict(boxstyle="round", fc="white", ec="black", pad=0.2)}
         )
#        plt.annotate("", xy = (x8, y8_f+shift), xytext=(x8, y8_f*fct+shift),
#        textcoords='data', ha="center", va='bottom',color='blue',
#        arrowprops=dict(arrowstyle='<|-|>', connectionstyle='arc3,rad=0', color='red')
#             )
        plt.savefig('waterfall_failure_plot.png', format='png', dpi=1200)
        plt.show()
    else:
        exit
    return

#------------------------------------------
# Editable input variables
#------------------------------------------

pt = ['Tech_POTEX.xlsx'] ##Editable
var1 = 'WellRank' ##Editable

FD_PPL576_589 = 0.5 ##Farm-down WI in PPL576 and PPL589

#Mailu in PPL576
Mailu_3 = 56 * FD_PPL576_589
Mailu_5 = 110 * FD_PPL576_589

Success_PPL576 = 382  * FD_PPL576_589
Success_PPL589 = 198 * FD_PPL576_589

Net_plus = 1
Net_minus = -1

#------------------------------------------
#fn to read path, load file defined as 'pt'
fName, pathlen = pass_file_path(pt)
df_excel = readinputfile(fName, var1)

# Current Total POTEX #
POTEX_TOTAL = df_excel.loc[(~df_excel['Name'].str.contains("XYZ")) & (~df_excel['Patrimonial/NV'].str.contains("NV")), 'Technical POTEX'].sum()
#print('POTEX_TOTAL: ', POTEX_TOTAL, 'Mboe')

# Farm-Down - Mailu 3 & Mailu 5 to 50%, Taiyang to 26%#
FD = (df_excel.loc[df_excel['Flag Success'] > -1, 'Technical POTEX'].sum() - df_excel.loc[df_excel['Flag Success'] > -1, 'Technical POTEX post FD'].sum())*Net_minus
#print('Farm Down: ', FD, 'Mboe')

# Firm Drilling 2020 - Mailu 3 [56 Mboe] & Mailu 5 [110 Mboe] are dependents #
DF_2020 = (df_excel.loc[df_excel['Flag Success'] == 1, 'Technical POTEX post FD'].sum() - Mailu_3 - Mailu_5)*Net_minus
#print('Firm Drilling [2020]: ', DF_2020, 'Mboe')

# Contingent Drilling 2020 #
DC_2020 = (df_excel.loc[df_excel['Flag Success'] == 2, 'Technical POTEX post FD'].sum())*Net_plus
#print('Contingent Drilling [2020]: ', DC_2020, 'Mboe')

# Firm Drilling 2021 #
DF_2021 = (df_excel.loc[df_excel['Flag Success'] == 3, 'Technical POTEX post FD'].sum())*Net_minus
#print('Firm Drilling [2021]: ', DF_2021, 'Mboe')

# Contingent Drilling 2021 - include now Mailu 3 and 5#
DC_2021 = (df_excel.loc[df_excel['Flag Success'] == 4, 'Technical POTEX post FD'].sum() - (- Mailu_3 - Mailu_5))*Net_plus
#print('Contingent Drilling [2021]: ', DC_2021, 'Mboe')

# Firm Drilling 2022 #
DF_2022 = (df_excel.loc[df_excel['Flag Success'] == 5, 'Technical POTEX post FD'].sum())*Net_minus
#print('Firm Drilling [2022]: ', DF_2022, 'Mboe')

# Contingent Drilling 2022 #
DC_2022 = (df_excel.loc[df_excel['Flag Success'] == 6, 'Technical POTEX post FD'].sum())*Net_plus
#print('Contingent Drilling [2022]: ', DC_2022, 'Mboe')

# Firm Drilling 2023 #
DF_2023 = (df_excel.loc[df_excel['Flag Success'] == 7, 'Technical POTEX post FD'].sum())*Net_minus
#print('Firm Drilling [2023]: ', DF_2023, 'Mboe')

# Contingent Drilling 2023#
DC_2023 = (df_excel.loc[df_excel['Flag Success'] == 8, 'Technical POTEX post FD'].sum())*Net_plus
#print('Contingent Drilling [2023]: ', DC_2023, 'Mboe')

# Relinquished #
Relinquish = (df_excel.loc[df_excel['Flag Success'] == 9, 'Technical POTEX post FD'].sum())*Net_minus
#print('Relinquishments/ Block Sales: ', Relinquish, 'Mboe')

# NV #
NV = (df_excel.loc[df_excel['Flag Success'] == 12, 'Technical POTEX post FD'].sum())*Net_plus
#print('New Ventures: ', NV, 'Mboe')

# Failure Case - Worst Case Scenario. All dependents & Contingent Wells are unchanged#
# Only Mailu 3, Mailu 5 & Tepat Deep are dropped #
Failure = ((df_excel.loc[df_excel['Flag Failure'] == 1, 'Technical POTEX post FD'].sum()) + Mailu_3 + Mailu_5)*Net_minus
#print('Failure: ', Failure, 'Mboe')

# The boost to the POTEX is given by the PNG team in the prospect maturation meetings17-Sept-2019 #
# PNG boost = 382 (PPL 576) + 198 (PPL 589)#
Success = ((df_excel.loc[df_excel['Flag Success'] == 10, 'Positive POTEX'].sum()) - (df_excel.loc[df_excel['Flag Success'] == 10, 'Technical POTEX post FD'].sum()) +Success_PPL576 +Success_PPL589)*Net_plus
#print('Success Case [x% Pg Uplift assumed, moving Pg towards 40-50% notional]: ', Success, 'Mboe')

a = [
    'Current\nPOTEX', 'Farm\nDown', '2020\nDrill\n(Firm)',
    '2021\nDrill\n(Firm)', '2022\nDrill\n(Firm)', '2023\nDrill\n(Firm)',
    'Relinquish', 'New\nVenture', 'Success'
    ]

#SO_Total_Open =  dataset['Total Opened (KSGD)'].sum(axis=0,skipna=True).round()
b = [
     POTEX_TOTAL, FD, DF_2020,
     DF_2021, DF_2022, DF_2023,
     Relinquish, NV, Success
     ]

c = [
    'Current\nPOTEX', 'Farm\nDown', '2020\nDrill\n(Firm)',
    '2021\nDrill\n(Firm)', '2022\nDrill\n(Firm)', '2023\nDrill\n(Firm)',
    'Relinquish', 'New\nVenture', 'Failure'
    ]

d = [
     POTEX_TOTAL, FD, DF_2020,
     DF_2021, DF_2022, DF_2023,
     Relinquish, NV, Failure
     ]

# Function
create_image(a, b, 1)
create_image(c, d, 2)
