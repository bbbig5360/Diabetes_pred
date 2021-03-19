import streamlit as st
import joblib
import numpy as np
import mysql.connector
from mysql.connector import Error

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

    name = st.text_input('이름을 입력하세요')
    birth_date = st.date_input('생년월일을 입력하세요')

    input_data = np.array([preg, Gl, BP, ST, Insul, BMI, dpf, age])
    input_data = input_data.reshape(1,-1)
    outcome = 0

    if st.button('당뇨병 예측을 원하신다면 클릭해주세요.'):
        y_pred = model.predict(input_data)
        if y_pred == 1:
            st.write('당뇨병에 걸릴 확률이 높습니다.')
            outcome = 1
        else:
            st.write('당뇨병에 걸릴 확률이 낮습니다.')   
            coutcome = 0

        try:           
            connection = mysql.connector.connect(
                host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                database = 'streamlitdb',
                user = 'awsstream',
                password = 'aws1234'
            )
            if connection.is_connected():

                print('data insert start')
                
                cursor = connection.cursor()
                
                query = '''insert into user(name, birth_date, outcome) 
                            values(%s, %s, %s);'''
                input_row = (name, birth_date, outcome)

                cursor.execute(query, input_row)
                connection.commit()

                print( '{}개 저장됨'.format(cursor.rowcount) )

        except Error as e:
            print('db관련 에러 발생', e)
        
        finally :
            cursor.close()
            connection.close()
            print('MySQL connection END')

