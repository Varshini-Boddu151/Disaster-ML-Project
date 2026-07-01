import streamlit as st
import pandas as pd
import joblib

# -------------------------------------------------------------------
# Load the saved pipeline (preprocessing + model combined)
# -------------------------------------------------------------------
model_pipeline = joblib.load("disaster_pipeline.pkl")

st.title("Disaster Severity Prediction")
st.write("Enter the disaster event details below to predict if it is a Major Disaster.")

# -------------------------------------------------------------------
# User Inputs (must match the exact column names used in training)
# -------------------------------------------------------------------
disaster_type = st.selectbox(
    "Disaster Type",
    ['Wildfire', 'Hurricane', 'Volcanic Eruption', 'Drought',
     'Landslide', 'Earthquake', 'Flood']
)

location = st.selectbox(
    "Location",
    ['Chile', 'India', 'Italy', 'Turkey', 'Indonesia', 'Japan', 'USA', 'Philippines']
)

aid_provided = st.selectbox("Aid Provided", ['Yes', 'No'])

latitude = st.number_input("Latitude", value=0.0, format="%.4f")
longitude = st.number_input("Longitude", value=0.0, format="%.4f")

severity_level = st.slider("Severity Level", min_value=1, max_value=10, value=5)

affected_population = st.number_input("Affected Population", min_value=0, value=1000)

estimated_economic_loss_usd = st.number_input(
    "Estimated Economic Loss (USD)", min_value=0.0, value=100000.0
)

response_time_hours = st.number_input("Response Time (hours)", min_value=0.0, value=24.0)

infrastructure_damage_index = st.slider(
    "Infrastructure Damage Index", min_value=0.0, max_value=10.0, value=5.0
)

# -------------------------------------------------------------------
# Predict button
# -------------------------------------------------------------------
if st.button("Predict"):

    input_df = pd.DataFrame([{
        "disaster_type": disaster_type,
        "location": location,
        "latitude": latitude,
        "longitude": longitude,
        "severity_level": severity_level,
        "affected_population": affected_population,
        "estimated_economic_loss_usd": estimated_economic_loss_usd,
        "response_time_hours": response_time_hours,
        "aid_provided": aid_provided,
        "infrastructure_damage_index": infrastructure_damage_index
    }])

    prediction = model_pipeline.predict(input_df)[0]

    if prediction == 1:
        st.error("Prediction: MAJOR DISASTER")
    else:
        st.success("Prediction: NOT a Major Disaster")