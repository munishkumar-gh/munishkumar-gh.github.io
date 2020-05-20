# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:10:29 2019

@author: Munish

https://morphocode.com/pandas-cheat-sheet/

A variation of the Acerage_strip_excel_col.py script

This script focuses on country specfic areas and does
a competitor extraction of relevant data for use
in visualization

"""
import time
import numpy as np
import pandas as pd
import os
import glob

start = time.time()

####---------------------Functions---------------------------------####
def readinputfile(pt, a):
    df_excel = pd.read_excel(pt,
                             sheet_name = a,
                             skiprows = 0, # header data
                             sep='\s*,\s*',
                             )
    df_excel.columns = map(str.upper, df_excel.columns) #all column headers set to upper case
    print("Completed Reading input file: ", pt)
    return df_excel

def userinput(run_code, df_excel, out):
    #Write out to single file with multiple filter
    #df1 = df_excel[(df_excel['RESOURCE_T'] == 'Unconventional') | (df_excel['RESOURCE_T'] == 'Conven & Unconven')]:

    #Change cols to lower case for use with dict
    df_excel.columns = map(str.lower, df_excel.columns)
    #df1 = df_excel[(df_excel['RESOURCE_T'] == 'Unconventional') | (df_excel['RESOURCE_T'] == 'Conven & Unconven')]:

    # Remap all the column names to dict based names to generalize the code.
    # Done as the input excel files often have different names.
    # All dict names case sensitive
    d = {'^applicat.*'          : 'APPLICAT_1',
         '^area_3d.*'           : 'BLOCK_3D_SQKM',
         '^area_2d.*'           : 'BLOCK_2D_SQKM',
         '^award_da.*'          : 'AWARD_DA_1',
         '^basin_na.*'          : 'BASIN_NAME',
         '^block_n.*'           : 'BLOCK_N',
         '^block_sqkm.*'        : 'BLOCK_SQKM',
         '^block_stat.*'        : 'BLOCK_STAT',
         '^block_val.*'         : 'BLK_VLD_FLG',
         '^company_ac.*'        : 'CO_ACR',
         '^company_ty.*'        : 'CO_TYPE',
         '^contract_n.*'        : 'CONTRACT_N',
         '^contract_val.*'      : 'CNTRCT_VLD_FLG',
         '^country_na.*'        : 'COUNTRY_NA',
         '^datum_name.*'        : 'DATUM_NAME',
         '^deep_water.*'        : 'DEEP_WATER',
         '^end_date_t.*'        : 'END_DATE_T',
         '^exp_expi.*'          : 'EXP_EXPI_1',
         '^expiry_d.*'          : 'EXPIRY_D_1',
         '^expiry_sch.*'        : 'EXPIRY_SCH',
         '^farm_out.*'          : 'FO_FLG',
         '^general_co.*'        : 'GENERAL_CO',
         '^interests_pct.*'     : 'INT_PER',
         '^main_parent.*'       : 'BASIN_NAME',
         '^net_deep.*'          : 'NET_DEEP_SQKM',
         '^net_osho.*'          : 'NET_ONSHORE_SQKM',
         '^net_shelf.*'         : 'NET_SHELF_SQKM',
         '^ons_offshore'        : 'ONS_OFFSHO',
         '^onshore_offshore'    : 'ONS_OFFSHO',
         '^onshore_sq.*'        : 'ONSHORE_SQ',
         '^operator_n.*'        : 'OPERATOR_N',
         '^previous_b.*'        : 'PREVIOUS_B',
         '^prod_expir.*'        : 'PROD_EXPIR',
         '^resource.*'          : 'RESOURCE_T',
         '^rights_typ.*'        : 'RIGHTS_TYP',
         '^shelf_sqkm.*'        : 'SHELF_SQKM',
         '^start_date.*'        : 'START_DATE',
         '^terra.*'             : 'TERRAIN',
         '^total_net_sqkm.*'    : 'NET_BLOCK_SQKM',
         '^total_sqkm.*'        : 'BLOCK_SQKM',
         '^unc_type1.*'         : 'UNC_TYPE1',
         '^unc_type2.*'         : 'UNC_TYPE2',
         '^unconv_type_1.*'     : 'UNC_TYPE1',
         '^unconv_type_2.*'     : 'UNC_TYPE2',
         '^z_max.*'             : 'MAX_WATER_',
         '^z_mean.*'            : 'MEDIAN_WAT',
         '^z_min.*'             : 'MIN_WATER_',
         }
    df_excel.columns = df_excel.columns.to_series().replace(d, regex=True)
    df_excel.fillna(0, inplace = True)
#    print(df_excel['BASIN_NAME'].head(5))

    conditions = [
            (df_excel['RESOURCE_T'] == 'Unconventional') & (df_excel['UNC_TYPE1'].notna()),
            (df_excel['RESOURCE_T'] == 'Unconventional') & (df_excel['UNC_TYPE2'].notna()),
            (df_excel['RESOURCE_T'] == 'Conven & Unconven') & (df_excel['UNC_TYPE1'].notna()),
            (df_excel['RESOURCE_T'] == 'Conven & Unconven') & (df_excel['UNC_TYPE2'].notna()),
            (df_excel['RESOURCE_T'] == 'Conventional'),
            ]
    choices = [df_excel['UNC_TYPE1'], df_excel['UNC_TYPE2'], df_excel['UNC_TYPE1'], df_excel['UNC_TYPE2'], df_excel['RESOURCE_T']]
    df_excel['HC_TYPE'] = np.select(conditions, choices, default = ' ')

    df_excel['WD_CALC'] = (
            (abs(df_excel['MIN_WATER_']) * df_excel['DEEP_WATER_SQKM']) +
            (abs(df_excel['MEDIAN_WAT']) * df_excel['SHELF_SQKM']) +
            (abs(df_excel['MAX_WATER_']) * df_excel['ONSHORE_SQKM'])
            )/df_excel['BLOCK_SQKM']
#    print(df_excel['WD_calc'].head(5))

    df_excel['ONSHORE_2D_SQKM'] = (
            abs(df_excel['ONSHORE_SQKM'])/abs(df_excel['BLOCK_SQKM'])*abs(df_excel['BLOCK_2D_SQKM'])
            )
    df_excel['SHELF_2D_SQKM'] = (
            abs(df_excel['SHELF_SQKM'])/abs(df_excel['BLOCK_SQKM'])*abs(df_excel['BLOCK_2D_SQKM'])
            )
    df_excel['DEEP_2D_WATER_SQKM'] = (
            abs(df_excel['DEEP_WATER_SQKM'])/abs(df_excel['BLOCK_SQKM'])*abs(df_excel['BLOCK_2D_SQKM'])
            )

    df_excel['NET_2D_BLOCK_SQKM'] = (
            abs(df_excel['BLOCK_2D_SQKM'])/100*abs(df_excel['INT_PER'])
            )
    df_excel['NET_2D_ONSHORE_SQKM'] = (
            abs(df_excel['ONSHORE_2D_SQKM'])/100*abs(df_excel['INT_PER'])
            )
    df_excel['NET_2D_SHELF_SQKM'] = (
            abs(df_excel['SHELF_2D_SQKM'])/100*abs(df_excel['INT_PER'])
            )
    df_excel['NET_2D_DEEP_WATER_SQKM'] = (
            abs(df_excel['DEEP_2D_WATER_SQKM'])/100*abs(df_excel['INT_PER'])
            )

#  ~(df_excel['ONS_OFFSHO'] == 'Onshore') means all elements in dataframe that are NOT 'Onshore'
    conditions2 = [
                (df_excel['ONS_OFFSHO'] == 'Onshore'),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_CALC'] >= 0) & (df_excel['WD_CALC'] < 500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_CALC'] >= 500) & (df_excel['WD_CALC'] < 1500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_CALC'] >= 1500) & (df_excel['WD_CALC'] < 3000),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (df_excel['WD_CALC'] >= 3000),
            ]
    choices2 = ['Onshore', 'Offshore', 'Deep Offshore', 'Ultra Deep Offshore', 'Frontier Deep Offshore']
    df_excel['WD'] = np.select(conditions2, choices2, default = ' ')
#    print(df_excel['WD'].head(5))

    #Rearrange and write out columns
    #df[['PROSPECT_NAME']].to_excel('Technical_POTEX.xlsx')
    df_excel[['COUNTRY_NA', 'BLOCK_N', 'BASIN_NAME', 'CO_ACR', 'INT_PER', 'CO_TYPE',
              'AWARD_DA_1', 'EXPIRY_D_1', 'GENERAL_CO', 'BLOCK_STAT',
              'BLOCK_2D_SQKM', 'ONSHORE_2D_SQKM', 'SHELF_2D_SQKM' ,'DEEP_2D_WATER_SQKM',
              'BLOCK_SQKM', 'ONSHORE_SQKM', 'SHELF_SQKM', 'DEEP_WATER_SQKM',
              'NET_2D_BLOCK_SQKM', 'NET_2D_ONSHORE_SQKM', 'NET_2D_SHELF_SQKM', 'NET_2D_DEEP_WATER_SQKM',
              'NET_BLOCK_SQKM', 'NET_ONSHORE_SQKM', 'NET_SHELF_SQKM', 'NET_DEEP_SQKM',
              'WD', 'WD_CALC', 'HC_TYPE', 'TERRAIN',
              'BLK_VLD_FLG','CNTRCT_VLD_FLG','FO_FLG',
              ]].to_excel(out)

    print ("File Extract Produced: ", out)
    return

def splitstack(out1, a):
#    fName = pass_file_path([out1])
    print("Reading file: ", out1)
    df_excel2 = readinputfile(out1, a)
    #Use example from Stack overflow - https://stackoverflow.com/questions/50731229/split-cell-into-multiple-rows-in-pandas-dataframe
    (# Set the columns that are not to be touched as the index. IN this case its only 'INT_PER'
     df_excel2.set_index(['COUNTRY_NA', 'BLOCK_N', 'BASIN_NAME', 'CO_ACR', 'CO_TYPE',
              'AWARD_DA_1', 'EXPIRY_D_1', 'GENERAL_CO', 'BLOCK_STAT',
              'BLOCK_2D_SQKM', 'ONSHORE_2D_SQKM', 'SHELF_2D_SQKM' ,'DEEP_2D_WATER',
              'BLOCK_SQKM', 'ONSHORE_SQ', 'SHELF_SQKM', 'DEEP_WATER',
              'NET_2D_BLOCK_SQKM', 'NET_2D_ONSHORE_SQ', 'NET_2D_SHELF_SQKM', 'NET_2D_DEEP_WATER',
              'NET_BLOCK_SQKM', 'NET_ONSHORE_SQ', 'NET_SHELF_SQKM', 'NET_DEEP_WATER',
              'WD', 'WD_CALC', 'HC_TYPE', 'TERRAIN',
              'BLK_VLD_FLG','CNTRCT_VLD_FLG','FO_FLG',
                  ])
    .stack()                        # Stack the rows
    .str.split(',', expand=True)    # This is now a series - call str.split on comma
    .stack()                        # Get rid of NULL values by calling stack again
    .unstack(-2)                    # Second last level of the index to become columns, so unstack using unstack(-2) (unstack on the second last level)
    .reset_index(-1, drop=True)     # Get rid of the superfluous last level using reset_index
    .reset_index()
    .to_excel(out1)
    )
    print ("File Extract Produced: ", out1)
    return

def combine_multiple(ZZ, AA):
    filenames = glob.glob('*Acerage*.xlsx',recursive=True)
    #filenames = [a, b]
    olddf=pd.DataFrame()
    for num, f in enumerate(filenames,start=1):
        if len(f)>0:
            df=pd.read_excel(f)
            olddf=pd.concat([olddf,df], ignore_index=True, sort=False).reset_index(drop=True)
    newdf = olddf[olddf['INT_PER'] >0]
    (
     newdf
     #.drop_duplicates(subset=[ZZ, AA], keep = 'last')
     .to_excel('@Competitor_Acerage_Final.xlsx')
     )
    print ("Final File Extract Produced")
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
        run_code = int(input("Choose option - (1) Extract Data (Single File) (2) Extract Data (Multiple Files) (3) Combine Multiple Files or (4) Exit: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    if run_code < 0:
        print("Sorry, your response must not be negative.")
        continue
    elif run_code >4:
        print("Incorrect Input Value - Choose only 1, 2 or 3")
        continue
    else:
        #value was successfully parsed, and we're happy with its value.
        pt = ['MY_CN_PNG_MM_Companies_20190909.xlsx']

        var1 = 'CN'
        out1 = 'Competitor_Acerage_CN.xlsx'

        var2 = 'MM'
        out2 = 'Competitor_Acerage_MM.xlsx'

        var3 = 'MY'
        out3 = 'Competitor_Acerage_MY.xlsx'

        var4 = 'PG'
        out4 = 'Competitor_Acerage_PG.xlsx'

        #checks for duplicates and drops within the whole file
        ctn1 = 'BLOCK_N'
        ctn2 = 'BLOCK_SQKM'

        #fn to read path, load file defined as 'pt'
        fName, pathlen = pass_file_path(pt)

        if run_code == 1: #mostly for testing
            df_excel = readinputfile(fName, var1)
            userinput(run_code, df_excel, out1)
#            fn = os.path.join(pathlen, out1)
#            splitstack(fn, 'Sheet1')

        elif run_code == 2:
            df_excel = readinputfile(fName, var1)
            userinput(run_code, df_excel, out1)
#            splitstack('Sheet1', out1)

            df_excel = readinputfile(fName, var2)
            userinput(run_code, df_excel, out2)
#            splitstack('Sheet1', out2)

            df_excel = readinputfile(fName, var3)
            userinput(run_code, df_excel, out3)
#            splitstack('Sheet1', out3)

            df_excel = readinputfile(fName, var4)
            userinput(run_code, df_excel, out4)
#            splitstack('Sheet1', out4)

            #combine_multiple('CONTRACT_N', 'Acerage14.xlsx', 'Acerage15.xlsx')
            combine_multiple(ctn1, ctn2)

        elif run_code == 3:
            combine_multiple(ctn1, ctn2)

        else:
            break
    count = 'Completed Process'
    elapsed = (time.time() - start)
    print ("%s in %s seconds" % (count,elapsed))
    break