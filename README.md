# 🏠 End-to-End House Price Prediction

## 📌 Project Overview

This project is an end-to-end machine learning application that predicts house prices based on various property features. It covers the complete ML lifecycle — data preprocessing, feature engineering, model training and evaluation, and deployment using **Streamlit**.

Users can interact with a clean web interface, input house details, and get real-time price predictions.

---

## 🚀 Features

* Data cleaning and preprocessing(EDA)
* Feature encoding and scaling
* Training multiple regression models

  * Linear Regression
  * Polynomial Regression
  * Ridge Regression
  * Lasso Regression
* Model evaluation using MSE, R² and RMSE
* Cross-validation (K-Fold) for robust model evaluation
* Best model selection
* Interactive Streamlit web application
* Real-time house price prediction

---

## 🧠 Technologies Used

* **Python**
* **NumPy, Pandas** – Data manipulation
* **Scikit-learn** – Machine learning models
* **Matplotlib, Seaborn** – Data visualization
* **Joblib** – Model persistence
* **Streamlit** – Web app deployment

---

## 📂 Project Structure

```
House_Price_Prediction/
│
├── app.py                     # Streamlit application
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
│
├── models/
│   ├── best_model.pkl         # Trained ML model
│   └── scaler.pkl             # Feature scaler
│
├── data/                      # Dataset (optional)
├── notebooks/                 # Colab notebooks (optional)
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/End-to-End-House-Price-Prediction.git
cd End-to-End-House-Price-Prediction
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv modelenv
modelenv\Scripts\activate   # Windows
source modelenv/bin/activate # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

```bash
streamlit run app.py
```

The app will open automatically in your browser.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push the project to GitHub
2. Connect the repository to Streamlit Cloud
3. Select `app.py` as the main file

---

## 📊 Model Evaluation

* Models were evaluated using MSE, **R² Score** and **RMSE**
* **Cross-validation (K-Fold)** was performed to ensure robust evaluation and avoid overfitting
* Linear Regression performed best, indicating a strong linear relationship between features and target

---

## 🎯 Use Case

* Real estate price estimation
* Learning end-to-end ML workflows
* Portfolio project for ML/Data Science roles

---

## 👤 Author

**Anaswara KS**
BCA Graduate | Machine Learning Enthusiast

---

## ⭐ Acknowledgements

* Scikit-learn documentation
* Streamlit community
* Open datasets for housing price prediction

---

Feel free to ⭐ this repository if you find it useful!
