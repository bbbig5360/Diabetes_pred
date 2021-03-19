import mysql.connector
from mysql.connector import Error
import streamlit as st


def run_check():

    name = st.text_input('이름을 입력하세요')
    birth_date = st.date_input('생년월일을 입력하세요')

    if st.button('다시 확인하고 싶으시면 버튼을 누르세요'):
        try:           
            connection = mysql.connector.connect(
                    host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                    database = 'streamlitdb',
                    user = 'awsstream',
                    password = 'aws1234'
            )

            if connection.is_connected():
                print('MySQL start')
                
                cursor = connection.cursor(dictionary=True)

                query = '''select outcome from user
                            where name= %s and birth_date = %s;'''
                input_row = (name, birth_date)

                cursor.execute(query, input_row)
                
                result = cursor.fetchall()
                
                if result==1 :
                    st.write('당뇨에 걸릴 확률이 높습니다.')
                elif result == 0:
                    st.write('당뇨에 걸릴 확률이 낮습니다.')
                else :
                    st.write('저장된 데이터가 없습니다.')

        except Error as e:
            print('db관련 에러 발생', e)
        
        finally :
            cursor.close()
            connection.close()
            print('MySQL connection END')
