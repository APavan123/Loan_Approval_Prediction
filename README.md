# 🏦 Loan Approval Prediction using Machine Learning

## 📌 Project Overview

The Loan Approval Prediction project uses Machine Learning classification algorithms to predict whether a loan application will be approved or rejected based on applicant information.

The project involves data preprocessing, Exploratory Data Analysis (EDA), feature engineering, model training, hyperparameter tuning, and model evaluation.

Two classification algorithms, K-Nearest Neighbors (KNN) and Gaussian Naive Bayes, are implemented and compared to identify the best-performing model.

## 🎯 Objectives

- Analyze loan applicant information.
- Perform data cleaning and preprocessing.
- Handle missing values in numerical and categorical features.
- Perform Exploratory Data Analysis (EDA).
- Create meaningful features using feature engineering.
- Build classification models using KNN and Naive Bayes.
- Optimize model performance using GridSearchCV.
- Evaluate models using classification metrics.
- Save the best-performing model pipeline.
- Deploy the prediction model using Streamlit.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Manipulation |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| Joblib | Model Serialization |
| Streamlit | Web Application Deployment |

## 📂 Dataset Description

**Dataset:** Loan Approval Dataset (`loan_approval_dataset.csv`)

The dataset contains applicant details and loan-related information.

Important features include:

- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area
- Loan_Status (Target Variable)

**Target Variable:**

- Y – Loan Approved
- N – Loan Rejected

## 🔍 Project Workflow

### 1. Data Collection
Loaded the loan approval dataset using Pandas.

### 2. Exploratory Data Analysis (EDA)

Performed:
- Dataset shape and information analysis.
- Statistical summary.
- Missing value detection.
- Target variable distribution.
- Univariate analysis.
- Bivariate analysis.
- Correlation analysis.

### 3. Data Preprocessing

Handled missing values using:

- Mode imputation for categorical features.
- Median imputation for numerical features.

### 4. Feature Engineering

Created additional features:

- **TotalIncome:** ApplicantIncome + CoapplicantIncome
- **EMI:** Estimated monthly loan payment using LoanAmount.
- **Income_Per_Person:** Total income divided by the number of dependents plus one.

Converted the Dependents column into numerical format and removed Loan_ID.

### 5. Train-Test Split

Split the dataset into:

- Training Data: 80%
- Testing Data: 20%

Used stratified sampling to maintain target class distribution.

### 6. Data Preprocessing Pipeline

Implemented Scikit-learn pipelines using:

- SimpleImputer
- StandardScaler
- OneHotEncoder
- ColumnTransformer

### 7. Model Building

Implemented two classification algorithms:

**K-Nearest Neighbors (KNN)**
- Classifies loan applications based on nearby data points.
- Uses distance-based classification.

**Gaussian Naive Bayes**
- Uses probability and Bayes' theorem.
- Predicts loan approval based on applicant features.

### 8. Hyperparameter Tuning

Used GridSearchCV with 5-fold cross-validation.

**KNN Parameters:**
- n_neighbors
- weights
- metric

**Naive Bayes Parameter:**
- var_smoothing

### 9. Model Evaluation

Evaluated models using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- ROC-AUC Score

Selected the best-performing model based on test accuracy.

### 10. Model Saving

Saved the complete preprocessing and prediction pipeline using Joblib.

File: `loan_pipeline.pkl`

### 11. Deployment

Used Streamlit to develop an interactive Loan Approval Prediction web application.

## 📁 Project Structure

```text
Loan_Approval_Prediction/
│
├── dataset/
│   └── loan_approval_dataset.csv
│
├── app.py
├── train.py
├── loan_pipeline.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### Step 1: Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to Project

```bash
cd Loan_Approval_Prediction
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Train the Model

```bash
python train.py
```

### Step 7: Run Streamlit Application

```bash
streamlit run app.py
```

## 📊 Model Evaluation

The project compares KNN and Gaussian Naive Bayes using multiple evaluation metrics.

| Evaluation Metric | Purpose |
|---|---|
| Accuracy | Measures overall correct predictions |
| Precision | Measures correctness of positive predictions |
| Recall | Measures how many actual positive cases are identified |
| F1-Score | Balances precision and recall |
| Confusion Matrix | Shows correct and incorrect predictions |
| ROC-AUC | Measures classification performance across thresholds |

*Actual model scores will be added after running the training code.*

## 🚀 Future Improvements

- Experiment with Logistic Regression, Decision Tree, and Random Forest.
- Improve model performance through feature selection.
- Add more advanced visualizations.
- Improve the Streamlit user interface.
- Deploy the application online.
- Add explainable AI techniques to understand prediction results.

## 👨‍💻 Author

**Pavan Amundla**

Aspiring AI/ML Engineer

Skills: Python | Machine Learning | Pandas | NumPy | Scikit-learn | SQL | Streamlit

---
