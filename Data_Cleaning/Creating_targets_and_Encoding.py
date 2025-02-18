# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:03:17 2025

@author: Admin
"""
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path=script_dir/"Dataset_imputed.xlsx"

df=pd.read_excel(file_path)


frequency=df['location'].value_counts(normalize=True)
df['location_encoded']=df['location'].map(frequency)

oe=OrdinalEncoder()
df['date_encoded'] = oe.fit_transform(df[['date']])


df.insert(2, 'location_encoded', df.pop('location_encoded'))
df.insert(3, 'date_encoded', df.pop('date_encoded'))    

df['vaccination_rate']=(df['new_vaccinations']/df['population'])*100
df['infection_rate']=(df['new_cases']/df['population'])*100


New_file_path=script_dir/"Dataset_with_targets_and_encoded.xlsx"

df_new=df.iloc[:,2:]

df_new.to_excel(New_file_path, index=False)
