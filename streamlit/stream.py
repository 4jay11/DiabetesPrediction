import streamlit as st
import pickle
import pandas as pd

# Load the model
model_file_path = "E:\MLP\streamlit\diabetes.pkl"
with open(model_file_path, 'rb') as file:
    model = pickle.load(file)
print("Model loaded successfully.")

# Streamlit app
st.title('Diabetes Prediction App')
st.sidebar.title('User Input')
st.sidebar.markdown('Enter the details:')
Pregnancies = st.sidebar.number_input('Pregnancies:')
Glucose = st.sidebar.number_input('Glucose:')
BloodPressure = st.sidebar.number_input('Blood Pressure:')
SkinThickness = st.sidebar.number_input('SkinThickness:')
Insulin = st.sidebar.number_input('Insulin:')
BMI = st.sidebar.number_input('BMI:')
DiabetesPedigreeFunction = st.sidebar.number_input('DiabetesPedigreeFunction:')
Age = st.sidebar.number_input('Age:')

# Create input DataFrame
input_data = {
    'Pregnancies': [Pregnancies],
    'Glucose': [Glucose],
    'BloodPressure': [BloodPressure],
    'SkinThickness': [SkinThickness],
    'Insulin': [Insulin],
    'BMI': [BMI],
    'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
    'Age': [Age]
}
input_df = pd.DataFrame(input_data)

# Make prediction
prediction = model.predict(input_df)

# Display prediction
if prediction[0] == 0:
    p = 'Having Diabetes'
else:
    p = 'Not Having Diabetes'

st.write('Prediction:', p)
