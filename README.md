# 🌾 Crop Yield Prediction

## 📌 Problem Statement

Crop yield is influenced by various factors such as soil conditions, weather, irrigation, fertilizer usage, pesticides, and planting density. Estimating crop yield using these factors can help understand how agricultural conditions affect production.

The objective of this project is to build a **Machine Learning regression model** that predicts crop yield in **tons per hectare (ton/ha)** based on agricultural, environmental, and soil-related features.

---

## 🎯 Project Overview

This is an end-to-end **Machine Learning regression project** developed to predict crop yield.

The project includes:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Numerical and categorical feature handling
* Missing-value imputation
* Feature scaling using `StandardScaler`
* Categorical encoding using `OneHotEncoder`
* Feature preprocessing using `ColumnTransformer`
* Multiple regression model training
* Model comparison
* Hyperparameter tuning using `GridSearchCV`
* Model evaluation using **R² Score and RMSE**
* Building an integrated Scikit-learn pipeline
* Saving the trained model using Pickle
* Developing an interactive **Streamlit web application** for predictions

---

## 📊 Dataset

The dataset contains **10,000 records and 13 columns**.

### Features

* Crop
* Region
* Soil Type
* Soil pH
* Rainfall
* Temperature
* Humidity
* Fertilizer Used
* Irrigation
* Pesticides Used
* Planting Density
* Previous Crop

### Target

`Yield_ton_per_ha`

---

## 🤖 Models Used

The following regression algorithms were trained and evaluated:

* Linear Regression
* K-Nearest Neighbors Regressor
* Decision Tree Regressor
* Random Forest Regressor
* Support Vector Regressor

**GridSearchCV** was used for hyperparameter tuning.

---

## 📈 Model Performance

The tuned models achieved approximately:

* **R² Score:** 0.9804
* **RMSE:** 5.32

The tuned Linear Regression and Random Forest models produced approximately the same performance in the experiments.

---

## 🌐 Streamlit Application

A Streamlit application was developed where users can enter crop and agricultural parameters and receive a predicted crop yield.

The trained preprocessing and model pipeline is saved as:

```text
model.pkl
```

The application loads this saved pipeline and generates predictions for new input data.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Pickle

---

## 🚀 Key Highlights

* End-to-end Machine Learning regression workflow
* 10,000+ records
* Multiple regression algorithms compared
* Hyperparameter tuning with GridSearchCV
* R² of approximately **0.98**
* Complete preprocessing + model pipeline
* Interactive Streamlit deployment
