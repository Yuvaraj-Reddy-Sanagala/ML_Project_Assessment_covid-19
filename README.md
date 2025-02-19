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
- This dataset is used as it contains all the required aspects for the project, including data on **total cases**, **deaths**, **vaccinations**, **population**, and other relevant demographic and economic factors.
- These features were used to calculate the **infection rate** and **vaccination rate**, which were then predicted using machine learning models.

---

### **Key Calculations**  

To derive the **infection rate** and **vaccination rate**, the following formulas were used:

- **Infection Rate** =  
  \[
  \left( \frac{\text{New Cases}}{\text{Population}} \right) \times 100
  \]
  
- **Vaccination Rate** =  
  \[
  \left( \frac{\text{New Vaccinations}}{\text{Population}} \right) \times 100
  \]

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
   - **Tableau dashboards** were utilized to visualize infection and vaccination trends using **GeoMaps** and **bar charts**.
   - **Correlation analysis** was applied to identify key features influencing **infection** and **vaccination rates**.  
     - Features with **correlation > 0.005** were selected for infection rate prediction.  
     - Features with **correlation > 0.05** were chosen for vaccination rate prediction.
   - **Recursive Feature Elimination (RFE)** was used to finalize **10 key features** per target, ensuring only the most relevant predictors were used for modeling.

4. **Model Selection:**
   - **Random Forest Regression** was chosen for its robustness, interpretability, and ability to handle complex, non-linear relationships.

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
  
---

## **Next Steps**

1. **Model Enhancement:**
   - Experiment with alternative **algorithms** (e.g., **XGBoost**, **LightGBM**) for potential performance improvements.
   - Explore **ensemble methods** to combine strengths of multiple models.
   - Incorporate **time-series forecasting** techniques (**ARIMA**, **Prophet**, **LSTM**) for predicting future waves.

---

## **Deployment Considerations**

### **Scalability**
- **Cloud Integration:**  
  Deploy models on **cloud platforms** (**AWS SageMaker**, **Google Cloud AI**) to handle larger datasets and real-time prediction requests.
- **API Services:**  
  Package models into **RESTful APIs** (using **Flask/Django** with **Docker**) for seamless integration into existing systems.

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
