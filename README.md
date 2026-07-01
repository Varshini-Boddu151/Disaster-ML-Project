# 🌪️ Disaster Severity Prediction using Machine Learning

A Machine Learning project that predicts whether a disaster event is likely to be a **Major Disaster** based on disaster characteristics such as disaster type, location, severity, affected population, economic loss, response time, and infrastructure damage.

The project includes data preprocessing, model comparison, pipeline creation, and deployment using **Streamlit**.

🔗 **Live Demo:** https://disaster-ml-project-efwbuahbb4sdhtwbtu6owd.streamlit.app/

---

## 🧭 Project Overview

Natural disasters cause significant damage to lives and infrastructure. Predicting whether a disaster is likely to become a major disaster can help authorities plan resources and improve emergency response.

This project uses Machine Learning classification algorithms to predict disaster severity.

---

## ✨ Features

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Multiple ML model training
- Model comparison
- Hyperparameter tuning
- Scikit-learn Pipeline
- Streamlit Web Application
- Saved model using Joblib

---

## 🗃️ Project Structure

```
Disaster-Severity-Prediction/
│
├── Disaster_ML_Project.ipynb      # Model training notebook
├── app.py                         # Streamlit application
├── disaster_pipeline.pkl          # Saved ML pipeline
├── requirements.txt               # Required packages
└── README.md
```

---

## 🧾 Input Features

The model uses the following inputs:

- Disaster Type
- Location
- Latitude
- Longitude
- Severity Level
- Affected Population
- Estimated Economic Loss (USD)
- Response Time (Hours)
- Aid Provided
- Infrastructure Damage Index

---

## 🎯 Target Variable

**is_major_disaster**

- **0 → Not a Major Disaster**
- **1 → Major Disaster**

---

## 🧠 Machine Learning Models Used

The following classification algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- Gaussian Naive Bayes

The models were compared using classification metrics, and the best-performing model was selected for deployment.

---

## 🔧 Data Preprocessing

The preprocessing pipeline includes:

- One-Hot Encoding for categorical features
- Standard Scaling for numerical features
- ColumnTransformer
- Scikit-learn Pipeline

Using a pipeline ensures that the same preprocessing steps are applied during both training and prediction.

---

## 📊 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

Training and testing accuracy were also compared to identify overfitting and underfitting.

---

## 🖥️ Streamlit Application

The Streamlit app allows users to enter disaster information and instantly predict whether the disaster is classified as a **Major Disaster**.

### User Inputs

- Disaster Type
- Location
- Latitude
- Longitude
- Severity Level
- Affected Population
- Estimated Economic Loss
- Response Time
- Aid Provided
- Infrastructure Damage Index

### Prediction Output

- ✅ Not a Major Disaster
- 🚨 Major Disaster

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 🔁 Application Workflow

1. Enter disaster details.
2. Click **Predict**.
3. The model processes the inputs.
4. The application predicts whether the disaster is a **Major Disaster**.

---

## 👤 Author

**Varshini Boddu**

Machine Learning Enthusiast



---

## ⭐ If you found this project useful, don't forget to star the repository!
