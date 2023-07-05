import streamlit as st

st.set_page_config(layout="wide")

col_1, col_2 = st.columns(2)

with col_1:
    st.image("images/photo.jpg", width=300)

with col_2:
    st.title("Yuriy Yurkiv")

    about_me = """
Hello, my name is Yuriy.\n
I am learning Python and I am very passionate about it.\n
Here you can view the applications that I developed during my studies.\n
    """

    st.info(about_me)

app_list_header = """
So here is my apps. Don't judge harshly, we all started once)))
"""
st.write(app_list_header)