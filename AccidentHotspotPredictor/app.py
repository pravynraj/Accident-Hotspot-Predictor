import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# --------------------------
# 🌍 PAGE CONFIGURATION
# --------------------------
st.set_page_config(page_title="Accident Hotspot Predictor", layout="wide")
st.title("🚗 Accident Hotspot Predictor")
st.markdown("### Predict accident severity and visualize hotspots using machine learning and maps")

# --------------------------
# 📂 UPLOAD DATASET
# --------------------------
uploaded_file = st.file_uploader("Upload Accident CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File Uploaded Successfully!")
    st.write("Preview of Data:")
    st.dataframe(df.head())
else:
    st.info("Please upload your accident dataset (CSV format).")
    st.stop()

# --------------------------
# 🧹 DATA CLEANING
# --------------------------
df = df.dropna(subset=['City', 'Severity', 'Temperature(F)', 'Weather_Condition', 'State'])
df = df[df['Severity'].apply(lambda x: str(x).isdigit())]
df['Severity'] = df['Severity'].astype(int)

data = df[['Severity', 'Temperature(F)', 'Weather_Condition', 'City', 'State']]

# --------------------------
# 🔠 ENCODING
# --------------------------
le_weather = LabelEncoder()
le_city = LabelEncoder()
le_state = LabelEncoder()

data['Weather_Code'] = le_weather.fit_transform(data['Weather_Condition'])
data['City_Code'] = le_city.fit_transform(data['City'])
data['State_Code'] = le_state.fit_transform(data['State'])

X = data[['Temperature(F)', 'Weather_Code', 'City_Code', 'State_Code']]
y = data['Severity']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# --------------------------
# 🧍‍♀️ USER INPUT SECTION
# --------------------------
st.sidebar.header("Enter Details for Prediction")

temperature = st.sidebar.number_input("Temperature (°F)", min_value=-20.0, max_value=130.0, value=70.0)
weather = st.sidebar.selectbox("Weather Condition", list(le_weather.classes_))
city = st.sidebar.selectbox("City", list(le_city.classes_))
state = st.sidebar.selectbox("State", list(le_state.classes_))

# Encode user input
weather_code = le_weather.transform([weather])[0]
city_code = le_city.transform([city])[0]
state_code = le_state.transform([state])[0]

input_data = np.array([[temperature, weather_code, city_code, state_code]])

# --------------------------
# 🔮 PREDICTION
# --------------------------
if st.sidebar.button("Predict Accident Severity"):
    prediction = model.predict(input_data)[0]
    st.sidebar.success(f"Predicted Accident Severity Level: {prediction}")
    st.balloons()

# --------------------------
# 🗺️ MAP VISUALIZATION
# --------------------------
st.subheader("🗺️ Accident Hotspot Map")
st.caption("Map showing accident locations based on severity")

# Randomly generate coordinates (demo purpose)
cities = df['City'].unique()
city_coords = {city: (np.random.uniform(10, 50), np.random.uniform(70, 90)) for city in cities}
df['Lat'] = df['City'].map(lambda x: city_coords[x][0])
df['Lng'] = df['City'].map(lambda x: city_coords[x][1])

m = folium.Map(location=[22.9734, 78.6569], zoom_start=5, tiles='CartoDB positron')
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Lat'], row['Lng']],
        radius=row['Severity'] * 1.5,
        color='crimson',
        fill=True,
        fill_color='red',
        fill_opacity=0.5,
        popup=f"City: {row['City']} | Severity: {row['Severity']} | Weather: {row['Weather_Condition']}"
    ).add_to(m)

folium_static(m)

# --------------------------
# 📊 ADDITIONAL INSIGHTS
# --------------------------
st.subheader("📈 Severity Distribution")
st.bar_chart(df['Severity'].value_counts().sort_index())
