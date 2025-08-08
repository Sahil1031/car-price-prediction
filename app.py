import streamlit as st
import joblib
import numpy as np
import pandas as pd


model = joblib.load('car_price_model.pkl')

st.title("Car Price Prediction App")


st.sidebar.header("Input Car Details")

def user_input():
    year = st.sidebar.number_input('Year of Purchase', min_value=1990, max_value=2025, step=1, value=2015)
    km_driven = st.sidebar.number_input('Kilometers Driven', value=50000)
    mileage = st.sidebar.number_input('Mileage (km/l or km/kg)', value=18.0)
    engine = st.sidebar.number_input('Engine Capacity (CC)', value=1200)
    max_power = st.sidebar.number_input('Max Power (bhp)', value=80.0)
    seats = st.sidebar.selectbox('Number of Seats', [2, 4, 5, 6, 7, 8])

    fuel = st.sidebar.selectbox('Fuel Type', ['Petrol', 'Diesel', 'LPG'])
    seller_type = st.sidebar.selectbox('Seller Type', ['Individual', 'Trustmark Dealer'])
    transmission = st.sidebar.selectbox('Transmission', ['Manual', 'Automatic'])
    owner = st.sidebar.selectbox('Owner', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])

    # Manual encoding
    fuel_Petrol = 1 if fuel == 'Petrol' else 0
    fuel_Diesel = 1 if fuel == 'Diesel' else 0
    fuel_LPG = 1 if fuel == 'LPG' else 0

    seller_Individual = 1 if seller_type == 'Individual' else 0
    seller_Trustmark = 1 if seller_type == 'Trustmark Dealer' else 0

    transmission_Manual = 1 if transmission == 'Manual' else 0

    owner_Second = 1 if owner == 'Second Owner' else 0
    owner_Third = 1 if owner == 'Third Owner' else 0
    owner_Fourth_Above = 1 if owner == 'Fourth & Above Owner' else 0
    owner_Test_Drive = 1 if owner == 'Test Drive Car' else 0

    # Construct final feature array
    features = np.array([[
        year, km_driven, mileage, engine, max_power, seats,
        fuel_Diesel, fuel_LPG, fuel_Petrol,
        seller_Individual, seller_Trustmark,
        transmission_Manual,
        owner_Fourth_Above, owner_Second, owner_Test_Drive, owner_Third
    ]])

    return features

# Get user input
input_data = user_input()

# Prediction
if st.button('Predict Car Price'):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Car Price: ₹{round(prediction, 2):,}")
