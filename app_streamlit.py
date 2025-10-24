import streamlit as st
import pandas as pd 
import joblib 

diabetes_model = joblib.load("lightgbm_model.pkl") 

st.title('Diabetes Predication') 

preg = st.number_input("Select Your Score :" , 0,20,0)

glu = st.number_input("Enter Your Glucose level : " , min_value=0 , max_value=300 , value = 120)

blp = st.number_input("Enter your Blood Pressure : " , min_value = 0 , max_value=200 , value=70 )

skt = st.number_input("Enter Your Skin Thinkness : " , min_value = 0 , max_value= 100 , value =20) 

ins = st.number_input("Enter Your Insulin level : " , min_value = 0 , max_value= 900 , value =80)  

bmi = st.number_input("Enter BMI : " , min_value = 0.0 , max_value=100.0 , value = 25.0)

pdp = st.number_input("Enter your Pedigree Function : " , min_value=0.0 , max_value=100.0 , value=25.0)

age = st.number_input("Enter your age : " , min_value=0 , max_value=120 , value=30 )

if st.button("Preict"):
    input_list = [[preg, glu, blp, skt, ins, bmi, pdp, age]] 
    prediction = diabetes_model.predict(input_list)
    result = "Has Diabetes " if prediction[0]==1 else "Does not have diabetes"
    st.success(f"predication:{result}") 