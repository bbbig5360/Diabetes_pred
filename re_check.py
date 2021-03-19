import mysql.connector
from mysql.connector import Error
import streamlit as st


def run_check():

    name = st.text_input('이름을 입력하세요')
    customer_num = st.number_input('검진번호를 입력하세요',0)

    if st.button('다시 확인하고 싶으시면 버튼을 누르세요'):
        st.info('오류메세지가 나오면 이름과 검진번호를 다시 확인하시고 버튼을 눌러주세요.')
        try:           
            connection = mysql.connector.connect(
                    host = 'database-2.c2tbevxe8w9x.us-east-2.rds.amazonaws.com',
                    database = 'streamlitdb',
                    user = 'awsstream',
                    password = 'aws1234'
            )

            if connection.is_connected():                
                cursor = connection.cursor(dictionary=True)

                query = '''select outcome from user
                            where name= %s and customer_num = %s;'''
                input_row = (name, customer_num)

                cursor.execute(query, input_row)
                
                result = cursor.fetchall()
                
                Diabete = result[0]['outcome']
                
                if Diabete == 1 :
                    st.write('당뇨에 걸릴 확률이 높습니다.')
                elif Diabete == 0 :
                    st.write('당뇨에 걸릴 확률이 낮습니다.')
            
        except Error as e:
            print('db관련 에러 발생', e)
        
        finally :
            cursor.close()
            connection.close()