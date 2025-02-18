# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:02:50 2024

@author: Admin
"""

import pandas as pd
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path=script_dir/"Dataset_with_required_cols.xlsx"

df=pd.read_excel(file_path)
df_NA=df[df['continent']=='North America'].copy()

df_new=df_NA.iloc[:,1:]

New_file_path=script_dir/"Dataset_NA.xlsx"

df_new.to_excel(New_file_path,index=False)



