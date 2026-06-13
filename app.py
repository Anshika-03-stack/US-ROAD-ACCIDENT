
import streamlit as st
import joblib
import pandas as pd
import streamlit as st
import joblib
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
# Load models


severity_model = joblib.load("severity_model.pkl")
severity_features = joblib.load("severity_features.pkl")
hotspot_model = joblib.load("hotspot_model.pkl")
hotspot_features = joblib.load("hotspot_features.pkl")

district_coords = {
    "South, Urban Area": [29.7604, -95.3698],
    "South, Rural Area": [32.7767, -96.7970],
    "North, Urban Area": [40.7128, -74.0060],
    "North, Rural Area": [44.9778, -93.2650],
    "East, Urban Area": [39.9526, -75.1652],
    "East, Rural Area": [37.5407, -77.4360],
    "West, Urban Area": [34.0522, -118.2437],
    "West, Rural Area": [43.6150, -116.2023],
    "Midwest, Urban Area": [41.8781, -87.6298],
    "Midwest, Rural Area": [41.5868, -93.6250]
}

st.title("🚦 US Road Accident Prediction System")
st.markdown("""
### Predict • Prevent • Protect

AI-powered accident hotspot and severity analysis for proactive traffic safety.
""")

tab1, tab2,tab3,tab4= st.tabs([
    "🔥 Hotspot Prediction",
    "🚑 Severity Prediction",
      "📊 Insights",
      "🗺️ US Hotspot Map"
])

with tab1:
    st.header("Stage 1: Hotspot Prediction")
# User Inputs
    district = st.selectbox(
    "Select District/Location",
    [
        "South, Rural Area",
        "South, Urban Area",
        "North, Rural Area",
        "North, Urban Area",
        "East, Rural Area",
        "East, Urban Area",
        "West, Rural Area",
        "West, Urban Area",
        "Midwest, Rural Area",
        "Midwest, Urban Area"
    ]
)

   
    time_options = [
    "12:00 AM","1:00 AM","2:00 AM","3:00 AM","4:00 AM","5:00 AM",
    "6:00 AM","7:00 AM","8:00 AM","9:00 AM","10:00 AM","11:00 AM",
    "12:00 PM","1:00 PM","2:00 PM","3:00 PM","4:00 PM","5:00 PM",
    "6:00 PM","7:00 PM","8:00 PM","9:00 PM","10:00 PM","11:00 PM"
]
    selected_time = st.selectbox(
    "Select Time",
    time_options,
    key="hotspot_time"
)

    hour = time_options.index(selected_time)

    hotspot_result = None
    
    if st.button("Predict Hotspot Risk", key="hotspot_btn"):



      input_df = pd.DataFrame({
        "District/Location": [district],
        "Hour of Day": [hour]
    })

    

      input_encoded = pd.get_dummies(input_df)

    

      input_encoded = input_encoded.reindex(
        columns=hotspot_features,
        fill_value=0
    )

    

      prediction = hotspot_model.predict(input_encoded)[0]

    

      risk_map = {
        0: "Low Risk",
        1: "Medium Risk",
        2: "High Risk"
    }

      hotspot_result = risk_map.get(prediction, "Unknown")

      
      st.write("Risk:", hotspot_result)

    
    if hotspot_result == "High Risk":
        st.error("🔴 High Risk Area")
        st.info(f"📍 High-risk zone detected near {district}")

    elif hotspot_result == "Medium Risk":
      st.warning("🟡 Medium Risk Area")

    elif hotspot_result == "Low Risk":
      st.success("🟢 Low Risk Area")



with tab2:
    # paste ALL severity code here
    st.header("Stage 2: Severity Prediction")

    vehicle = st.selectbox(
    "Vehicle Type",
    [
        "Passenger Car",
        "SUV",
        "Motorcycle",
        "Truck",
        "Other"
    ]
)

    road = st.selectbox(
    "Road Type",
    [
        "Two-Way Not Divided",
        "Two-Way Divided",
        "Two-Way Divided Median"
    ]
)

    time_options = [
    "12:00 AM","1:00 AM","2:00 AM","3:00 AM","4:00 AM","5:00 AM",
    "6:00 AM","7:00 AM","8:00 AM","9:00 AM","10:00 AM","11:00 AM",
    "12:00 PM","1:00 PM","2:00 PM","3:00 PM","4:00 PM","5:00 PM",
    "6:00 PM","7:00 PM","8:00 PM","9:00 PM","10:00 PM","11:00 PM"
]

    selected_time = st.selectbox(
    "Select Accident Time",
    time_options
)

    hour = time_options.index(selected_time)

    month = st.slider("Month", 1, 12, 1)

    weekend = st.selectbox(
    "Weekend?",
    ["No", "Yes"]
)

    rush = st.selectbox(
    "Rush Hour?",
    ["No", "Yes"]
)

    density = st.number_input(
    "Historical Accident Density",
    min_value=0,
    value=1000
)
    if st.button("Predict Severity"):

       severity_input = pd.DataFrame({
        "Vehicle Type": [vehicle],
        "Road Type": [road],
        "Hour of Day": [hour],
        "Month": [month],
        "Weekend Indicator": [weekend],
        "Rush Hour Indicator": [rush],
        "Historical Accident Density": [density]
    })

       severity_encoded = pd.get_dummies(severity_input)

       severity_encoded = severity_encoded.reindex(
        columns=severity_features,
        fill_value=0
    )

       pred = severity_model.predict(severity_encoded)[0]

       severity_map = {
        0: "Minor",
        1: "Serious",
        2: "Fatal"
    }

       severity_result = severity_map[pred]

       st.success(f"Predicted Severity: {severity_result}")

       if severity_result == "Fatal":
        st.error("""
🚨 Emergency Recommendations

• Alert nearby hospitals
• Dispatch ambulance services
• Activate traffic control
""")

       elif severity_result == "Serious":
        st.warning("""
⚠️ Moderate Alert

• Ensure quick medical response
• Monitor traffic conditions
""")

       else:
        st.success("""
✅ Minor Severity

• Standard emergency response sufficient
""")

    
with tab3:

    st.header("Model Insights")

    importance = pd.DataFrame({
        "Feature": severity_features,
        "Importance": severity_model.feature_importances_
    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    ).head(10)

    st.subheader("Top Features Affecting Severity")

    st.bar_chart(
        importance.set_index("Feature")
    )

with tab4:
    st.header("🗺️ US Accident Hotspot Map")

    m = folium.Map(
        location=[39.8283, -98.5795],
        zoom_start=4
    )

    for location, coords in district_coords.items():
        folium.Marker(
            location=coords,
            popup=location,
            tooltip=location,
            icon=folium.Icon(color="red")
        ).add_to(m)

    st_folium(
        m,
        width=700,
        height=500
    )   