# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:27:47 2025

@author: Admin
"""
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor

df = pd.read_excel("C:/Users/Admin/Desktop/ML Project/Data_Cleaning/Dataset_NA.xlsx")

numeric_columns = df.select_dtypes(include=['number']).columns
non_numeric_columns = df.select_dtypes(exclude=['number']).columns

rf_estimator = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
imputer = IterativeImputer(estimator=rf_estimator, max_iter=10, random_state=42)

df_numeric = df[numeric_columns]
df_numeric_imputed = pd.DataFrame(imputer.fit_transform(df_numeric), columns=numeric_columns)

df_imputed = pd.concat([df[non_numeric_columns], df_numeric_imputed], axis=1)

df_imputed.to_excel("C:/Users/Admin/Desktop/ML Project/Data_Cleaning/Dataset_imputed.xlsx", index=False)
