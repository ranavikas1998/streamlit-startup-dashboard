import streamlit as st
import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), "data", "startup_cleaned.csv")
df = pd.read_csv(file_path)
def load_investor_details(investor):
    st.title(investor)
#  Load the recent 5 investments of the investor
    last5_df=df[df["Investors"].str.contains("Investors")][["date", "startup", "vertical", "city", "amount"]].head()
    st.subheader("Most Recent Investors")
    st.dataframe(last5_df)



# data cleaning
#df["Investors Name"]=df["Investors Name"].fillna("undisclosed")
#st.dataframe(df)

st.sidebar.title("Startup Funding Analysis")
option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])
if option =="Overall Analysis":
    st.title("Overall Analysis")
    pass
elif option =="Startup":
    st.sidebar.selectbox("Select Startup",sorted(df["startup"].unique().tolist())) # convert to the list
    st.title("Startup Analysis")
    btn1=st.sidebar.button("Find Startup Details")
    pass
else:
    selected_investor=st.sidebar.selectbox("Select Startup",sorted(set(df["Investors"].str.split(",").sum())))
    btn2=st.sidebar.button("Find Investor Details")
    if btn2 :
        load_investor_details(selected_investor)


