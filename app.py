from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI(title="Diabetes Predictor")

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Load model
diabetes_model = joblib.load("lightgbm_model.pkl")

@app.post("/diabetes_prediction")
def diabetes_pred(input_parameters: ModelInput):
    input_dict = input_parameters.dict()
    input_list = [
        input_dict['Pregnancies'],
        input_dict['Glucose'],
        input_dict['BloodPressure'],
        input_dict['SkinThickness'],
        input_dict['Insulin'],
        input_dict['BMI'],
        input_dict['DiabetesPedigreeFunction'],
        input_dict['Age']
    ]

    prediction = diabetes_model.predict([input_list])
    result = "Has Diabetes" if prediction[0] == 1 else "Does Not Have Diabetes"
    return {"prediction": int(prediction[0]), "result": result}
