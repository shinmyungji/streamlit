import streamlit as st

# 제목과 설명
st.title("Streamlit 기본 예제")
st.write("이것은 Streamlit을 이용한 간단한 예제입니다.")

# 슬라이더를 이용해 숫자를 선택
st.write("아래 슬라이더를 이용해 숫자를 선택해 보세요.")
number = st.slider("숫자를 선택하세요", 0, 100, 50)
st.write(f"선택한 숫자는: {number}")

# 텍스트 입력 필드를 이용해 사용자 입력 받기
name = st.text_input("이름을 입력하세요", "홍길동")
st.write(f"안녕하세요, {name}님!")

# 버튼을 이용해 간단한 액션 수행
if st.button("클릭해 보세요"):
    st.write(f"{name}님이 버튼을 클릭하셨습니다!")

# 데이터프레임 출력 예시
import pandas as pd
data = {
    '이름': ['홍길동', '이순신', '김유신'],
    '나이': [30, 45, 29],
    '직업': ['개발자', '디자이너', 'PM']
}
df = pd.DataFrame(data)
st.write("간단한 데이터프레임:")
st.dataframe(df)

# 이미지를 표시하는 예시
st.write("Streamlit을 이용해 이미지도 표시할 수 있습니다.")
st.image("https://via.placeholder.com/150", caption="예시 이미지")


