# 🧠 Diabetes Prediction System  

An end-to-end **Machine Learning** project that predicts the likelihood of diabetes based on clinical data.  
It covers the **entire ML pipeline** — from data cleaning and EDA to model training, evaluation, and deployment via **Streamlit** and **FastAPI**.

---

## 🚀 Project Overview
Early detection of diabetes can help prevent serious complications.  
This project uses the **Pima Indians Diabetes Dataset** to train and deploy a prediction model accessible through both a **web app** and a **REST API**.

---

## 🧩 Tech Stack
- **Language:** Python 3.11  
- **Libraries:** pandas, numpy, scikit-learn, lightgbm, matplotlib, seaborn  
- **Deployment:** Streamlit, FastAPI, Uvicorn  
- **Model Serialization:** joblib  

---

## 📂 Project Structure
```bash
diabetes/
│
├── app.py                  # FastAPI backend
├── streamlit_app.py        # Streamlit frontend
├── lightgbm_model.pkl      # Trained model
├── data.csv                # Dataset
├── requirements.txt        # Dependencies
├── url.py                  # API endpoints test file
├── diabetes.ipynb          # Jupyter notebook (EDA + modeling)
└── README.md               # Documentation
```

🧹 1. Data Cleaning & EDA
Replaced invalid zero values in key medical features (Glucose, BMI, BloodPressure) with median values.
Analyzed feature correlations and class imbalance.
Visualized patterns using histograms, pairplots, and boxplots.
Discovered strong relationships between:
High Glucose & BMI → greater diabetes probability
Age and DiabetesPedigreeFunction → moderate influence

⚙️ 2. Model Training
Evaluated multiple ML algorithms:
Logistic Regression
Random Forest
XGBoost
LightGBM ✅ (Best performance)
Final Model Metrics:
Accuracy: 75%
F1-Score: 0.72
Recall: 0.89 (prioritizing fewer false negatives)

🧪 3. API (FastAPI)
Run the backend server:
bash
Copy code
uvicorn app:app --reload
Test via http://127.0.0.1:8000/docs
Sample Request:
json
Copy code
{
  "Pregnancies": 3,
  "Glucose": 145,
  "BloodPressure": 82,
  "SkinThickness": 23,
  "Insulin": 94,
  "BMI": 32.5,
  "DiabetesPedigreeFunction": 0.601,
  "Age": 33
}

Sample Response:
json
Copy code
{
  "prediction": 1,
  "result": "Likely to have diabetes"
}

💻 4. Streamlit Web App
Run:
bash
Copy code
streamlit run streamlit_app.py
Interactive UI for real-time predictions.
Users enter their medical data and get immediate results with visual indicators.

🧠 5. Key Insights
Glucose and BMI are the strongest indicators.
High recall ensures better detection of diabetic cases.
LightGBM outperforms others in speed and accuracy.

📦 Installation
bash
Copy code
git clone https://github.com/<your_username>/diabetes-prediction.git
cd diabetes-prediction
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
🔮 Future Improvements
Integrate SHAP for interpretability.

Add Docker containerization.
Deploy on Render / Hugging Face Spaces / AWS Lambda.

✨ Author
👩‍💻 Fatto — Data Science & AI
📫 Connect on LinkedIn

🏷️ Tags
#DataScience #MachineLearning #FastAPI #Streamlit #LightGBM #EDA #Python #AI

yaml
Copy code
