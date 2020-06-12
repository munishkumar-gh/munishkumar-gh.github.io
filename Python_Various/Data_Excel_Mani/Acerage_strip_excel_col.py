# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:27:10 2019

@author: Munish

https://morphocode.com/pandas-cheat-sheet/

This code analyzes the contract data over the years, extracts the features of interest,
filters and calssifies, and finally collates into 1 common dataset
For plotting with Power BI

This has now been generalized to run with either 1 file or with Multiple files

Note however that the output files in the single file case has an additional column
called 'Area_3D_sqkm'

All input files extracted from IHS; this means that for Woodmac this code has to be
modified

"""
import time
import numpy as np
import pandas as pd
import glob

start = time.time()

####---------------------Functions---------------------------------####
def readinputfile(pt, a):
    print ("File Read In: ", a)
    df_excel = pd.read_excel(pt,
    sheet_name = a,
    skiprows = 0 # header data
    )
    return df_excel

def userinput(run_code, df_excel, out):

    df_excel.columns = map(str.lower, df_excel.columns)
    #Write out to single file with multiple filter
    #df1 = df_excel[(df_excel['RESOURCE_T'] == 'Unconventional') | (df_excel['RESOURCE_T'] == 'Conven & Unconven')]:

    #Dict elements are case sensitive
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
         '^company_na.*'        : 'CO_NA',
         '^contract_n.*'        : 'CONTRACT_N',
         '^contract_val.*'      : 'CNTRCT_VLD_FLG',
         '^contract_stat.*'     : 'CNTRCT_STAT',
         '^country_na.*'        : 'COUNTRY_NA',
         '^datum_name.*'        : 'DATUM_NAME',
         '^deep_water.*'        : 'DEEP_WATER_SQKM',
         '^end_date_t.*'        : 'END_DATE_T',
         '^exp_expi.*'          : 'EXP_EXPI_1',
         '^expiry_d.*'          : 'EXPIRY_D_1',
         '^expiry_sch.*'        : 'EXPIRY_SCH',
         '^farm_out.*'          : 'FO_FLG',
         '^general_co.*'        : 'GENERAL_CO',
         '^interests_pct.*'     : 'INT_PER',
         '^int_pct.*'           : 'INT_PER',
         '^main_parent.*'       : 'BASIN_NAME',
         '^net_deep.*'          : 'NET_DEEP_SQKM',
         '^net_osho.*'          : 'NET_ONSHORE_SQKM',
         '^net_shelf.*'         : 'NET_SHELF_SQKM',
         '^ons_offshore'        : 'ONS_OFFSHO',
         '^onshore_offshore'    : 'ONS_OFFSHO',
         '^onshore_sq.*'        : 'ONSHORE_SQKM',
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
         '^total_int.*'         : 'INT_PER',
         '^unc_type1.*'         : 'UNC_TYPE1',
         '^unc_type2.*'         : 'UNC_TYPE2',
         '^unconv_type_1.*'     : 'UNC_TYPE1',
         '^unconv_type_2.*'     : 'UNC_TYPE2',
         '^z_max.*'             : 'MAX_WATER_',
         '^zmax.*'              : 'MAX_WATER_',
         '^z_mean.*'            : 'MEDIAN_WAT',
         '^zmean.*'             : 'MEDIAN_WAT',
         '^z_min.*'             : 'MIN_WATER_',
         '^zmin.*'              : 'MIN_WATER_',
         }
    df_excel.columns = df_excel.columns.to_series().replace(d, regex=True)
    df_excel.fillna(0, inplace = True)
#    print(df_excel['RESOURCE_T'].head(5))

    conditions = [
            (~(df_excel['RESOURCE_T'] == 'Conventional')) & (df_excel['UNC_TYPE1'].notna()),
            (~(df_excel['RESOURCE_T'] == 'Conventional')) & (df_excel['UNC_TYPE2'].notna()),
            (~(df_excel['RESOURCE_T'] == 'Conventional')),
            (df_excel['RESOURCE_T'] == 'Conventional'),
            ]
    choices = [df_excel['UNC_TYPE1'], df_excel['UNC_TYPE2'], df_excel['UNC_TYPE1'], df_excel['RESOURCE_T']]
    df_excel['HC_TYPE'] = np.select(conditions, choices, default = ' ')

    df_excel['WD_CALC'] = (
            (abs(df_excel['MIN_WATER_']) * df_excel['DEEP_WATER_SQKM']) +
            (abs(df_excel['MEDIAN_WAT']) * df_excel['SHELF_SQKM']) +
            (abs(df_excel['MAX_WATER_']) * df_excel['ONSHORE_SQKM'])
            )/df_excel['BLOCK_SQKM']
#    print(df_excel['WD_CALC'].head(5))

    df_excel['ONSHORE_2D_SQKM'] = (
            abs(df_excel['ONSHORE_SQKM'])/abs(df_excel['BLOCK_SQKM'])*abs(df_excel['BLOCK_2D_SQKM'])
            )
    df_excel['SHELF_2D_SQKM'] = (
            abs(df_excel['SHELF_SQKM'])/abs(df_excel['BLOCK_SQKM'])*abs(df_excel['BLOCK_2D_SQKM'])
            )
    df_excel['DEEP_2D_WATER_SQKM'] = (
            abs(df_excel['DEEP_WATER_SQKM'])/abs(df_excel['BLOCK_SQKM'])*abs(df_excel['BLOCK_2D_SQKM'])
            )
    if run_code == 2:
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

    conditions3 = [
                (df_excel['ONS_OFFSHO'] == 'Onshore'),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['MEDIAN_WAT']) >= 0) & (abs(df_excel['MEDIAN_WAT']) < 500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['MEDIAN_WAT']) >= 500) & (abs(df_excel['MEDIAN_WAT']) < 1500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['MEDIAN_WAT']) >= 1500) & (abs(df_excel['MEDIAN_WAT']) < 3000),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['MEDIAN_WAT']) >= 3000),
            ]
    choices3 = ['Onshore', 'Offshore', 'Deep Offshore', 'Ultra Deep Offshore', 'Frontier Deep Offshore']
    df_excel['WD_MED'] = np.select(conditions3, choices3, default = ' ')

    df_excel['MAX_WD'] = abs(df_excel['MIN_WATER_'])
    df_excel['MED_WD'] = abs(df_excel['MEDIAN_WAT'])
    df_excel['MIN_WD'] = abs(df_excel['MAX_WATER_'])

    #Rearrange and write out columns
    #df[['PROSPECT_NAME']].to_excel('Technical_POTEX.xlsx')
    if run_code ==1:
        df_excel[
                [
                'COUNTRY_NA',
                'CONTRACT_N',
                'BASIN_NAME',
                #'OPERATOR_N',
                #'CO_NA',
                #'CO_ACR',
                #'RIGHTS_TYP',
                'AWARD_DA_1',
                'EXPIRY_D_1',
                #'EXPIRY_SCH',
                'GENERAL_CO',
                'BLOCK_STAT',
                'BLOCK_SQKM',
                'BLOCK_2D_SQKM',
                #'NET_2D_BLOCK_SQKM',
                'ONSHORE_SQKM',
                'ONSHORE_2D_SQKM',
                #'NET_2D_ONSHORE_SQKM',
                'SHELF_SQKM',
                'SHELF_2D_SQKM',
                #'NET_2D_SHELF_SQKM',
                'DEEP_WATER_SQKM',
                'DEEP_2D_WATER_SQKM',
                #'NET_2D_DEEP_WATER_SQKM',
                'MIN_WD',
                'MED_WD',
                'MAX_WD',
                'WD_MED',
                'WD_CALC',
                'WD',
                'TERRAIN',
                #'PREVIOUS_B',
                #'DATUM_NAME',
                'HC_TYPE',
                'BLK_VLD_FLG',
                'CNTRCT_STAT',
                #'CO_TYPE',
                'INT_PER'
                  ]
        ].to_excel(out)


    elif run_code == 2:
        df_excel[
                [
                'COUNTRY_NA',
                'CONTRACT_N',
                'BASIN_NAME',
                #'OPERATOR_N',
                'CO_NA',
                'CO_ACR',
                #'RIGHTS_TYP',
                'AWARD_DA_1',
                #'END_DATE_T',
                #'EXPIRY_SCH',
                'GENERAL_CO',
                'BLOCK_STAT',
                'BLOCK_SQKM',
                'BLOCK_2D_SQKM',
                'NET_2D_BLOCK_SQKM',
                'ONSHORE_SQKM',
                'ONSHORE_2D_SQKM',
                'NET_2D_ONSHORE_SQKM',
                'SHELF_SQKM',
                'SHELF_2D_SQKM',
                'NET_2D_SHELF_SQKM',
                'DEEP_WATER_SQKM',
                'DEEP_2D_WATER_SQKM',
                'NET_2D_DEEP_WATER_SQKM',
                'MIN_WD',
                'MED_WD',
                'MAX_WD',
                'WD_MED',
                'WD_CALC',
                'WD',
                'TERRAIN',
                #'PREVIOUS_B',
                #'DATUM_NAME',
                'HC_TYPE',
                'BLK_VLD_FLG',
                'CNTRCT_STAT',
                'CO_TYPE',
                  ]
        ].to_excel(out)

    else:
        df_excel[
                [
                'CONTRACT_N',
                'COUNTRY_NA',
                'BASIN_NAME',
                'OPERATOR_N',
                'RIGHTS_TYP',
                'AWARD_DA_1',
                'END_DATE_T',
                'EXPIRY_SCH',
                'GENERAL_CO',
                'BLOCK_STAT',
                'WD',
                'BLOCK_SQKM',
                'ONSHORE_SQKM',
                'SHELF_SQKM',
                'DEEP_WATER_SQKM',
                'WD_CALC',
                'PREVIOUS_B',
                'DATUM_NAME',
                'HC_TYPE',
                'BLK_VLD_FLG',
                ]
        ].to_excel(out)

    print ("File Extract Produced: ", out)
    return

def combine_multiple(ZZ, AA):
    filenames = glob.glob('Acerage*.xlsx',recursive=True)
    #filenames = [a, b]
    olddf=pd.DataFrame()
    for num, f in enumerate(filenames,start=1):
        if len(f)>0:
            df=pd.read_excel(f)
            olddf=pd.concat([olddf,df], ignore_index=True).reset_index(drop=True)
    olddf.drop_duplicates(subset=[ZZ, AA], keep = 'last').to_excel('@Acerage_Evolution_Final.xlsx')
    print ("Final File Extract Produced")
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
        run_code = int(input("Choose option - (1) Extract Acerage Data (Single Company) (2) Extract Acerage Data (All Competitors) (3) Extract Acerage Data (Multiple Files) or (4) Exit: "))
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
        if run_code == 1:
            pt = 'W:/Group/EXPLO/APC/$CONSOLIDATION/APC_02_Potex/0 2020 PORTFOLIO/9 ACREAGE ANALYSIS/1_Raw/0_Blocks_Licences/20200130/APC_Total_Blocks_30Jan2020.xls'
            df_excel = readinputfile(pt, 'TOTAL_BLOCKS')
            userinput(run_code, df_excel, 'Acerage_Evolution_Total_Final.xlsx')

        elif run_code == 2:
            pt = 'W:/Group/EXPLO/APC/$CONSOLIDATION/APC_02_Potex/0 2020 PORTFOLIO/9 ACREAGE ANALYSIS/1_Raw/0_Blocks_Licences/20200130/All_Competitors_and_Total_Current_30Jan2020_Acreage.xls'
            df_excel = readinputfile(pt, 'APC_Companies_Valid_Contract')
            userinput(run_code, df_excel, 'Acerage_Evolution_Final.xlsx')

        elif run_code == 3:
            pt = 'W:/Group/EXPLO/APC/$CONSOLIDATION/APC_02_Potex/0 2019 PORTFOLIO/9 ACREAGE ANALYSIS/2_Processed/@Valid_Contracts_2014_2019_Total.xlsx'
            df_excel = readinputfile(pt, 'ValidContracts2014_Total')
            userinput(run_code, df_excel, 'Acerage14.xlsx')
            df_excel = readinputfile(pt, 'ValidContracts2015_Total')
            userinput(run_code, df_excel, 'Acerage15.xlsx')
            df_excel = readinputfile(pt, 'ValidContracts2016_Total')
            userinput(run_code, df_excel, 'Acerage16.xlsx')
            df_excel = readinputfile(pt, 'ValidContracts2017_Total')
            userinput(run_code, df_excel, 'Acerage17.xlsx')
            df_excel = readinputfile(pt, 'ValidContracts2018_Total')
            userinput(run_code, df_excel, 'Acerage18.xlsx')
            df_excel = readinputfile(pt, 'ValidContracts2019_Total')
            userinput(run_code, df_excel, 'Acerage19.xlsx')
            #combine_multiple('CONTRACT_N', 'Acerage14.xlsx', 'Acerage15.xlsx')
            combine_multiple('CONTRACT_N', 'BLOCK_SQKM')
        else:
            #we're ready to exit the loop.
            break
    count = 'Completed Process'
    elapsed = (time.time() - start)
    print ("%s in %s seconds" % (count,elapsed))
    break