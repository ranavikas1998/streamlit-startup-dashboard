import streamlit as st
import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "data", "startup_funding.csv")
df = pd.read_csv(file_path)
st.dataframe(df)

st.sidebar.title("Startup Funding Analysis")
option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])
if option =="Overall Analysis":
    st.title("Overall Analysis")
    pass
elif option =="Startup":
    st.sidebar.selectbox("Select Startup",["Byjus","Ola","Flipkart"])
    st.title("Startup Analysis")
    pass
else:
    st.sidebar.selectbox("Select Startup", ["Richman1", "Richman2 ", "Richman3"])
    st.title("Investor Analysis")

