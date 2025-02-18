# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:16:59 2025

@author: Admin
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error, root_mean_squared_error,r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir.parent /"Data_Cleaning"/"Dataset_with_targets_and_encoded.xlsx"

cols_file_path=script_dir.parent /"Exploratory_Data_Analysis"/"Vaccination_rate_dataset_selected_features.txt"

df=pd.read_excel(file_path)

with open(cols_file_path, "r") as file:
    file_content = file.read()
    
read_list = eval(file_content)


X=df[read_list[:10]]
Y=df['vaccination_rate']

X_train, X_test, y_train, y_test=train_test_split(X, Y, test_size=0.20,shuffle=True,random_state=42)

rf_estimator = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)

rf_fit=rf_estimator.fit(X_train,y_train)

y_pred=rf_fit.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse=mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)

performance_metrics={"MAE": mae, "MSE": mse, "RMSE": rmse, "R^2 Score": r2}

New_file_path=script_dir/"Performance_mertics_for_vaccination_rate.txt"

with open(New_file_path, "w") as file:
    file.write(str(performance_metrics))
    
feature_importances=rf_fit.feature_importances_
indices=np.argsort(feature_importances)
names=np.array(X_train.columns)[indices]

plt.figure(figsize=(10, 6))
plt.barh(names, feature_importances[indices], color='green')
plt.xlabel("Feature Importance")
plt.ylabel("Feature Names")
plt.title("Feature Importance for Vaccination Rate Prediction")

save_path=script_dir/"Vaccination_Rate_Feature_Importances.jpg"
plt.savefig(save_path)

plt.show()


residuals= abs(y_test-y_pred)

plt.figure(figsize=(10,6))
sns.scatterplot(x=y_test,y=y_pred, hue=residuals, palette="coolwarm")
sns.lineplot(x=[y_test.min(), y_test.max()], y=[y_test.min(), y_test.max()], color='Red', linestyle='-.')
plt.xlabel('Actual Vaccination Rate')
plt.ylabel('Predicted Vaccination Rate')
plt.title('Actual vs Predicted Vaccination Rate')

save_path=script_dir/"Actual_vs_Predicted_Vaccination_Rate.jpg"
plt.savefig(save_path)

plt.show()
