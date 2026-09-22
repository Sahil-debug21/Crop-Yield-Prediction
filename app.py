import streamlit as st
import pandas as pd
import pickle
from pathlib import Path


# Load model
model_path = Path(__file__).resolve().parent / "results" / "model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)


# Title
st.title("🌾 Crop Yield Prediction")
st.write("Enter the details below to predict crop yield.")


# User inputs

crop = st.selectbox("Crop",["Maize", "Wheat", "Rice", "Barley"])
soil_type = st.selectbox("Soil Type",["Sandy", "Clay", "Loamy", "Black"])
soil_ph = st.number_input("Soil pH",min_value=0.0,max_value=14.0,value=7.0)
rainfall = st.number_input("Rainfall (mm)",min_value=0.0,value=1000.0)
temperature = st.number_input(
    "Temperature (°C)",
    min_value=-50.0,
    max_value=60.0,
    value=25.0
)
humidity = st.number_input("Humidity (%)",min_value=0.0,max_value=100.0,value=60.0)
fertilizer = st.number_input("Fertilizer Used (kg)",min_value=0.0,value=100.0)
irrigation = st.selectbox("Irrigation",["Yes", "No"])
pesticides = st.number_input("Pesticides Used (kg)",min_value=0.0,value=10.0)
planting_density = st.number_input("Planting Density",min_value=0.0,value=20.0)


# Prediction

if st.button("Predict Yield"):

    input_data = pd.DataFrame({
        "Crop": [crop],
        "Soil_Type": [soil_type],
        "Soil_pH": [soil_ph],
        "Rainfall_mm": [rainfall],
        "Temperature_C": [temperature],
        "Humidity_pct": [humidity],
        "Fertilizer_Used_kg": [fertilizer],
        "Irrigation": [irrigation],
        "Pesticides_Used_kg": [pesticides],
        "Planting_Density": [planting_density]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Crop Yield: {prediction[0]:.2f} ton/ha"
    )


