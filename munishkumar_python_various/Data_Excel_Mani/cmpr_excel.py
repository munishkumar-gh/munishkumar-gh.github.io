# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:20:24 2019

@author: J0501553

Compare 2 excel sheets quickly
Create a UID column as column 0
Remove all duplicates in each sheet

"""
import pandas as pd
from pathlib import Path


def excel_diff(path_OLD, path_NEW, index_col):

    df_OLD = pd.read_excel(path_OLD, index_col=index_col).fillna(0)
    df_NEW = pd.read_excel(path_NEW, index_col=index_col).fillna(0)
    df_NEW['is_duplicated'] = df_NEW.duplicated()
    df_NEW = df_NEW.loc[df_NEW['is_duplicated'] == False]

    # Perform Diff
    dfDiff = df_NEW.copy()
    droppedRows = []
    newRows = []

    cols_OLD = df_OLD.columns
    cols_NEW = df_NEW.columns
    sharedCols = list(set(cols_OLD).intersection(cols_NEW))

    for row in dfDiff.index:
        if (row in df_OLD.index) and (row in df_NEW.index):
            for col in sharedCols:
                value_OLD = df_OLD.loc[row,col]
                value_NEW = df_NEW.loc[row,col]
                if value_OLD==value_NEW:
                    dfDiff.loc[row,col] = df_NEW.loc[row,col]
                else:
                    dfDiff.loc[row,col] = ('{}→{}').format(value_OLD,value_NEW)
        else:
            newRows.append(row)

    for row in df_OLD.index:
        if row not in df_NEW.index:
            droppedRows.append(row)
            dfDiff = dfDiff.append(df_OLD.loc[row,:])

            """
            line 51 has to be commented out if there are symbols in file. Still buggy
            """
            dfDiff = dfDiff.sort_index().fillna('')
            print(dfDiff)
            print('Dropped Rows: {}'.format(droppedRows))
            print('\nNew Rows:   {}'.format(newRows))


    # Save output and format
    fname = '{} vs {}.xlsx'.format(path_OLD.stem,path_NEW.stem)
    writer = pd.ExcelWriter(fname, engine='xlsxwriter')

    dfDiff.to_excel(writer, sheet_name='DIFF', index=True)
    df_NEW.to_excel(writer, sheet_name=path_NEW.stem, index=True)
    df_OLD.to_excel(writer, sheet_name=path_OLD.stem, index=True)

    # get xlsxwriter objects
    workbook  = writer.book
    worksheet = writer.sheets['DIFF']
    worksheet.hide_gridlines(2)
    worksheet.set_default_row(15)

    # define formats
    date_fmt = workbook.add_format({'align': 'center', 'num_format': 'yyyy-mm-dd'})
    center_fmt = workbook.add_format({'align': 'center'})
    number_fmt = workbook.add_format({'align': 'center', 'num_format': '#,##0.00'})
    cur_fmt = workbook.add_format({'align': 'center', 'num_format': '$#,##0.00'})
    perc_fmt = workbook.add_format({'align': 'center', 'num_format': '0%'})
    grey_fmt = workbook.add_format({'font_color': '#E0E0E0'})
    highlight_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color':'#B1B3B3'})
    new_fmt = workbook.add_format({'font_color': '#32CD32','bold':True})

    # set format over range
    ## highlight changed cells
    worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                            'criteria': 'containing',
                                            'value':'→',
                                            'format': highlight_fmt})

    ## highlight unchanged cells
#    worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
#                                            'criteria': 'not containing',
#                                            'value':'→',
#                                            'format': grey_fmt})

    # highlight new/changed rows
    for row in range(dfDiff.shape[0]):
        if row+1 in newRows:
            worksheet.set_row(row+1, 15, new_fmt)
        if row+1 in droppedRows:
            worksheet.set_row(row+1, 15, grey_fmt)

    # save
    writer.save()
    print('\nDone.\n')


def main():
    path_OLD = Path('old_Acerage_Evo_Total_Final.xlsx') # Previous Month
    path_NEW = Path('Acerage_Evolution_Total_Final.xlsx') # Current Month

    # get index col from data
    df = pd.read_excel(path_NEW)
    index_col = df.columns[1]
    print('\nIndex column: {}\n'.format(index_col))

    excel_diff(path_OLD, path_NEW, index_col)

if __name__ == '__main__':
    main()