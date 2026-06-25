# 💳 Credit Risk Default Prediction using Machine Learning

> Predicting loan default risk using Machine Learning to help financial institutions identify high-risk customers and make informed lending decisions.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![Model](https://img.shields.io/badge/Model-Logistic%20Regression-orange)
![ROC-AUC](https://img.shields.io/badge/ROC--AUC-98%25-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📖 Project Overview

Credit risk modelling is one of the most critical applications of Machine Learning in the banking and finance industry. Lenders need reliable tools to assess whether a customer is likely to default before approving a loan.

In this project, I built an **end-to-end Credit Risk Prediction system** for **Lauki Finance** that predicts whether a customer is likely to default on a loan based on customer demographics, loan details, and bureau information.

**The project covers:**

- Data Cleaning & Preprocessing
- Feature Engineering
- Handling Imbalanced Data (SMOTE & Undersampling)
- Feature Selection (IV, VIF, Domain Knowledge)
- Model Training & Hyperparameter Tuning
- Model Evaluation using Banking-Grade Metrics
- Streamlit Web Application Deployment

---

## 📸 Application Screenshots

### Home Page
![Home Page](screenshots/home_page.png)

### Prediction Result
![Prediction Result](screenshots/prediction_result.png)

---

## 🚀 Tech Stack

| Category | Technologies |
|---|---|
| Language | Python 3.10 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-Learn, XGBoost |
| Imbalanced Data | SMOTE, UnderSampling (imbalanced-learn) |
| Hyperparameter Tuning | RandomizedSearchCV, Optuna |
| Model Evaluation | ROC-AUC, Gini, KS Statistic, Rank Ordering |
| Deployment | Streamlit |
| Model Serialization | Joblib |

---

## 📂 Dataset

The dataset contains three categories of information:

- **Customer Details** — Demographics and personal information
- **Loan Information** — Loan amount, tenure, type, purpose
- **Credit Bureau Information** — Past credit behaviour, delinquency history

**Target Variable:** `Default`
- `1` → Customer Defaulted
- `0` → Customer Did Not Default

---

## ⚙️ Project Workflow

| Stage | Description |
|---|---|
| 📂 Dataset | Customer, Loan, and Bureau data with `Default` as the target variable |
| 🧹 Data Preprocessing | Missing value treatment, invalid value handling, feature engineering, Min-Max scaling |
| 🔍 Feature Selection | Information Value (IV), VIF analysis, and domain knowledge |
| ✂️ Train-Test Split | 75% Training — 25% Testing |
| 🤖 Model Training | Logistic Regression, Random Forest, XGBoost with SMOTE and Undersampling |
| ⚙️ Hyperparameter Tuning | RandomizedSearchCV and Optuna |
| 📊 Model Evaluation | ROC-AUC, KS Statistic, Gini Coefficient, Rank Ordering, Classification Report |
| 🚀 Deployment | Streamlit Web Application |

---

## 🤖 Machine Learning Models Compared

| Model | AUC | Gini |
|---|---|---|
| Logistic Regression ✅ *(Final Model)* | 98% | 96% |
| XGBoost | 99% | 96% |
| Random Forest | 97% | 95% |

> **Logistic Regression** was selected as the final model for its excellent performance, interpretability, and suitability for credit risk use cases where model explainability is critical.

---

## 📈 Final Model Performance

| Metric | Score |
|---|---|
| ROC-AUC Score | **98%** |
| Gini Coefficient | **96%** |
| Top 3 Decile Capture Rate | **99.53%** |

---

## 🎯 Key Insights

- ✅ Excellent discrimination between defaulters and non-defaulters
- ✅ Strong rank ordering capability — high-risk customers consistently scored higher
- ✅ High KS Statistic indicating effective separation of risky and safe customers
- ✅ Top 3 decile captures **99.53%** of all defaulters — highly actionable for lending decisions
- ✅ Logistic Regression chosen for interpretability, which is essential in regulated financial environments

---

## 💻 Installation

**Clone the repository**

```bash
git clone https://github.com/Likhitha1234-lab/ml-project-credit-risk-model.git
cd ml-project-credit-risk-model
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Run the Streamlit application**

```bash
streamlit run main.py
```

---

## 📁 Project Structure

```
ml-project-credit-risk-model/
│
├── artifacts/               # Saved models and encoders
├── screenshots/             # App screenshots
├── main.py                  # Streamlit application
├── prediction_helper.py     # Prediction logic and preprocessing
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 👩‍💻 Author

**Likhitha N** — Aspiring AI & Data Scientist

Skills: Python · Machine Learning · Statistics · SQL · Streamlit · Logistic Regression · XGBoost

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/likhitha-n-79b1152b7)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com/Likhitha1234-lab)

---

⭐ *If you found this project useful, consider giving it a star!*