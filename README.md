#  US Road Accident Prediction System

 Overview
The US Road Accident Prediction System is a machine learning-based web application developed using Streamlit. It helps predict accident hotspot risk and accident severity using historical accident patterns and provides visual insights through an interactive dashboard.

#Objectives
- Predict accident hotspot risk levels.
- Predict accident severity.
- Visualize accident-prone regions using a US hotspot map.
- Provide insights to support road safety awareness.

# Technologies Used
- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib
- Folium
- Streamlit-Folium
- Git & GitHub

# Machine Learning Models
# Hotspot Prediction
- Input Features:
  - District/Location
  - Hour of Day
- Output:
  - Low Risk
  - Medium Risk
  - High Risk

#Severity Prediction
- Predicts the severity level of road accidents based on selected accident-related factors.

#Features
-  Hotspot Risk Prediction
-  Accident Severity Prediction
- Insights Dashboard
-  US Hotspot Visualization
- User-friendly Streamlit Interface

#How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/Anshika-03-stack/US-ROAD-ACCIDENT.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application:

```bash
streamlit run app.py
```

# Project Structure


US-ROAD-ACCIDENT/
│
├── app.py
├── hotspot_model.pkl
├── hotspot_features.pkl
├── severity_model.pkl
├── severity_features.pkl
├── requirements.txt
└── README.md

## 📜 License
This project was developed for academic purposes.
