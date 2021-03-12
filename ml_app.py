import streamlit as st
import joblib
import numpy as np


def run_ml():
    st.subheader('Machine Learning 화면입니다.')

    model = joblib.load('data/diabetes_ai.plk')

    preg = st.number_input('임신 횟수를 입력해주세요',0)
    Gl = st.number_input('공복혈당을 입력해주세요(mm Hg)',0)
    BP = st.number_input('혈압을 입력해주세요(mm)',0)
    ST = st.number_input('피부 두께를 입력해주세요',0)
    Insul = st.number_input('인슐린 수치를 입력해주세요',0)
    BMI = st.number_input('BMI를 입력해주세요',0.0)
    dpf = st.number_input('당뇨 가족력을 입력하세요',0.0)
    age = st.number_input('나이를 입력하세요',0,100)    


    input_data = np.array([preg, Gl, BP, ST, Insul, BMI, dpf, age])
    input_data = input_data.reshape(1,-1)


    if st.button('당뇨병 예측을 원하신다면 클릭해주세요.'):
        y_pred = model.predict(input_data)

        if y_pred == 1:
            st.write('당뇨병에 걸릴 확률이 높습니다.')
        else:
            st.write('당뇨병에 걸릴 확률이 낮습니다.')   