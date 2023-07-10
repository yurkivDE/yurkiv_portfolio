import streamlit as st
from send_email import send_email

st.header("Contact Me:")

with st.form(key="email_address"):
    user_email = st.text_input("Your email address:")
    message = st.text_area("Your message:")
    form_submitted = st.form_submit_button("Submit")
    if form_submitted:
        send_email(user_email, message)
        st.info("Your message was sent successfully!")
