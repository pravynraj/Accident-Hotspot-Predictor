# 🚗 Accident Hotspot Predictor

An interactive **Machine Learning-based Accident Hotspot Predictor** built using **Python, Streamlit, Scikit-learn, Folium, and Pandas**. The application predicts accident severity based on environmental conditions and visualizes accident hotspots on an interactive map.

## 📌 Overview

Road accidents are influenced by multiple factors such as weather, temperature, and location. This project uses a **Random Forest Classifier** to predict accident severity from historical accident data and provides an intuitive dashboard for data visualization.

Users can upload their own accident dataset, receive severity predictions, and explore accident hotspots through an interactive map.

---

## ✨ Features

- 📂 Upload accident dataset (CSV)
- 🧹 Automatic data preprocessing and cleaning
- 🤖 Machine Learning-based accident severity prediction
- 🌤 Predict severity using:
  - Temperature
  - Weather Condition
  - City
  - State
- 🗺 Interactive accident hotspot visualization using Folium
- 📊 Severity distribution charts
- 🎯 Simple and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web Application |
| Scikit-learn | Machine Learning |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Folium | Interactive Maps |
| Streamlit-Folium | Map Integration |

---

## 📂 Project Structure

```
AccidentHotspotPredictor/
│
├── app.py              # Main Streamlit Application
├── accidents.csv       # Sample Dataset
├── index.html          # Frontend Demo
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Accident-Hotspot-Predictor.git
```

### 2. Navigate to the Project

```bash
cd Accident-Hotspot-Predictor
```

### 3. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn folium streamlit-folium
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 📁 Dataset Requirements

The uploaded CSV should contain the following columns:

| Column |
|---------|
| City |
| State |
| Severity |
| Temperature(F) |
| Weather_Condition |

Additional columns are allowed but not required.

---

## 🤖 Machine Learning Model

The project uses the **Random Forest Classifier** for accident severity prediction.

### Input Features

- Temperature
- Weather Condition
- City
- State

### Target

- Accident Severity

---

## 🗺️ Visualization

The application generates an interactive map displaying accident hotspots where:

- Larger markers indicate higher accident severity.
- Each marker provides:
  - City
  - Severity Level
  - Weather Condition

It also includes:

- Severity Distribution Bar Chart
- Interactive Hotspot Map

---

## 🚀 Future Enhancements

- Real GPS coordinates instead of generated locations
- Live weather API integration
- Deep Learning prediction models
- Heatmap visualization
- Time-series accident forecasting
- User authentication
- Cloud deployment (AWS/Azure)

---

## 📸 Application Preview

Add screenshots here after running the application.

```
images/
    dashboard.png
    prediction.png
    hotspot-map.png
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Machine Learning Classification
- Data Cleaning & Feature Engineering
- Label Encoding
- Interactive Data Visualization
- Geospatial Mapping
- Streamlit Dashboard Development
- Python Data Science Workflow

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author



If you found this project useful, consider giving it a ⭐ on GitHub.
