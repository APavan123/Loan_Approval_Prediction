import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load(r"C:\Users\ganga\Desktop\python_learning\loan_model.pkl")

st.title("Loan Approval Prediction")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term", min_value=0)

credit_history = st.selectbox("Credit History", [1, 0])

property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encoding
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0

if dependents == "3+":
    dependents = 3
else:
    dependents = int(dependents)

education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

if property_area == "Urban":
    property_area = 2
elif property_area == "Semiurban":
    property_area = 1
else:
    property_area = 0

features = np.array([[gender,
                      married,
                      dependents,
                      education,
                      self_employed,
                      applicant_income,
                      coapplicant_income,
                      loan_amount,
                      loan_amount_term,
                      credit_history,
                      property_area]])

if st.button("Predict"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
        