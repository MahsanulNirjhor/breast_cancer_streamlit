import streamlit as st
import numpy as np
from model import train_model

# Load model
model, feature_names = train_model()

st.title("🧠 Breast Cancer Predictor (Logistic Regression)")
st.markdown("Predict whether a tumor is **benign or malignant** using ML.")

st.sidebar.header("Input Features")

# Create inputs dynamically for all features
user_input = []
for feature in feature_names:
    val = st.sidebar.slider(f"{feature}", 0.0, 30.0, 15.0)
    user_input.append(val)

# Convert to numpy array
input_data = np.array(user_input).reshape(1, -1)

# Predict on button click
if st.button("🩺 Predict"):
    prediction = model.predict(input_data)[0]
    result = "Benign 😌" if prediction == 1 else "Malignant 😟"
    st.subheader(f"Prediction: {result}")
