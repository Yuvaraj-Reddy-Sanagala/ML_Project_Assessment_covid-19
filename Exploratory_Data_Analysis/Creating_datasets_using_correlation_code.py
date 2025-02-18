# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:34:20 2025

@author: Admin
"""

import pandas as pd
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir.parent / "Data_Cleaning" / "Dataset_with_targets_and_encoded.xlsx"

df=pd.read_excel(file_path)

df_numeric_cols=df.iloc[:,2:]
non_numeric_cols=list(df.iloc[:,:2].columns)

df_corr_1= dict(df_numeric_cols.corr()['infection_rate'])
df_corr_2=dict(df_numeric_cols.corr()['vaccination_rate'])


x=[]
x.extend(non_numeric_cols) 
for i in df_corr_1.keys():
    if abs(df_corr_1[i])>0.005:
        x.append(i)

y=[]
y.extend(non_numeric_cols) 
for i in df_corr_2.keys():
    if abs(df_corr_2[i])>0.05:
        y.append(i)


New_file_path_1=script_dir/"Correlated_cols_for_infection_rate_and_vaccination_rate.txt"

with open(New_file_path_1, "w") as file:
    file.write(str([x,y]))

    