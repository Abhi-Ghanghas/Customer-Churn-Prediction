# 📊 Customer Churn Prediction & Retention Analytics

An end-to-end Data Science and Machine Learning project that predicts whether a telecom customer is likely to churn and provides retention recommendations.
## 🌐 Live Demo

👉 [Try the Customer Churn Prediction App][(https://your-app.streamlit.app/)](https://customer-churn-prediction-abhi.streamlit.app/)

## 🎯 Business Problem

Customer churn can significantly affect revenue and customer acquisition costs.

This project identifies customers who are likely to leave so that businesses can take proactive retention actions.

## 🚀 Features

- Exploratory Data Analysis
- Data Cleaning
- SQL Analysis
- Customer Segmentation
- Logistic Regression
- Random Forest
- XGBoost
- Model Comparison
- ROC-AUC Evaluation
- SHAP Explainability
- Real-Time Churn Prediction
- Risk Classification
- Retention Recommendations
- Streamlit Web Application

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- SQL / SQLite
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- SHAP
- Streamlit
- Joblib

## 🧠 Machine Learning Workflow

Raw Data  
↓  
Data Cleaning  
↓  
Exploratory Data Analysis  
↓  
SQL Analysis  
↓  
Feature Preprocessing  
↓  
Train/Test Split  
↓  
Model Training  
↓  
Model Comparison  
↓  
Explainability  
↓  
Streamlit Deployment  

## 🤖 Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## 🏆 Best Model

**Logistic Regression**

**ROC-AUC: 0.8359**

Logistic Regression achieved the highest ROC-AUC score among the evaluated models and was selected as the final model.

## 🔍 Explainability

SHAP and Logistic Regression coefficients were used to understand which customer attributes influence churn risk.

## 💡 Business Application

The system can help retention teams:

- Identify high-risk customers
- Prioritize retention campaigns
- Recommend long-term contracts
- Target customers with personalized offers
- Detect common churn factors
- Reduce preventable customer loss

## 🌐 Streamlit Application

The application allows users to enter customer details and receive:

- Churn probability
- Risk level
- Churn prediction
- Possible risk factors
- Recommended retention actions

## 📁 Project Structure

```text
Customer Churn Prediction/
│
├── .streamlit/
│   └── config.toml
│
├── Data/
│   └── customer_churn.csv
│
├── Models/
│   ├── churn_model.pkl
│   └── feature_importance.csv
│
├── Notebooks/
│   └── churn_analysis.ipynb
│
├── app.py
├── database.py
├── customer_churn.db
├── requirements.txt
├── .gitignore
└── README.md




👨‍💻 Author

Abhi Ghanghas

B.Tech Computer Science Engineering
Aspiring Data Scientist
