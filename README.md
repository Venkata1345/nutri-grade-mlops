# 🍔 Nutri-Grade MLOps: End-to-End Calorie Predictor

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)
![CI/CD](https://github.com/iamabhishek/nutri-grade-mlops/actions/workflows/ci.yaml/badge.svg)

A complete **End-to-End MLOps Project** that predicts the calorie content of food items based on their nutritional value (Fat, Carbs, Protein, Sugar).

This project goes beyond simple modeling; it implements a robust **MLOps pipeline** including data versioning, experiment tracking, automated testing (CI), and cloud deployment (CD).

---

## 🚀 Live Demo
- **Frontend (Streamlit):** [Link to your Streamlit App](https://nutri-grade-mlops-hbswsm8hrajznfv93xykkg.streamlit.app)"
- **API Documentation (Swagger UI):** [Link to your Render API/docs](https://nutri-grade-mlops.onrender.com/docs)

---

## 🏗️ Architecture & Workflow

This project mimics a production-grade machine learning lifecycle:

1.  **Data Versioning (DVC):** Raw data (McDonald's Nutrition Dataset) is tracked using DVC to ensure reproducibility.
2.  **Experiment Tracking (MLflow):** Model training runs, metrics (RMSE), and parameters are logged to identify the best performing model.
3.  **Model Serving (FastAPI):** The best model is exposed via a REST API using FastAPI and Pydantic for validation.
4.  **Frontend (Streamlit):** A user-friendly web interface consumes the API to display predictions.
5.  **CI/CD (GitHub Actions):** Automated pipeline runs unit tests (`pytest`) on every push to ensure code quality.
6.  **Deployment (Render):** The API is automatically deployed to the cloud.

---

## 📂 Project Structure

```bash
nutri-grade-mlops/
├── .github/workflows/   # CI/CD Pipeline (GitHub Actions)
├── app/                 # FastAPI Source Code
│   └── main.py          # API Endpoints
├── data/                # Data storage (tracked by DVC)
├── models/              # Production Model Artifacts
├── src/                 # ML Scripts
│   ├── load_data.py     # Data Ingestion
│   └── train.py         # Model Training (MLflow)
├── tests/               # Unit Tests
│   └── test_app.py      # API Endpoint Testing
├── streamlit_app.py     # Frontend UI
├── requirements.txt     # Python Dependencies
├── Dockerfile           # Container Configuration
└── README.md            # Project Documentation


## 🛠️ Installation & Setup

### Prerequisites
* Python 3.9+
* Git

### 1. Clone the Repository
```bash
git clone [https://github.com/iamabhishek/nutri-grade-mlops.git](https://github.com/iamabhishek/nutri-grade-mlops.git)
cd nutri-grade-mlops

### 2. Create Virtual Environment
Bash

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
### 3. Install Dependencies
Bash

pip install -r requirements.txt
### 4. Pull Data (DVC)
Note: This requires access to the remote storage. For this demo, you can regenerate the data.

Bash

python src/load_data.py
🏃‍♂️ Usage
1. Train the Model
Run the training script to train a Random Forest regressor and log it to MLflow.

Bash

python src/train.py
2. Run the API (Backend)
Start the FastAPI server locally.

Bash

uvicorn app.main:app --reload
Access the API docs at: http://localhost:8000/docs

3. Run the App (Frontend)
In a new terminal, start the Streamlit interface.

Bash

streamlit run streamlit_app.py
🧪 Testing
This project uses Pytest for automated testing. The test suite checks if the API endpoint returns valid predictions and correct status codes.

Bash

# Run all tests
pytest
🔧 Technologies Used
Language: Python

Web Framework: FastAPI

Frontend: Streamlit

ML Libraries: Scikit-Learn, Pandas, NumPy

Ops Tools:

DVC: Data Version Control

MLflow: Experiment Tracking

GitHub Actions: Continuous Integration

Render: Cloud Deployment
