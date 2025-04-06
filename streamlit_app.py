import streamlit as st
import numpy as np
import pandas as pd
from app.model import train_model

# Load model and feature names
model, feature_names = train_model()

st.title("🧠 Breast Cancer Predictor with Logistic Regression")
st.markdown("Predict whether a tumor is **benign or malignant** using ML.")

# Let users choose input method
input_method = st.radio("Choose input method:", ["Manual (sliders)", "Upload CSV"])

# ---------- OPTION 1: MANUAL SLIDER INPUT ----------
if input_method == "Manual (sliders)":
    st.sidebar.header("Input Features")

    # Initialize session state for the sliders if not already set
    if "sliders" not in st.session_state or st.button("🔄 Reset All"):
        st.session_state.sliders = {feature: 15.0 for feature in feature_names}

    user_input = []

    # Display sliders using session state
    for feature in feature_names:
        val = st.sidebar.slider(
            label=feature,
            min_value=0.0,
            max_value=30.0,
            value=st.session_state.sliders[feature],
            key=feature
        )
        user_input.append(val)
        st.session_state.sliders[feature] = val  # Update session state

    input_data = np.array(user_input).reshape(1, -1)

    if st.button("🩺 Predict"):
        prediction = model.predict(input_data)[0]
        result = "Benign 😌" if prediction == 1 else "Malignant 😟"
        st.subheader(f"Prediction: {result}")


# ---------- OPTION 2: CSV FILE UPLOAD ----------
else:
    st.info("Upload a CSV file with the following columns:")
    st.code(", ".join(feature_names))

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            # Check if columns match
            missing_cols = set(feature_names) - set(df.columns)
            if missing_cols:
                st.error(f"❌ Missing columns: {', '.join(missing_cols)}")
            else:
                st.success("✅ File loaded successfully!")

                # Make predictions
                predictions = model.predict(df[feature_names])
                df["Prediction"] = ["Benign 😌" if p == 1 else "Malignant 😟" for p in predictions]

                st.subheader("Prediction Results")
                st.dataframe(df)

                # Let users download the results
                csv_result = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📥 Download predictions as CSV",
                    data=csv_result,
                    file_name="prediction_results.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"Error: {str(e)}")
