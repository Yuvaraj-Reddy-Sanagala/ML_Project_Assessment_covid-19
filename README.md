# ML_Project_Assessment_covid-19
  # Project Overview:
  
    What to do?
    Need to utilize the global Covid-19 datasets to analyze trends, perform time series forecasting, and building predictive models for infection rate and vaccination rate or futre waves.

    Data Source:

    
    What was done?
    Data Cleaning and Preprocessig (Data_Cleaning Folder):
    1. Selected a dataset and cleaned the data by eliminating some of the columns by using excel.
    2. Next, the North America continent data was selected from the dataset.
    3. Finally, prepared the data by imputing the missing values by Random Forest Regression using python scripting.
    
    Exploratory Data Anlysis (Exploratory_Data_Analysis folder):
    1. The data was analyzed for infection and vaccination rates across various locations with different date filters.
    2. A dashboard was created in Tableau using GeoMap and bar charts to visualize these rates.
    3. Next, correlation is used to eliminate the features as a first step of selection procedure for the targets.
    4. Two different lists were created based on different targets.
    4. Finally, few more were eliminated by using the Recursive Feature Elimination(RFE) and 10 features were selected for each target.

    Model Creation and Analysis:
    1. Two models were created based on the above selected features one for infection rate and another for the vaccination rate 
    2. Both models were created using the Random Forest Regression. This model was selected due to complexity in data, time series and as it was related to healthcare sector.
    3. Next, different metrics such as Mean Absolute Error(MAE), Mean Squared Error(MSE), Root Mean Squared Error(RMSE), R2 Score were used to perfomance of the models.
    4. Finally, graphs are ploted for Feature Importance and Actual vs Predicted Rates for both models.
    Conclusion:
    Infection Rate:
    {'MAE': 0.0037009944801956584, 'MSE': 0.0019611721743952024, 'RMSE': 0.044285123624025285, 'R^2 Score': 0.8918852009098319}
    
    Vaccination Rate:
    {'MAE': 0.05920397226775297, 'MSE': 0.1506372680725753, 'RMSE': 0.38812017220517575, 'R^2 Score': 0.9932253679029347}
