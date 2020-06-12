# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:35:47 2020

@author: Munish Kumar

Script to rad multiple Excel tabs and extract information of relevance
In this case, the multiple tabs are country tabs,
and the information to extract from each is
(a) license (col A)
(b) contract type (col B)
(c) number of blocks (col C)
(d) gross onshore acreage (sqkm) (col D)
(e) gross offshore acreage (sqkm) (col E)
(f) Entry Date TOTAL (col L)
(g) Exit Dat TOTAL (col M)
(i) Partners (col N)
(j) Total PI% (col O)
(k) Total WI% (P)

"""
import time
import numpy as np
import pandas as pd
import glob
import os

start = time.time()


dir_name = 'C:/Users/J0501553/AnacondaProjects/'
base_filename = 'Gesper_Licenses_28Jan20'
filename_suffix = 'xlsx'
exls_sht = os.path.join(dir_name, base_filename + "." + filename_suffix)

skiprows = 1
skipfooter = 5
usecols = "A:E, L:P"

def userinput(run_code, df_excel, out):

    df = df_excel.rename(columns =
              {"License":"License", "Type of":"Contract",
               "Nbr": "Blocks", "Gross Acreage(km²)":"Gross Onshore Acreage(km²)",
               "Unnamed: 4":"Gross offshore Acreage(km²)","Unnamed: 11":"Entry Date Total",
               "Unnamed: 12":"Exit Date Total","Operator":"Operator",
               "PI(%)":"PI(%)","WI(%)":"WI(%)"
               })
    # Forward fill all columns.
    df = df.fillna(method='ffill')
    df = df[df.Operator != 'Total']
    conditions = [
            ]

    if run_code == 1:
        df[[
            'License',
            'Contract',
            'Blocks',
            'Gross Onshore Acreage(km²)',
            'Gross offshore Acreage(km²)',
            'Entry Date Total',
            'Exit Date Total',
            'Operator',
            'PI(%)',
            'WI(%)'
        ]].to_excel(out)
    print ("File Extract Produced: ", out)
    return


####---------------------Main-----------------------------------####
while True:
    try:
        run_code = int(input("Choose option - (1) Extract License Data (Single Country) (2) Extract License Data (All Countries) or (3) Exit: "))
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
        xl = pd.ExcelFile(exls_sht)
        if run_code == 1:
            txt = input("Worksheet name: ")
            txtf = txt.lower().upper()
            df = pd.read_excel(xl, txtf)
            total_rows = len(df.index)
            df = xl.parse(txtf, skiprows=skiprows, skipfooter=skipfooter, usecols=usecols)
            print(df)
            out_sht = txtf + "." + filename_suffix
            userinput(run_code, df, out_sht)

        elif run_code == 2:
            for sh in xl.sheet_names:
                df = xl.parse(sh, skiprows=skiprows, skipfooter=skipfooter, usecols=usecols)
                print('Processing: [{}] ...'.format(sh))
                print(df)

        else:
            #we're ready to exit the loop.
            break
    count = 'Completed Process'
    elapsed = (time.time() - start)
    print ("%s in %s seconds" % (count,elapsed))
    break