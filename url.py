import requests

url = "http://127.0.0.1:8000/diabetes_prediction"

data = {
    "Pregnancies": 5,
    "Glucose": 180,
    "BloodPressure": 90,
    "SkinThickness": 35,
    "Insulin": 130,
    "BMI": 33.2,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 45
}

response = requests.post(url, json=data)
print(response.json())
