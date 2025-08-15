import streamlit as st

email =st.text_input("enter email")
password=st.text_input("enter password")

btn=st.button("login")

# if the button is clicked
if btn:
    if email=="ranavikas1998@gmail.com" and password=="1234":
        st.success("Login Successful")
        st.balloons()
    else:
        st.error("Login Failed")


