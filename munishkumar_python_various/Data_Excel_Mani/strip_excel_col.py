# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:27:10 2019

@author: Munish

https://morphocode.com/pandas-cheat-sheet/

"""
import numpy as np
import pandas as pd

####---------------------Functions---------------------------------####
def rename_col(df_excel):
    conditions1 = [
            (df_excel['ATTRACTIVENESS'] == 'D not high graded (by Default)'),
            (df_excel['ATTRACTIVENESS'] == 'G High Graded POTEX'),
            (df_excel['ATTRACTIVENESS'] == 'E Temporary Excluded'),
            (df_excel['ATTRACTIVENESS'] == 'T Trash-definitely excluded'),
            ]
    choices1 = [
            'Low Graded or Not Fully Assessed "D"',
            'High Graded "G"',
            "E Temporary Excluded",
            "T Trash-definitely excluded"
            ]
    df_excel['ATTRACTIVENESS'] = np.select(conditions1, choices1, default = ' ')

    conditions2 = [
            (df_excel['MATURITY'] == 'A:Prospect requiring data Acquisition'),
            (df_excel['MATURITY'] == 'S:Prospect requiring GG Studies/interp'),
            (df_excel['MATURITY'] == 'R:Prospect Ready to drill'),
            (df_excel['MATURITY'] == 'H:History'),
            (df_excel['MATURITY'] == 'X:Temporary computation/Test'),
            (df_excel['MATURITY'] == 'D:Drilled'),
            (df_excel['MATURITY'] == 'L:Lead'),
            (df_excel['MATURITY'] == 'N:Notional (concept)'),
            ]
    choices2 = [
            '(A)dditional Key Data Needed',
            '(S)tudies Needed',
            'Technically (R)eady to Engineer',
            'H:History',
            'X:Temporary computation/Test',
            'D:Drilled',
            'L:Lead',
            'N:Notional (concept)'
            ]
    df_excel['MATURITY'] = np.select(conditions2, choices2, default = ' ')
    return df_excel

def userinput1(df_excel):
    ## Technical POTEX Inputs
    #Write out to single file with multiple filter
    df1 = df_excel[(df_excel['Region'] == 'APC') & (df_excel['Prospect_Valid'] == 'Yes')]

    conditions = [
            (df1['PA_UMR_MARKETABLE'] < 100),
            (df1['PA_UMR_MARKETABLE'] >= 100) & (df1['PA_UMR_MARKETABLE'] <= 500),
            (df1['PA_UMR_MARKETABLE'] > 500),
            ]
    choices = [
            '<100 Mboe UMR',
            'Large (100-500 Mboe)',
            'Giant (>500 Mboe)',
            ]
    df1['SIZE_CATEGORY'] = np.select(conditions, choices, default = ' ')

    #Rearrange and write out columns
    #df[['PROSPECT_NAME']].to_excel('Technical_POTEX.xlsx')
    df1[['PROSPECT_NAME', 'COUNTRY', 'PROSPECT_ID', 'EXPLO_TYPE',
         'ATTRACTIVENESS', 'MATURITY', 'PA_PG', 'PA_UMR',
         'PA_UMR_MARKETABLE', 'PA_Potex', 'EVALUATION_TYPE',
         'SA_Potex', 'Lithology_Simplified', 'Fluids',
         'Trap_Type_Simplified', 'Drilling_Environment',
         'COEFF_SEC', 'WI', 'SA_DEPOS_ENVIRONMENT',
         'PROSPECT_IMPACT', 'SEISMIC_COVER', 'DHI',
         'SIZE_CATEGORY', 'SA_ID', 'SA_NAME','PG_Grouped',
         'PA_MARKETABLE_P10', 'PA_MARKETABLE_P50', 'PA_MARKETABLE_P90',
         'LICENSE', 'PROSPECT_IMPACT', 'OPERATOR']].to_excel('Technical_POTEX.xlsx')

    print ("File Technical Potex Produced")
    return

def userinput2(df_excel):
    ## Temp Excluded Inputs
    #Write out to single file with multiple filter
    df2 = df_excel[
            (df_excel['Region'] == 'APC')
            & (df_excel['Prospect_Valid'] == 'No')
            & (df_excel['PA_VERSION'] == 'A')
            & (df_excel['SA_VERSION'] == 'A')
            & (df_excel['ATTRACTIVENESS'].str.contains('Temporary'))
                   ]

    #Rearrange and write out columns
    df2[['PROSPECT_NAME', 'COUNTRY', 'ATTRACTIVENESS',
         'MATURITY', 'PA_RISKED_MEAN',
         'Drilling_Environment', 'SEGMENT_NAME', 'EXPLO_THEME',
         'LICENSE', 'PA_PG', 'TRAP_TYPE',
         'LITHOLOGY', 'SA_DEPOS_ENVIRONMENT',
         'EXPLO_TYPE', 'PA_MODIFIED_DATE', 'PROSPECT_ID',
         'SEGMENT_ID']].to_excel('Temporary_Excluded.xlsx')

    print ("File Temporary Excluded Produced")
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
        run_code = int(input("Choose option - (1)Extract Technical POTEX, (2)Extract Temp Excluded or (3)Do both: "))
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
        #we're ready to exit the loop.
        break

print ("Reading File")

#k = 'W:/Group/EXPLO/APC/$CONSOLIDATION/APC_02_Potex/0 2019 PORTFOLIO/2 PATRIMONIAL GEOX/@POTEX_Licenses_Leads_Concepts_Extraction.xlsx'
k= 'C:/Users/J0501553/AnacondaProjects/January_2020.xlsm'

df_excel = pd.read_excel(k,
    sheet_name='Data',
    skiprows=[1] # header data
)

if run_code == 1:
    rename_col(df_excel)
    userinput1(df_excel)
elif run_code == 2:
    rename_col(df_excel)
    userinput2(df_excel)
else:
    rename_col(df_excel)
    userinput1(df_excel)
    rename_col(df_excel)
    userinput2(df_excel)



























