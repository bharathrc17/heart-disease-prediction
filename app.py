import streamlit as st
import numpy as np
import joblib

# Load the pre-trained model
model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('heart_disease_scaler.pkl')

#title of the app
st.title('Heart Disease Prediction App')
# Input fields for user data
age = st.slider('Age', min_value=0, max_value=120, value=30)
sex = st.selectbox('Sex', options=[0,1], format_func=lambda x:'Female' if x == 0 else 'Male')
cp = st.selectbox('Chest Pain Type', options=[0,1,2,3], format_func=lambda x: f'Type {x}')
trestbps = st.slider('Resting Blood Pressure (mm Hg)', min_value=80, max_value=200, value=120)
chol = st.slider('Serum Cholesterol (mg/dl)', min_value=100, max_value=600, value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
restecg = st.selectbox('Resting Electrocardiographic Results', options=[0,1,2], format_func=lambda x: f'Result {x}')
thalach = st.slider('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
exang = st.selectbox('Exercise Induced Angina', options=[0,1], format_func=lambda x: 'No' if x == 0 else 'Yes')
oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=6.0, value=1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0,1,2], format_func=lambda x: f'Slope {x}')
ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', options=[0,1,2,3], format_func=lambda x: f'Vessel {x}')
thal = st.selectbox('Thalassemia', options=[0,1,2,3], format_func=lambda x: f'Thal {x}')

# Button to trigger prediction
if st.button('Predict'):
    # Prepare the input data
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    input_data_scaled = scaler.transform(input_data)
    # Make prediction
    prediction = model.predict(input_data_scaled)
    # Display the result
    if prediction[0] == 1:
        st.success('The model predicts that you have heart disease.')
    else:
        st.success('The model predicts that you do not have heart disease.')
        
