# 🛡️ CipherShield AI

## AI-Powered Credit Card Fraud Detection System using XGBoost & Flask

CipherShield AI is a machine learning-based fraud detection platform designed to identify suspicious credit card transactions using advanced classification techniques. The system uses an optimized **XGBoost model** to analyze transaction patterns and predict whether a transaction is legitimate or fraudulent.

This project combines **Machine Learning + Web Development** to provide an interactive dashboard where users can upload transaction data and receive real-time fraud predictions with probability analysis.

---

# 🚀 Features

- ✅ AI-powered credit card fraud detection
- ✅ XGBoost classification model
- ✅ Handles highly imbalanced transaction data
- ✅ SMOTE-based class balancing
- ✅ CSV transaction upload support
- ✅ Real-time fraud prediction
- ✅ Fraud probability estimation
- ✅ Flask-based web application
- ✅ Fast ML model inference
- ✅ Clean and user-friendly dashboard

---

# 🧠 Machine Learning Workflow

```
Data Collection
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Scaling
        ↓
Class Imbalance Handling (SMOTE)
        ↓
XGBoost Model Training
        ↓
Model Evaluation
        ↓
Model Serialization
        ↓
Flask Deployment
        ↓
Real-Time Prediction
```

---

# 📊 Model Information

### Algorithm
- XGBoost Classifier

### Dataset
- Credit Card Fraud Detection Dataset

### Input Features

- Time
- V1 - V28 anonymized transaction features
- Amount

### Problem Type

Binary Classification

### Classes

- 0 → Legitimate Transaction
- 1 → Fraudulent Transaction

---

# 🛠️ Tech Stack

## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Imbalanced-learn (SMOTE)
- Joblib

## Backend

- Flask
- Python

## Frontend

- HTML
- CSS
- JavaScript

## Tools

- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 📂 Project Structure

```
CipherShield-AI/
│
├── app/
│   ├── main.py
│   ├── model_loader.py
│   └── predictor.py
│
├── model/
│   └── credit_card_fraud_xgboost.pkl
│
├── notebook/
│   └── fraud_detection.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/CipherShield-AI.git
```

## Navigate to Project Folder

```bash
cd CipherShield-AI
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app/main.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# 🔍 How It Works

1. User uploads transaction data through the web interface.
2. Flask receives and processes the input.
3. The trained XGBoost model analyzes transaction patterns.
4. The model predicts the transaction category.
5. The application displays:
   - Transaction status
   - Fraud probability
   - Prediction result

---

# 📈 Model Evaluation

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Confusion Matrix

XGBoost was selected because it performs effectively on structured/tabular datasets and captures complex relationships between transaction features.

---

# 🔮 Future Enhancements

- Real-time transaction monitoring
- Explainable AI using SHAP
- Advanced anomaly detection
- Cloud deployment
- Model performance monitoring
- Automated model retraining pipeline
- User authentication system

---

# 👨‍💻 Author

## Jayendra Ghosh


---

# ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
