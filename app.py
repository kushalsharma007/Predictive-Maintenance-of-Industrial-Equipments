import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load(r'D:\Major project\random_forest_model.pkl')


st.set_page_config(page_title="Machine Failure Predictor", layout="centered")

st.title("🔧 Machine Failure Type Predictor")

# Define input form
with st.form("prediction_form"):
    st.subheader("Enter Machine Data")

    air_temp = st.number_input("Air Temperature", min_value=0.0)
    process_temp = st.number_input("Process Temperature", min_value=0.0)
    rotational_speed = st.number_input("Rotational Speed", min_value=0)
    torque = st.number_input("Torque", min_value=0.0)
    tool_wear = st.number_input("Tool Wear", min_value=0)

    # For 'Type', you might have to map strings to what the model was trained on
    machine_type = st.selectbox("Machine Type", ['L', 'M', 'H'])  # Adjust if you encoded these differently

    submit = st.form_submit_button("Predict")

# Handle prediction
if submit:
    # Create a DataFrame for prediction
    input_data = pd.DataFrame({
        'Type': [machine_type],
        'Air temperature': [air_temp],
        'Process temperature': [process_temp],
        'Rotational speed': [rotational_speed],
        'Torque': [torque],
        'Tool wear': [tool_wear]
    })

    # If label encoding was used for 'Type', load and transform it here
    # le = joblib.load('label_encoder.pkl')
    # input_data['Type'] = le.transform(input_data['Type'])

    # Make prediction
    prediction = model.predict(input_data)

    st.success(f"🔍 Predicted Failure Type: **{prediction[0]}**")
