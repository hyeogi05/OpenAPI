import streamlit as st
import folium
from streamlit.components.v1 import html

# folium 지도 생성
m = folium.Map(location=[37, 127], zoom_start=6)
marker = folium.Marker(
    [35.183778757, 126.880647243],
    popup='한국폴리텍 V 대학 광주캠퍼스',
    icon=folium.Icon(color='blue')
)
marker.add_to(m)

# 지도를 HTML 문자열로 렌더링
map_html = m._repr_html_()

# Streamlit 페이지에 지도 출력
st.title("대학교 위치 지도")
html(map_html, height=500)