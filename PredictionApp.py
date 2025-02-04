#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import joblib
import numpy as np


# In[11]:


model = joblib.load('random_forest.pkl')

st.title("Appointments Prediction")

st.markdown("""
This app predicts whether a patient will Show up or Not for their medical appointment based on various factors.
""")

gender = st.radio("Gender", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
age = st.number_input("Enter Age of the Patient", min_value=0, max_value=120, step=1)
scholarship = st.radio("Is pateint receiving Scholarship", options=[0, 1])
hypertension = st.radio("Does patient have Hypertension", options=[0, 1])
diabetes = st.radio("Is patient diabetic", options=[0, 1])
alcoholism = st.radio("Alchohol comsumption", options=[0, 1])
handicap = st.radio("Handicap", options=[0, 1])
sms_received = st.radio("Received SMS Reminder", options=[0, 1])
days_difference = st.number_input("Gap between scheduled and actual appointment date", min_value=0, step=1)

user_input = np.array([[gender, age, scholarship, hypertension, diabetes, alcoholism, 
                        handicap, sms_received, days_difference]])

# Make the prediction
if st.button('Predict'):
    prediction = model.predict(user_input)[0]

    # Interpret prediction
    if prediction == 0:
        st.success("The patient is likely to Attend for the appointment.")
    else:
        st.error("The patient is likely to Miss for the appointment.")


# Convert to python script

# In[10]:

