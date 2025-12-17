import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("models/best_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="centered")
st.title("🏠 House Price Prediction App")
st.subheader("Enter House Features:")

# Input fields
area = st.number_input("Area (sqft)", min_value=100, max_value=10000, value=1000, step=50)
bedrooms = st.slider("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.slider("Bathrooms", min_value=1, max_value=10, value=2)
stories = st.slider("Number of Stories", min_value=1, max_value=5, value=1)
parking = st.slider("Parking Spots", min_value=0, max_value=5, value=1)

# Binary features
mainroad = st.selectbox("Main Road Access", ["No", "Yes"])
basement = st.selectbox("Basement", ["No", "Yes"])
guestroom = st.selectbox("Guestroom", ["No", "Yes"])
hot_water_heating = st.selectbox("Hot Water Heating", ["No", "Yes"])
prefarea = st.selectbox("Preferred Area", ["No", "Yes"])

# Furnishing status
furnishing_status = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])

# Convert categorical to numerical
mainroad_val = 1 if mainroad == "Yes" else 0
basement_val = 1 if basement == "Yes" else 0
guestroom_val = 1 if guestroom == "Yes" else 0
hot_water_heating_val = 1 if hot_water_heating == "Yes" else 0
prefarea_val = 1 if prefarea == "Yes" else 0
airconditioning = st.selectbox("Air Conditioning", ["No", "Yes"])
airconditioning_val = 1 if airconditioning == "Yes" else 0
# Furnishing status encoding (one-hot)
furnishing_unfurnished = 1 if furnishing_status == "Unfurnished" else 0
furnishing_semi = 1 if furnishing_status == "Semi-Furnished" else 0
# furnishing_furnished column is optional if you used only 2 one-hot columns in training
# so we skip it here if your training had 2 columns
# furnishing_furnished = 1 if furnishing_status == "Furnished" else 0

# Predict button
if st.button("Predict Price"):
    # Combine features in the same order as your training data
    features = np.array([[ 
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad_val,
        guestroom_val,
        basement_val,
        hot_water_heating_val,
        airconditioning_val,  
        parking,
        prefarea_val,
        furnishing_semi,
        furnishing_unfurnished
    ]])
    
    # Scale features
    features_scaled = scaler.transform(features)
    
    # Predict
    price = model.predict(features_scaled)[0]
    st.success(f"💰 Estimated House Price: ₹{price:,.0f}")
