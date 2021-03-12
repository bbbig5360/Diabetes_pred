import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer


def run_eda():
    st.subheader('EDA화면입니다.')

    radio_menu = ['데이터 프레임', '통계치', '상관관계표']
    selected_radio = st.radio('선택하세요', radio_menu)


    # 확인해보니 0값이 많아 평균값으로 맞춰주기.
    fill = SimpleImputer(missing_values=0, strategy='mean')
    
    df = pd.read_csv('data/diabetes.csv')
    df.iloc[:, :-1] = fill.fit_transform(df.iloc[:, :-1])

    int_list = ['Pregnancies','Glucose', 'BloodPressure', 'SkinThickness', 'Insulin']
    df[int_list] = df[int_list].astype(int)

    if selected_radio == '데이터 프레임':
        st.dataframe(df)

    if selected_radio == '통계치':
        st.dataframe(df.iloc[:, :-1].describe())
    
    if selected_radio == '상관관계표':
        st.dataframe(df.corr())



