import streamlit as st
import requests
import json

# ---------------------------------------------------------
# CONFIGURE THE APP
# ---------------------------------------------------------
st.set_page_config(page_title="Nutri-Grade AI", page_icon="🍔")


API_URL = "https://nutri-grade-mlops.onrender.com/predict"


st.sidebar.header("📝 Enter Nutrition Details")

total_fat = st.sidebar.slider("Total Fat (g)", 0, 100, 20)
carbs = st.sidebar.slider("Carbohydrates (g)", 0, 100, 45)
protein = st.sidebar.slider("Protein (g)", 0, 100, 25)
sugar = st.sidebar.slider("Sugar (g)", 0, 100, 10)

# ---------------------------------------------------------
# MAIN PAGE: RESULTS
# ---------------------------------------------------------
st.title("🍔 Nutri-Grade AI Predictor")
st.markdown("Adjust the sliders on the left to estimate the calorie count of your food.")

if st.button("Predict Calories"):
    # 1. Prepare the payload for the API
    payload = {
        "total_fat": total_fat,
        "carbs": carbs,
        "protein": protein,
        "sugar": sugar
    }

    # 2. Send request to the API
    try:
        with st.spinner("Asking the AI..."):
            response = requests.post(API_URL, json=payload)
        
        # 3. Handle response
        if response.status_code == 200:
            result = response.json()
            calories = result["predicted_calories"]
            
            st.success("Prediction Complete!")
            st.metric(label="Estimated Calories", value=f"{calories:.0f} kcal")
            
            # Fun conditional feedback
            if calories > 500:
                st.warning("⚠️ That's a heavy meal!")
            else:
                st.balloons()
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)
            
    except Exception as e:
        st.error(f"Connection Error: {e}")