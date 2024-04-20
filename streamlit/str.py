import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("E:\MLP\Diabetes\Model\diabetes dataset.csv")  
x = data.iloc[:,:-1]
y = data.iloc[:, -1]
# Train the model
model=DecisionTreeClassifier()
model.fit(x, y)
# Function to predict EMISSION using the loaded model
def predict(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    features = np.asarray([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    features = features.reshape(1,-1)
    emission = model.predict(features)
    if emission==1:
        return "Having diabetes"
    else:
        return "Not Having diabetes"

# Streamlit UI
st.title('DIABETES PREDICTION')
st.write("ENTER INPUTS:")

#'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#'BMI', 'DiabetesPedigreeFunction', 'Age'

# Input fields for user
Pregnancies = st.number_input('Pregnancies')
Glucose = st.number_input('Glucose')
BloodPressure = st.number_input('BloodPressure')
SkinThickness = st.number_input('SkinThickness')
Insulin = st.number_input('Insulin')
BMI = st.number_input('BMI')
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')
Age = st.number_input('Age')

# Prediction button
if st.button('Predict'):
    # Predict EMISSION
    prediction = predict(Pregnancies,Glucose,BloodPressure,SkinThickness,BMI ,Insulin,DiabetesPedigreeFunction,Age)
    st.write(f"PREDICTION: {prediction}")