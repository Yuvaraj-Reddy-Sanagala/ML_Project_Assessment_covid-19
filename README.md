# ML_Project_Assessment_covid-19
  ## **Project Overview**

### **What to Do?**
Utilize global COVID-19 datasets to analyze trends, perform time series forecasting, and build predictive models for infection and vaccination rates, as well as predicting future waves.

---

### **Data Source**
(Global COVID-19 datasets used for analysis.)

---

### **What Was Done?**

#### **Data Cleaning and Preprocessing (Data_Cleaning Folder):**
1. Selected a dataset and cleaned the data by eliminating unnecessary columns using Excel.
2. Filtered data specific to the North American continent.
3. Imputed missing values using **Random Forest Regression** in Python.

---

#### **Exploratory Data Analysis (Exploratory_Data_Analysis Folder):**
1. Analyzed infection and vaccination rates across various locations using different date filters.
2. Created a **Tableau dashboard** with **GeoMap and bar charts** for visualization.
3. Applied **correlation analysis** to eliminate irrelevant features as the first step of feature selection for targets.
4. Created two separate feature lists based on different targets.
5. Further refined the features using **Recursive Feature Elimination (RFE)**, selecting **10 key features** for each target.

---

#### **Model Creation and Analysis**
1. Developed two models:
   - **Infection Rate Prediction Model**
   - **Vaccination Rate Prediction Model**
2. Used **Random Forest Regression** due to the dataset’s complexity, time-series nature, and relevance to the healthcare sector.
3. Evaluated model performance using metrics:
   - **Mean Absolute Error (MAE)**
   - **Mean Squared Error (MSE)**
   - **Root Mean Squared Error (RMSE)**
   - **R² Score**
4. Plotted graphs for **Feature Importance** and **Actual vs. Predicted Rates** for both models.

---

#### **Conclusion**

##### **Infection Rate Model Performance:**
- **MAE:** 0.0037  
- **MSE:** 0.00196  
- **RMSE:** 0.0443  
- **R² Score:** 0.8919
The Random Forest Regression model effectively predicts infection rates with a high degree of accuracy.
The R² Score of 0.8919 indicates that approximately 89.19% of the variance in infection rates is explained by the model.
Additionally, the low MAE (0.0037) and RMSE (0.0443) suggest minimal prediction errors, reinforcing the model’s reliability.

#### **Actual vs Predicted Infection Rate**
![Actual vs Predicted Infection Rate](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Actual_vs_Predicted_Infection_Rate.jpg)

#### **Infection Rate Feature Importance**
![Infection Rate Feature Importance](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Infection_Rate_Feature_Importances.jpg)

#### **Vaccination Rate Model Performance:**
- **MAE:** 0.0592  
- **MSE:** 0.1506  
- **RMSE:** 0.3881  
- **R² Score:** 0.9932
The Random Forest Regression model demonstrates exceptional performance in predicting vaccination rates.
With an R² Score of 0.9932, the model explains 99.32% of the variance, indicating a near-perfect fit.
The low MAE (0.0592) and RMSE (0.3881) suggest minimal errors in prediction, making it highly reliable for forecasting vaccination trends.

#### **Actual vs Predicted Vaccination Rate**
![Actual vs Predicted Vaccination Rate](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Actual_vs_Predicted_Vaccination_Rate.jpg)

#### **Vaccination Rate Feature Importance**
![Vaccination Rate Feature Importance](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Vaccination_Rate_Feature_Importances.jpg)

---

This project successfully utilized machine learning techniques to analyze COVID-19 infection and vaccination trends, providing accurate predictions and valuable insights for future forecasting.


