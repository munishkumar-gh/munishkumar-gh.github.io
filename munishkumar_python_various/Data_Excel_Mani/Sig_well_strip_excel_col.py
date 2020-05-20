# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:41:42 2019

@author: J0501553

This code analyzes the significant wells over the years, extracts the features of interest,
filters and calssifies, and finally collates into 1 common dataset
For plotting with Power BI

This has now been generalized to run with either 1 file or with Multiple files

All input files extracted from IHS
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

    #Dict elements are case sensitive
    d = {'^applicat.*'          : 'APPLICAT_1',
         '^area_3d.*'           : 'BLOCK_3D_SQKM',
         '^area_2d.*'           : 'BLOCK_2D_SQKM',
         '^award_da.*'          : 'AWARD_DA_1',
         '^basin_na.*'          : 'BASIN',
         '^block_n.*'           : 'BLOCK_N',
         '^block_sqkm.*'        : 'BLOCK_SQKM',
         '^block_stat.*'        : 'BLOCK_STAT',
         '^block_val.*'         : 'BLK_VLD_FLG',
         '^company_ac.*'        : 'CO_ACR',
         '^company_ty.*'        : 'CO_TYPE',
         '^company_na.*'        : 'CO_NA',
         '^companies.*'         : 'COMP',
         '^contract_n.*'        : 'CONTRACT_N',
         '^contract_val.*'      : 'CNTRCT_VLD_FLG',
         '^contract_stat.*'     : 'CNTRCT_STAT',
         '^country_na.*'        : 'COUNTRY',
         '^current_op.*'        : 'CRNT_OPER',
         '^cond_recover.*'      : 'COND_RECOVERABLE_MMBBL',
         '^datum_name.*'        : 'DATUM_NAME',
         '^deep_water.*'        : 'DEEP_WATER_SQKM',
         '^disc_y.*'            : 'DRILL_DATE',
         '^discovery_well_na.*' : 'WELL_NAME',
         '^discovery_well_td.*' : 'WELL_TD',
         '^end_date_t.*'        : 'END_DATE_T',
         '^exp_expi.*'          : 'EXP_EXPI_1',
         '^expiry_d.*'          : 'EXPIRY_D_1',
         '^expiry_sch.*'        : 'EXPIRY_SCH',
         '^farm_out.*'          : 'FO_FLG',
         '^field_na.*'          : 'FIELD',
         '^general_co.*'        : 'GENERAL_CO',
         '^gas_recover.*'       : 'GAS_RECOVERABLE_MMSCF',
         '^hc.*'                : 'HC_TYPE',
         '^interests_pct.*'     : 'INT_PER',
         '^lat.*'               : 'LATITUDE',
         '^lon.*'               : 'LONGITUDE',
         '^main_parent.*'       : 'BASIN_NAME',
         '^net_deep.*'          : 'NET_DEEP_SQKM',
         '^net_osho.*'          : 'NET_ONSHORE_SQKM',
         '^net_shelf.*'         : 'NET_SHELF_SQKM',
         '^ons_offshore'        : 'ONS_OFFSHO',
         '^onshore_offshore'    : 'ONS_OFFSHO',
         '^onshore_sq.*'        : 'ONSHORE_SQKM',
         '^operator.*'          : 'OPERATOR',
         '^oil_recover.*'       : 'OIL_RECOVERABLE_MMBBL',
         '^previous_b.*'        : 'PREVIOUS_B',
         '^prod_expir.*'        : 'PROD_EXPIR',
         '^prod_stat.*'         : 'PROD_STAT',
         '^resource.*'          : 'RESOURCE_T',
         '^rights_typ.*'        : 'RIGHTS_TYP',
         '^remarks.*'           : 'REMARKS',
         '^shelf_sqkm.*'        : 'SHELF_SQKM',
         '^start_date.*'        : 'START_DATE',
         '^terra.*'             : 'TERRAIN',
         '^total_net_sqkm.*'    : 'NET_BLOCK_SQKM',
         '^total_sqkm.*'        : 'BLOCK_SQKM',
         '^total_recover.*'     : 'HC_RECOVERABLE_MMBOE',
         '^unc_type1.*'         : 'UNC_TYPE1',
         '^unc_type2.*'         : 'UNC_TYPE2',
         '^unconv_type_1.*'     : 'UNC_TYPE1',
         '^unconv_type_2.*'     : 'UNC_TYPE2',
         '^water_depth.*'       : 'WAT_DEP',
         '^z_max.*'             : 'MAX_WATER_',
         '^z_mean.*'            : 'MEDIAN_WAT',
         '^z_min.*'             : 'MIN_WATER_',
         }
    df_excel.columns = df_excel.columns.to_series().replace(d, regex=True)
    df_excel.fillna(0, inplace = True)
