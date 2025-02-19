# **COVID-19 Infection & Vaccination Rate Prediction**

This repository contains the code and documentation for a machine learning project aimed at predicting **COVID-19 infection** and **vaccination rates**. The project leverages global COVID-19 datasets with a focus on **North America** and utilizes machine learning techniques to provide accurate forecasts that can aid in real-world decision-making.

---

## Table of Contents

- [**Project Overview**](#project-overview)
- [**Data Source**](#data-source)
- [**Key Calculations**](#key-calculations)
- [**Thought Process**](#thought-process)
- [**Challenges Faced**](#challenges-faced)
- [**Results Interpretation**](#results-interpretation)
- [**Next Steps**](#next-steps)
- [**Deployment Considerations**](#deployment-considerations)
- [**Model Justification**](#model-justification)
- [**Conclusion**](#conclusion)

---

## **Project Overview**

The primary goal of this project is to analyze global **COVID-19 datasets**, focusing on:
- **Infection Rate Prediction**
- **Vaccination Rate Prediction**

Using **Random Forest Regression** as the primary modeling approach, the project involves:
- **Data Cleaning & Preprocessing:**  
  - Removing unnecessary columns using **Excel**.
  - Filtering data specific to **North America**.
  - Imputing missing values using **Random Forest Regression**.
  
- **Exploratory Data Analysis (EDA):**
  - Visualization of infection and vaccination trends using **Tableau dashboards** (GeoMap and bar charts).
  - Applying **correlation analysis** for preliminary feature selection.
  - Using **Recursive Feature Elimination (RFE)** to finalize a list of **10 key features** per target.

- **Model Development & Evaluation:**
  - Building and evaluating separate **Random Forest Regression** models for predicting infection and vaccination rates.
  - Evaluating performance with metrics such as **MAE**, **MSE**, **RMSE**, and **R² Score**.
  - Visualizing model outcomes through **feature importance** and **actual vs. predicted rate** graphs.

---

## **Data Source**

The data used in this project is sourced from the following Kaggle dataset:

- **COVID-19 Daily Updates by Willian Oliveira**: A comprehensive dataset containing daily updated statistics on COVID-19 infections, recoveries, and deaths globally.  
  [Dataset Link](https://www.kaggle.com/datasets/willianoliveiragibin/covid-19-daily-updates?select=owid_covid_codebook.csv)  
- This dataset is used as it contains all the required aspects for the project, including data on **cases**, **deaths**, **vaccinations**, **population**, and other relevant demographic and economic factors.
- These features were used to calculate the **infection rate** and **vaccination rate**, which were then predicted using machine learning models.

---

### **Key Calculations**  

To derive the **infection rate** and **vaccination rate**, the following formulas were used:

- **Infection Rate** =  
  ```math
  \text{Infection Rate} = \left( \frac{\text{New Cases}}{\text{Population}} \right) \times 100
  
- **Vaccination Rate** =  
  ```math
  \text{Vaccination Rate} = \left( \frac{\text{New Vaccinations}}{\text{Population}} \right) \times 100

These rates were then used as the target variables for the prediction models.

---

## **Thought Process**

1. **Understanding the Problem:**
   - The rapid evolution of **COVID-19** necessitates effective forecasting models to guide healthcare interventions and policy decisions.
   - By concentrating on **North America**, this project aimed to create a manageable and actionable dataset.

2. **Data Collection and Preprocessing:**
   - Handling **missing values** and data inconsistencies was crucial for ensuring model reliability.
   - **Imputation** using **Random Forest Regression** provided more robust estimates compared to simpler imputation techniques.

3. **Exploratory Data Analysis (EDA):**
   - **EDA** was used to uncover trends and validate assumptions.
   - **Tableau dashboard** was utilized to visualize infection and vaccination trends using **GeoMaps** and **bar charts**.
   - **Correlation analysis** was applied to identify key features influencing **infection** and **vaccination rates**.  
     - Features with **correlation > 0.005** were selected for infection rate prediction.  
     - Features with **correlation > 0.05** were chosen for vaccination rate prediction.
   - **Recursive Feature Elimination (RFE)** was used to finalize **10 key features** per target, ensuring only the most relevant predictors were used for modeling.

4. **Model Selection:**
   - **Random Forest Regression** is ideal for healthcare applications as it handles complex, non-linear relationships, interprets time series data effectively, and provides clear insights into factors influencing predictions, making it a robust tool for forecasting patient outcomes and treatment effectiveness.

---

## **Challenges Faced**

- **Data Quality & Missing Values:**  
  Significant **missing data** required advanced imputation methods, which were computationally intensive but necessary for accuracy.

- **Feature Selection:**  
  Identifying the most relevant **features** from a high-dimensional dataset was challenging. A combination of **correlation analysis** and **RFE** helped streamline the process.

- **Complexity of the Data:**  
  Variations in reporting standards and **outliers** introduced noise, complicating model training and validation.

- **Model Overfitting:**  
  Fine-tuning **hyperparameters** was essential to ensure the model generalized well across unseen data.

- **Computational Limitations with Data:**  
  The dataset's large volume and complexity, including various features like **hospitalization rates**, posed challenges due to limited computational resources.
  This restricted the analysis to key features such as **infection** and **vaccination rates**.

---

## **Results Interpretation**

### **Infection Rate Prediction Model**

- **Performance Metrics:**
  - **MAE:** 0.0037  
  - **MSE:** 0.00196  
  - **RMSE:** 0.0443  
  - **R² Score:** 0.8919

- **Interpretation:**
  - The high **R² score** indicates that 89.19% of the variance in infection rates is captured by the model.
  - Low **MAE** and **RMSE** values confirm minimal prediction errors.
 
- **Visualizations:**
  - **Actual vs. Predicted Infection Rate:**  
    ![Actual vs Predicted Infection Rate](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Actual_vs_Predicted_Infection_Rate.jpg)
  - **Infection Rate Feature Importance:**  
    ![Infection Rate Feature Importance](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Infection_Rate_Feature_Importances.jpg)

### **Vaccination Rate Prediction Model**

- **Performance Metrics:**
  - **MAE:** 0.0592  
  - **MSE:** 0.1506  
  - **RMSE:** 0.3881  
  - **R² Score:** 0.9932

- **Interpretation:**
  - An **R² score** of 0.9932 indicates near-perfect prediction capability.
  - The low error metrics reinforce the model's robustness in forecasting vaccination trends.
  
- **Visualizations:**
  - **Actual vs. Predicted Vaccination Rate:**  
    ![Actual vs Predicted Vaccination Rate](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Actual_vs_Predicted_Vaccination_Rate.jpg)
  - **Vaccination Rate Feature Importance:**  
    ![Vaccination Rate Feature Importance](https://github.com/Yuvaraj-Reddy-Sanagala/ML_Project_Assessment_covid-19/blob/main/Models/Vaccination_Rate_Feature_Importances.jpg)
    
---

## Next Steps

1. **Model Enhancement:**
   - Experiment with alternative algorithms (e.g., XGBoost, LightGBM) for potential performance improvements.
   - Explore ensemble methods to combine strengths of multiple models.
   - Incorporate time-series forecasting techniques (ARIMA, Prophet, LSTM) for predicting future waves.

2. **Data Expansion:**
   - Extend the analysis to include additional global regions for broader insights.
   - Integrate more granular data, such as governmental policy changes and mobility patterns.

3. **Validation and Calibration:**
   - Implement rigorous cross-validation and consider additional metrics like MAPE.
   - Continuously update and retrain models with new data to maintain relevance.

---

## **Deployment Considerations**

### **Scalability**
- **Cloud Integration:**  
  Deploy the model on cloud platforms like **AWS SageMaker**, **Google Cloud AI**, or **Microsoft Azure** to handle large datasets and support real-time predictions.
- **Auto-scaling:**  
  Utilize cloud-native auto-scaling features (e.g., **AWS Auto Scaling**, **Google Cloud Autoscaler**) to automatically adjust resources based on demand.
- **API Services:**  
  Package the model as a **RESTful API** using frameworks like **Flask** or **Django**, and containerize the application with **Docker** for seamless deployment.

### **Performance**
- **Low-Latency Predictions:**  
  Optimize the model to ensure low-latency predictions, suitable for real-time healthcare decision-making.
- **Serverless Computing:**  
  Consider using **AWS Lambda** or **Google Cloud Functions** to run predictions on-demand without managing servers.
- **Automated Retraining:**  
  Set up pipelines using tools like **Apache Airflow** or **Kubeflow** for periodic retraining with fresh data to maintain model accuracy.

### **Real-World Implementation**
- **Dashboard Integration:**  
  Integrate model predictions into live dashboards (e.g., **Tableau**, **Power BI**) for real-time monitoring.
- **User-Friendly Interfaces:**  
  Develop intuitive interfaces (using frameworks like **React** or **Angular**) for healthcare professionals to interact with the predictions.
- **CI/CD Pipelines:**  
  Implement CI/CD using tools like **GitHub Actions** or **AWS CodePipeline** to automate testing, deployment, and updates.

---

## **Model Justification**

### Why **Random Forest Regression**?
- **Robustness & Flexibility:**  
  Capable of handling **non-linear relationships** and **high-dimensional data** without extensive preprocessing.
- **Interpretability:**  
  Provides **feature importance** scores, offering insights into the underlying factors influencing predictions.
- **Performance:**  
  Demonstrated high accuracy in predicting both infection and vaccination rates, as evidenced by the evaluation metrics.

---

## **Conclusion**

This project demonstrates the effectiveness of machine learning in predicting **COVID-19 trends**, providing:
- Accurate forecasts of **infection** and **vaccination rates**.
- Valuable insights through **exploratory data analysis** and **feature importance**.
- A strong foundation for further enhancements and real-world applications.

Future work will focus on enhancing **model performance**, expanding the dataset to a **global scale**, and ensuring seamless **deployment** in real-world environments.
