# -*- coding: utf-8 -*-
"""MultipleDiseasePrediciton.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kxPbCOzMqfwB_IYBuLJu9MnEnleyVb12
"""

# !pip install -q streamlit
# !pip install -q streamlit_option_menu

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))
# kidney_model = pickle.load(open('kidney_model.sav', 'rb'))

# sidebar for navigate

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System using ML',
    ['Diabetes Prediction',
    'Heart Disease Prediciton'] ,
#     'Kidney Disease Prediciton'],
                        icons=['activity' ,'heart','clipboard2-pulse'],
                        default_index=0)

# Diabetes Prediction
if (selected=='Diabetes Prediciton'):
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
      Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
      Glucose = st.text_input('Glucose level')
    with col3:
      BloodPressure = st.text_input('Blood Pressure value')
    with col1:
      SkinThickness = st.text_input('Skin Thickness value')
    with col2:
      Insulin = st.text_input('Insulin level')
    with col3:
      BMI = st.text_input('BMI value')
    with col1:
      DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
      Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_dignosis = ''

    # creating a button for prediction
    if st.button('Diabetes Test Result'):
      diab_prediciton = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure,
                                                 SkinThickness, Insulin, BMI,
                                                 DiabetesPedigreeFunction, Age]])
      if (diab_prediction[0]==1):
        diab_diagnosis = 'The person is Diabetic'
      else:
        diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)




# Heart Disease
if (selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediciton using ML')
 # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
      Sex = st.text_input('1 = male, 0 = female')
    with col2:
      Cp = st.text_input('Chest Pain Type')
    with col3:
      Trestbps = st.text_input('Resting Bp in mm Hg')
    with col1:
      Chol = st.text_input('Serum Cholestoral in mg/dl')
    with col2:
      Fbs = st.text_input('Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)')
    with col3:
      Restecg = st.text_input('Resting electrocardigraphic ')
    with col1:
      Thalach = st.text_input('Maximum heart rate achieved')
    with col2:
      Exang = st.text_input('Exercisee induced angina (1 = yes, 0 = no)')
    with col3:
      Oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col1:
      Slope = st.text_input('The slope of the peak exercise ST segment')
    with col2:
      Ca = st.text_input('number of major vessels (0-3) colored by flourosopy')
    with col3:
      Thal = st.text_input('thal - 3 = normal; 6 = fixed defect; 7 = reversable defect')
    with col1:
      Age = st.text_input('Age of the Person')

    # code for Prediction
    heart_dignosis = ''

    # creating a button for prediction
    if st.button('Heart Test Result'):
      heart_prediciton = heart_model.predict([[ sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, age ]])
      if (heart_prediction[0]==1):
        heart_diagnosis = 'The person has a Heart Disease.'
      else:
        heart_diagnosis = 'The person does not have a Heart Disease.'
    st.success(heart_diagnosis)







# # Kidney Disease
# if (selected=='Kidney Disease Prediction'):
#     st.title('Kidney Disease Prediciton using ML')

#  # getting the input data from the user
#     col1, col2, col3 = st.columns(3)

#     with col1:
#       Age = st.text_input('Number of Pregnancies')
#     with col2:
#       BloodPressure = st.text_input('Blood Pressure value')
#     with col3:
#       Sg = st.text_input('Specific gravity ')
#     with col1:
#       Al = st.text_input('Albumin')
#     with col2:
#       Su = st.text_input('Sugar')
#     with col3:
#       Pc = st.text_input('Pus cells')
#     with col1:
#       Pcc = st.text_input('Pus cell clumps')
#     with col2:
#       Ba = st.text_input('Bacteria')
#     with col3:
#       Bgr = st.text_input('Blood Glucose Random ')
#     with col1:
#       Bu = st.text_input('Blood urea')
#     with col2:
#       Sc = st.text_input('Serum creatinine')
#     with col3:
#       Sod = st.text_input('Sodium')
#     with col1:
#       Pot = st.text_input('Potassium')
#     with col2:
#       Hemo = st.text_input('Insulin level')
#     with col3:
#       Pcv = st.text_input('Packed cells volume')
#     with col1:
#       Htn = st.text_input('Hypertension')
#     with col2:
#       Dm = st.text_input('Diabetes mellitus')
#     with col3:
#       Cad = st.text_input('Coronary Artery Disease')
#     with col1:
#       Appet = st.text_input('Appetite')
#     with col2:
#       Pe = st.text_input('Pedal Edema')
#     with col3:
#       Ane = st.text_input('Anemia')


#     # code for Prediction
#     kidney_dignosis = ''

#     # creating a button for prediction
#     if st.button('Chronic Kidney Test Result'):
#       kidney_prediciton = kidney_model.predict([[age, bp ,sg ,al ,su ,pc ,pcc ,ba ,bgr ,bu ,sc ,sod ,pot ,hemo ,pcv ,htn ,dm ,cad ,appet ,pe ,ane]])

#       if (kidney_prediction[0]==1):
#         kidney_diagnosis = 'The person has Chronic Kidney Disease.'
#       else:
#         kidney_diagnosis = 'The person does not have Chronic Kidney Disease.'
#     st.success(kidney_diagnosis)



# # !streamlit run /content/MultipleDiseasePrediction.py &> /content/streamlit run command.txt

# # # Run the Streamlit app
# # !streamlit run /content/MultipleDiseasePrediction.py & npx localtunnel --port 8501