#    print(df_excel['WAT_DEP'].head(5))

    conditions = [
            df_excel['HC_TYPE'].str.contains("ydrate", case = False, regex = True)==True,
            df_excel['HC_TYPE'].str.contains("hal", case = False, regex = True)==True,
            df_excel['HC_TYPE'].str.contains("igh", case = False, regex = True)==True,
            df_excel['HC_TYPE'].str.contains("oa", case = False, regex = True)==True,
            df_excel['HC_TYPE'].str.contains("as,con", case = False, regex = True)==True,
            df_excel['HC_TYPE'].str.contains("ondensat", case = False, regex = True)==True,
            df_excel['HC_TYPE'].str.contains("oi", case = False, regex = True)==True
            ]
    choices = ['Unconventional', 'Unconventional', 'Unconventional', 'Unconventional', 'Condensate', 'Condensate', 'Oil']
    df_excel['HC'] = np.select(conditions, choices, default = 'Gas')

#  ~(df_excel['ONS_OFFSHO'] == 'Onshore') means all elements in dataframe that are NOT 'Onshore'
    conditions2 = [
                (df_excel['ONS_OFFSHO'] == 'Onshore'),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['WAT_DEP']) >= 0) & (abs(df_excel['WAT_DEP']) < 500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['WAT_DEP']) >= 500) & (abs(df_excel['WAT_DEP']) < 1500),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['WAT_DEP']) >= 1500) & (abs(df_excel['WAT_DEP']) < 3000),
                (~(df_excel['ONS_OFFSHO'] == 'Onshore')) & (abs(df_excel['WAT_DEP']) >= 3000),
            ]
    choices2 = ['Onshore', 'Offshore', 'Deep Offshore', 'Ultra Deep Offshore', 'Frontier Deep Offshore']
    df_excel['WD'] = np.select(conditions2, choices2, default = ' ')

    df_excel['WATER_DEPTH']=abs(df_excel['WAT_DEP'])

    #Rearrange and write out columns
    #df[['PROSPECT_NAME']].to_excel('Technical_POTEX.xlsx')
    if run_code == 1:
        df_excel[
                [
                'COUNTRY',
                'BASIN',
                'FIELD',
                'DRILL_DATE',
                'WELL_NAME',
                'WELL_TD',
                'WATER_DEPTH',
                'WD',
                'LATITUDE',
                'LONGITUDE',
                'GENERAL_CO',
                'OPERATOR',
                'CRNT_OPER',
                'COMP',
                'HC_TYPE',
                'HC',
                'PROD_STAT',
                'GAS_RECOVERABLE_MMSCF',
                'COND_RECOVERABLE_MMBBL',
                'OIL_RECOVERABLE_MMBBL',
                'HC_RECOVERABLE_MMBOE',
                ]
                ].to_excel(out)

    print ("File Extract Produced: ", out)
    return


####---------------------Main-----------------------------------####

while True:
    try:
        run_code = int(input("Choose option - (1) Extract Significant Well Data (Single File) or (2) Exit: "))
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
            pt = 'W:/Group/EXPLO/APC/$CONSOLIDATION/APC_02_Potex/0 2019 PORTFOLIO/9 ACREAGE ANALYSIS/2_Processed/APC_FIELD_SIGNIFICANT_WELLS_STATS.xlsx'
            df_excel = readinputfile(pt, 'APC_FIELD_SIGNIFICANT_WELLS_STA')
            userinput(run_code, df_excel, 'Significant_Well_Final.xlsx')
        else:
            #we're ready to exit the loop.
            break
    count = 'Completed Process'
    elapsed = (time.time() - start)
    print ("%s in %s seconds" % (count,elapsed))
    break