import streamlit as st
import pandas as pd
import pickle


st.title("Expenses Prediction App")

with open('pipe.pkl', 'rb') as f:
    model = pickle.load(f)

age = st.number_input("Age", min_value=18, max_value=100, step=1)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
children_expense = st.selectbox("Children Expense",
                                ['lower expenses', 'high expenses', 'medium expenses'])  
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"])

input_df = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'smoker': [smoker],
    'region': [region],
    'children_expense': [children_expense]})


if st.button("Predict Expense"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Insurance Expense: ${prediction[0]:.2f}")