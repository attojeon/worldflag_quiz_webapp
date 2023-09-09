import streamlit as st
import json

st.set_page_config(
    page_title="Flags of the World",
    page_icon="🇰🇷",
    layout="wide"
)

# flags.json 파일을 읽어서, flags 변수에 저장한다.
def get_data():
    with open("flags.json") as file:
        flags = json.load(file)
    return flags

flags = get_data()

st.title("전 세계 국기 모음")
st.divider()

##################################################################################
# 아래와 같이 st.container()없이 st.columns()만 사용하면, 칼럼의 높이가 다르게 출력된다.
# st.container()를 사용하면, 칼럼의 높이가 동일하게 출력된다.
# cols = st.columns(3) 
# for i in range(len(flags)):
#     col = cols[i%3]
#     col.image(flags[i]["img_url"], caption=flags[i]["country_name"], use_column_width=True)

last = len(flags)
idx = 0
while idx < last:
    cols = st.columns(4)
    with st.container():
        for col in cols:
            if idx < last:
                col.image(flags[idx]["img_url"], caption=flags[idx]["country_name"], use_column_width=True)
                idx += 1


    