import streamlit as st
from eda_app import run_eda
from ml_app import run_ml
from re_check import run_check

def main():
    st.title('당뇨병 예측 앱')

    menu = ['메뉴를 선택하세요', '인공지능에 사용된 데이터셋', '예측 프로그램', '간단 재확인']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == '메뉴를 선택하세요':
        st.write('이 앱은 1000명의 데이터를 이용해 당뇨병 여부를 예측한 인공지능 프로그램입니다.')
        st.write('고객의 정보를 입력하면 당뇨병에 걸릴지 안 걸릴지 예측을 할 수 있습니다.')
    
    elif choice == '인공지능에 사용된 데이터셋':
        run_eda()

    elif choice == '예측 프로그램':
        run_ml()
    
    else :
        run_check()

if __name__ == '__main__':
    main()