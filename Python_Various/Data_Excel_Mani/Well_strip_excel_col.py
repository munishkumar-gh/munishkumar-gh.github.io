# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:27:10 2019

@author: Munish

https://morphocode.com/pandas-cheat-sheet/
This code takes exisiting well production data from 2 datasources, IHS and Woodmac
It aims to strip and extract features of interest, apply filtering and collation
As much as possible, the 2 data sets are being normalized for comparability

For use with Power BI

"""
import numpy as np
import pandas as pd
import glob

####---------------------Functions---------------------------------####
def readinputfile(a, ch):
    print ("File Read In: ", a)
    if ch == 1:
        df_excel = pd.read_excel('C:/Users/J0501553/AnacondaProjects/@Well_summary_WMAC.xlsx',
                                 sheet_name = a,
                                 skiprows = 0 # header data
                                 )
    else:
        df_excel = pd.read_excel('C:/Users/J0501553/AnacondaProjects/@Well_summary_IHS.xlsx',
                                 sheet_name = a,
                                 skiprows = 0 # header data
                                 )
    return df_excel

def userinput(df_excel, out, ch):
    #Input Data from WoodMac is ch = 1

    if ch == 1:
        conditions = [
                (df_excel['Sidetrack'].notna()) & (df_excel['Re-entry'].notna()) & (df_excel['Tested'].notna()),
                (df_excel['Sidetrack'].notna()) & (df_excel['Re-entry'].notna()),
                (df_excel['Sidetrack'].notna()) & (df_excel['Tested'].notna()),
                (df_excel['Sidetrack'].notna()),
                (df_excel['Re-entry'].notna()) & (df_excel['Tested'].notna()),
                (df_excel['Re-entry'].notna()),
                (df_excel['Tested'].notna()),
                ]
        choices = [
                df_excel['Sidetrack'] + ', ' + df_excel['Re-entry'] + ', ' + df_excel['Tested'],
                df_excel['Sidetrack'] + ', ' + df_excel['Re-entry'],
                df_excel['Sidetrack'] + ', ' + df_excel['Tested'],
                df_excel['Sidetrack'],
                df_excel['Re-entry'] + ', ' + df_excel['Tested'],
                df_excel['Re-entry'],
                df_excel['Tested'],
                ]
        df_excel['Operations'] = np.select(conditions, choices, default = ' ')

        conditions2 = [
                (df_excel['Oil-gas-dry'].notna()) & (df_excel['Discovery type'].notna()),
                (df_excel['Oil-gas-dry'].notna()) & (df_excel['Discovery type'] == ' '),
                (df_excel['Oil-gas-dry'] == ' ') & (df_excel['Discovery type'].notna()),
                ]
        choices2 = [
                df_excel['Oil-gas-dry'] + ', ' + df_excel['Discovery type'],
                df_excel['Oil-gas-dry'],
                'HC Type unknown' + ', ' + df_excel['Discovery type'],
                ]
        df_excel['HC_type'] = np.select(conditions2, choices2, default = ' ')

        conditions3 = [
                (df_excel['Shore status'] == 'Onshore'),
                (df_excel['Shore status'] == 'Shelf'),
                (df_excel['Shore status'] == 'Deepwater'),
                (df_excel['Shore status'] == 'Ultra-deepwater'),
                ]
        choices3 = ['Onshore', 'Offshore', 'Deep Offshore', 'Ultra Deep Offshore']
        df_excel['WD'] = np.select(conditions3, choices3, default = ' ')

        #Write out to single file with multiple filter
        df_excel = df_excel[(df_excel['Company'] == 'Elf Aquitaine') | (df_excel['Company'] == 'Total')]
        df_excel['Equity (%)'] = (df_excel['Company equity in subsidiary (%)']/100 * df_excel['Subsidiary equity in asset (%)']/100) * 100

       #Rearrange and write out columns
        #df[['PROSPECT_NAME']].to_excel('Technical_POTEX.xlsx')
        df_excel[['Well (local name)', 'Country', 'Company', 'Operator-partner',
                  'Basin', 'Sector', 'Operator', 'Block name',
                  'Well type', 'Result',  'Status', 'Spud date',
                  'Completion date', 'Net drill days (days)', 'Rig type', 'Net WI discovered reserves (mmboe)',
                  'Net well cost (nominal terms) (US$M)', 'Latitude DMS','Longitude DMS', 'Primary period',
                  'Primary formation', 'Partners', 'Well comment', 'Operations',
                  'HC_type', 'WD', 'Equity (%)',
                  ]].to_excel(out)
    else:
#  ~(df_excel['ONS_OFFSHO'] == 'Onshore') means all elements in dataframe that are NOT 'Onshore'
        conditions1 = [
                (df_excel['ONS_OFFSHO'] == 'Onshore'),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_calc'] >= 0) & (df_excel['WD_calc'] < 500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_calc'] >= 500) & (df_excel['WD_calc'] < 1500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_calc'] >= 1500) & (df_excel['WD_calc'] < 3000),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_calc'] >= 3000),
                ]
        choices1 = ['Onshore', 'Offshore', 'Deep Offshore', 'Ultra Deep Offshore', 'Frontier Deep Offshore']
        df_excel['WD'] = np.select(conditions1, choices1, default = ' ')

        conditions2 = [
                (df_excel['General Class'] == 'Exploratory'),
                (df_excel['General Class'] == 'Development/Service'),
                (df_excel['General Class'] == 'Injector'),
                (df_excel['General Class'] == 'Non-hydrocarbon') & (df_excel['Well Class'] == 'Stratigraphic test'),
                (df_excel['General Class'] == 'Non-hydrocarbon') & (df_excel['Well Class'] == 'Relief'),
                ]
        choices2 = ['Exploration', 'Development', 'Production', 'Non-HC - Stratigraphic Test', 'Non-HC - Relief']
        df_excel['Well Type'] = np.select(conditions2, choices2, default = ' ')

        conditions3 = [(df_excel['Operator Flag'] == 'Y')]
        choices3 = ['Operator']
        df_excel['Operator-partner'] = np.select(conditions3, choices3, default = 'Partner')

        df_excel[['Country Name', 'Contract Name', 'Basin Name',
                  'Well Name', 'General Resource Type', 'Content', 'Disc Flag',
                  'Spud Date', 'Rig Days',  'Company Acronym', 'Company Type',
                  'Interests Pct', 'Operator-partner', 'WD', 'Well Type']].to_excel(out)
    print ("File Extract Produced: ", out)
    return

def splitstack(a, out):
    df_excel = pd.read_excel('C:/Users/J0501553/AnacondaProjects/Summarized_WL_WMAC.xlsx',
                             sheet_name = a,
                             skiprows = 0 # header data
                             )

    #Use example from Stack overflow - https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe
    (# Set the columns that are not to be touched as the index
     df_excel.set_index(['Well (local name)', 'Country', 'Company', 'Operator-partner',
                  'Basin', 'Sector', 'Operator', 'Block name',
                  'Well type', 'Result',  'Status', 'Spud date',
                  'Completion date', 'Net drill days (days)', 'Rig type', 'Net WI discovered reserves (mmboe)',
                  'Net well cost (nominal terms) (US$M)', 'Latitude DMS','Longitude DMS', 'Primary period',
                  'Primary formation', 'Well comment', 'Operations',
                  'HC_type', 'WD', 'Equity (%)'])
    .stack()                        # Stack the rows
    .str.split(',', expand=True)    # This is now a series - call str.split on comma
    .stack()                        # Get rid of NULL values by calling stack again
    .unstack(-2)                    # Second last level of the index to become columns, so unstack using unstack(-2) (unstack on the second last level)
    .reset_index(-1, drop=True)     # Get rid of the superfluous last level using reset_index
    .reset_index()
    .to_excel(out)
    )

#    (
#     df_excel.set_index(['Well (local name)', 'Country', 'Company', 'Operator-partner',
#                  'Basin', 'Sector', 'Operator', 'Block name',
#                  'Well type', 'Result',  'Status', 'Spud date',
#                  'Completion date', 'Net drill days (days)', 'Rig type', 'Net WI discovered reserves (mmboe)',
#                  'Net well cost (nominal terms) (US$M)', 'Latitude DMS','Longitude DMS', 'Primary period',
#                  'Primary formation', 'Well comment', 'Operations',
#                  'HC_type', 'WD', 'Equity (%)'])
#    .stack()
#    .str.split('(', expand=True)
#    .stack()
#    .unstack(-2)
#    .reset_index(-1, drop=True)
#    .reset_index()
#    .to_excel(out)
#    )

    print ("File Extract Produced: ", out)
    return


####---------------------Main-----------------------------------####

#filter single value
#df_excel[df_excel['quantity'] == 14]
#filter multiple value
#df_excel[(df_excel['name'] == 'Barton LLC') | (df_excel['quantity'] == '14')]
#Write out to single file a single filter
#df_excel[df_excel['quantity'] == 14].to_excel('testdoco.xlsx')
#For trouble shooting - print last 5 rows
#df_excel.tail(5)
#print(df_excel)

while True:
    try:
        run_code = int(input("Choose option - (1)Extract Well Data from Wood-Mac, (2) Extract Well Data from IHS or (3)Exit: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    if run_code < 0:
        print("Sorry, your response must not be negative.")
        continue
    elif run_code >3:
        print("Incorrect Input Value - Choose only 1, 2 or 3")
        continue
    else:
        #value was successfully parsed, and we're happy with its value.
        if run_code == 1:
            df_excel = readinputfile('Well_summary_WMAC', 1)
            userinput(df_excel, 'Summarized_WL_WMAC.xlsx', 1)
            splitstack('Sheet1', 'Summarized_WL_WMAC.xlsx')

        elif run_code == 2:
            df_excel = readinputfile('Well_summary_IHS', 2)
            userinput(df_excel, 'Summarized_WL_IHS.xlsx', 2)
        else:
        #we're ready to exit the loop.
        #combine_multiple('CONTRACT_N', 'BLOCK_SQKM')
            break










































