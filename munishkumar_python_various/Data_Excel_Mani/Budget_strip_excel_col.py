# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:08:38 2019

@author: Munish Kumar

Code is built in to pre-process
output from console master
It modifies lices names to be consistent
and also check water depth
Strips out superfluous data, and fills in
gaps where necessary


"""

import time
import numpy as np
import pandas as pd
import os
import glob

start = time.time()

####---------------------Functions---------------------------------####
def readinputfile(pt, a):
    print ("File Read In: ", a)
    df_excel = pd.read_excel(pt,
                             sep='\s*,\s*',
                             sheet_name = a,
                             skiprows = 0 # header data
                             )
    print("Completed Reading input file: ", pt)
    return df_excel

def userinput(run_code, df_excel, out):
#  ~(df_excel['XXX'] == 'YYY') means all elements in dataframe that are NOT 'YYY'

    conditions = [
            (df_excel['License'] == 'WA-285-P (R2)') & (df_excel['License'].notna()),
            (df_excel['License'] == 'WA-343-P') & (df_excel['License'].notna()),
            (df_excel['License'] == 'BLOC B') & (df_excel['License'].notna()),
            (df_excel['License'] == 'BLOC CA1') & (df_excel['License'].notna()),
            (df_excel['License'] == 'TAIYANG') & (df_excel['License'].notna()),
            (df_excel['License'] == 'SEBUKU') & (df_excel['License'].notna()),
            (df_excel['License'] == 'JS-5, JS-6') & (df_excel['License'].notna()),
            (df_excel['License'] == 'A6') & (df_excel['License'].notna()),
            (df_excel['License'] == 'M5-M6') & (df_excel['License'].notna()),
            (df_excel['License'] == 'MD-2') & (df_excel['License'].notna()),
            (df_excel['License'] == 'MD-4') & (df_excel['License'].notna()),
            (df_excel['License'] == 'MD-7') & (df_excel['License'].notna()),
            (df_excel['License'] == 'YWB') & (df_excel['License'].notna()),
            (df_excel['License'] == 'DW-2E') & (df_excel['License'].notna()),
            (df_excel['License'] == 'Block N') & (df_excel['License'].notna()),
            (df_excel['License'] == 'PPL 339') & (df_excel['License'].notna()),
            (df_excel['License'] == 'PPL 576') & (df_excel['License'].notna()),
            (df_excel['License'] == 'PPL 589') & (df_excel['License'].notna()),
            (df_excel['License'] == 'PRL 15') & (df_excel['License'].notna())
            ]
    choices = ['WA-285-P (R2)', 'WA-343-P', 'BLOC B - 1989 PMA', 'BLOCK CA1',
               'TAIYANG', 'SEBUKU', 'JS-5/6', 'A6',
               'M5-M6', 'MD-02', 'MD-04', 'MD-07',
               'YWB', 'DW 2E', 'BLOCK N_OFFSHORE SABAH', 'PPL 339',
               'PPL 576', 'PPL 589', 'PRL 15'
               ]
    df_excel['FIL_LIC'] = np.select(conditions, choices, default = ' ')

    conditions = [
            (df_excel['FIL_LIC'] == 'WA-343-P') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'WA-285-P (R2)') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'BLOC B - 1989 PMA') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'BLOCK CA1') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'TAIYANG') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'SEBUKU') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'JS-5/6') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'A6') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'M5-M6') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'MD-02') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'MD-04') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'MD-07') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'YWB') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'DW 2E') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'BLOCK N_OFFSHORE SABAH') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'PPL 339') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'PPL 576') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'PPL 589') & (df_excel['FIL_LIC'].notna()),
            (df_excel['FIL_LIC'] == 'PRL 15') & (df_excel['FIL_LIC'].notna()),
            ]
    choices = ['Offshore', 'Offshore', 'Offshore', 'Deep Offshore',
               'Ultra Deep Offshore', 'Offshore', 'Ultra Deep Offshore', 'Ultra Deep Offshore',
               'Offshore', 'Ultra Deep Offshore', 'Ultra Deep Offshore', 'Ultra Deep Offshore',
               'Ultra Deep Offshore', 'Deep Offshore', 'Ultra Deep Offshore', 'Onshore',
               'Ultra Deep Offshore', 'Ultra Deep Offshore', 'Onshore'
               ]
    choices2 = ['Emerging', 'Mature', 'Mature', 'Emerging',
                'Frontier', 'Emerging', 'Frontier', 'Emerging',
                'Emerging', 'Emerging', 'Frontier', 'Frontier',
                'Frontier', 'Mature', 'Emerging', 'Emerging',
                'Frontier', 'Frontier', 'Mature'
                ]
    df_excel['Environ'] = np.select(conditions, choices, default = ' ')
    df_excel['Explo_Code'] = np.select(conditions, choices2, default = ' ')

#    conditions = [
#            (df_excel['Explo Type Code'] == 'EXT') & (df_excel['Explo Type Code'].notna()),
#            (df_excel['Explo Type Code'] == 'FRONT') & (df_excel['Explo Type Code'].notna()),
#            (df_excel['Explo Type Code'] == 'INT') & (df_excel['Explo Type Code'].notna()),
#            ]
#    choices = ['Emerging', 'Frontier', 'Mature']
#    df_excel['Explo_Code'] = np.select(conditions, choices, default = ' ')

    #Rearrange and write out columns
    #df[['PROSPECT_NAME']].to_excel('Technical_POTEX.xlsx')
    if run_code ==1:

        df2 = df_excel[(df_excel['Type EA'] == 'Explo') &
                       (df_excel['Unconventional'] == 'No') &
                       (df_excel['Country Code'] != 'APC') &
                       (df_excel['Asset Name'] != 'New Ventures') &
                       ~(df_excel['Asset Name'].str.contains('NV')) &
                       (df_excel['Asset Name'] != 'AC-P60') &
                       (df_excel['Asset Name'] != 'Gladstone_LNG') &
                       ~(df_excel['Asset Name'].str.contains('SC')) &
                       ~(df_excel['Asset Name'].str.contains('Bongkot')) &
                       (df_excel['License'] != 'WA-56R') &
                       (df_excel['FIL_LIC'] != ' ') &
                       (df_excel['Environ'] != ' ')
                       ]

        df2[
                [
                'Country Code',
                'Affiliate Code',
                'Data Category',
                'Data Type',
                'FIL_LIC',
                'Environ',
                'Explo_Code',
                'Project Name',
                'Share Of Costs IB',
                'Share Of Costs CF',
                'Share Of Costs 2020 ',
                'PI IB',
                'PI CF',
                'PI 2020',
                'Costs 100% IB',
                'Costs 100% CF',
                'Costs 100% 2020',
                'Firm/cont Plan',
                'Operating Code',
                'Obligation Code',
                'Id Project',
                'Code Nature',
                'Comments'
                  ]
        ].to_excel(out)

#df_excel[(df_excel['name'] == 'Barton LLC') | (df_excel['quantity'] == '14')]

    print ("File Extract Produced: ", out)
    return

def pass_file_path(myFiles):
    pathlen = os.getcwd()
    for filename in myFiles:
        fName = os.path.join(pathlen, filename)
    print (fName)
    return fName, pathlen

####---------------------Main-----------------------------------####
while True:
    try:
        run_code = int(input("Choose option - (1) Load Consolmaster file or (2) Exit: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    if run_code < 0:
        print("Sorry, your response must not be negative.")
        continue
    elif run_code >2:
        print("Incorrect Input Value - Choose only 1 or 2")
        continue
    else:
        #value was successfully parsed, and we're happy with its value.
        if run_code == 1:
            pt = ['Consolmaster.xlsx'] ##Editable
            var1 = 'Budget' ##Editable
            out1 = 'Budget.xlsx'

        #fn to read path, load file defined as 'pt'
            fName, pathlen = pass_file_path(pt)
            df_excel = readinputfile(fName, var1)
            userinput(run_code, df_excel, out1)
        else:
            #we're ready to exit the loop.
            break
    count = 'Completed Process'
    elapsed = (time.time() - start)
    print ("%s in %s seconds" % (count,elapsed))
    break