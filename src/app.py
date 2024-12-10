'''Simple Streamlit web app.'''
import pickle
import pandas as pd
import streamlit as st

# Load the model
model_file='../models/model.pkl'

with open(model_file, 'rb') as input_file:
    model=pickle.load(input_file)

# Dictionary to translate numerical predictions into
# human readable strings
class_dict={
    '0': 'Not diabetic',
    '1': 'Diabetic'
}

# Page title
st.title('Diabetes prediction')

val1 = st.slider("Glucose", min_value = 0.0, max_value = 199.0, step = 0.1)
val2 = st.slider("Insulin", min_value = 0.0, max_value = 846.0, step = 0.1)
val3 = st.slider("BMI", min_value = 0.0, max_value = 67.1, step = 0.1)
val4 = st.slider("Age", min_value = 21.0, max_value = 81.0, step = 0.1)



# When the user clicks 'Predict'
if st.button('Predict'):

        

    # Display the prediction to the user
    prediction = str(model.predict([[val1, val2, val3, val4]])[0])
    predicted_class = class_dict[prediction]
    st.write('Prediction:', predicted_class)
