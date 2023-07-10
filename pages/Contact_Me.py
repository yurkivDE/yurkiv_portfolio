import streamlit as st

st.header("Contact Me:")

with st.form(key="email_address"):
    user_email = st.text_input("Your email address:")
    message = st.text_area("Yuor message:")
    form_submitted = st.form_submit_button("Submit")
    if form_submitted:
        print(user_email)
        print(message)