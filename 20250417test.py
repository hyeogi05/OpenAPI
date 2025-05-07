import streamlit as st

# col1, col2 = st.columns(2)

# with col1 :
#   st.write("왼쪽")
#   st.write("왼쪽의 내용입니다.")
  
# with col2 :
#   st.write("오른쪽")
#   st.write("오른쪽의 내용입니다.")
  
# st.write("안녕~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 아래쪽?")

# 균등하게 3칸
# col1, col2, col3 = st.columns(3)
# 비율이 다르게
col1, col2, col3 = st.columns([1,5,1])

with col1 :
  st.write("왼쪽")
  st.write("왼쪽의 내용입니다.")
  
with col2 :
  st.write("중앙")
  st.write("중앙의 내용입니다.")

with col3 :
  st.write("오른쪽")
  st.write("오른쪽의 내용입니다.")
  

