# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:19:29 2025

@author: Admin
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor


file_path="C:/Users/Admin/Desktop/ML Project/ML_Project_Assessment_covid-19/Data_Cleaning/Dataset_with_targets_and_encoded.xlsx"

cols_file_path="C:/Users/Admin/Desktop/ML Project/ML_Project_Assessment_covid-19/Exploratory_Data_Analysis/Correlated_cols_for_infection_rate_and_vaccination_rate.txt"

df=pd.read_excel(file_path)

with open(cols_file_path, "r") as file:
    file_content = file.read()
    
read_list = eval(file_content)

X=df[read_list[1][:17]]
Y=df['vaccination_rate']

X_train, X_test, y_train, y_test=train_test_split(X, Y, test_size=0.20,shuffle=True,random_state=42)

rf_estimator = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)

rfe_selector = RFE(estimator=rf_estimator, n_features_to_select=10, step=1)
x=rfe_selector.fit(X_train, y_train)


selected_features = X_train.columns[rfe_selector.support_].tolist()

selected_features.append("vaccination_rate")
    
print("Selected features:", selected_features)

New_file_path="C:/Users/Admin/Desktop/ML Project/ML_Project_Assessment_covid-19/Exploratory_Data_Analysis/Vaccination_rate_dataset_selected_features.txt"

with open(New_file_path, "w") as file:
    file.write(str(selected_features))