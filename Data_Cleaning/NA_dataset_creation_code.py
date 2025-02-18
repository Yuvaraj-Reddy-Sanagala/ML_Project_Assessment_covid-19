# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:02:50 2024

@author: Admin
"""

import pandas as pd

file_path="C:/Users/Admin/Desktop/ML Project/ML_Project_Assessment_covid-19/Data_Cleaning/Dataset_with_required_cols.xlsx"

df=pd.read_excel(file_path)
df_NA=df[df['continent']=='North America'].copy()

df_new=df_NA.iloc[:,1:]

New_file_path="C:/Users/Admin/Desktop/ML Project/ML_Project_Assessment_covid-19/Data_Cleaning/Dataset_NA.xlsx"

df_new.to_excel(New_file_path,index=False)



