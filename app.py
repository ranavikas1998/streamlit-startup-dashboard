import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",page_title="Startup Analysis")  # take the space website page title show in bro

file_path = os.path.join(os.path.dirname(__file__), "data", "startup_cleaned.csv")
df = pd.read_csv(file_path)
def load_investor_details(investor):
    st.title(investor)

#  Load the recent 5 investments of the investor
    last5_df=df[df["Investors"].str.contains("Investors")][["date", "startup", "vertical", "city", "amount"]].head()
    st.subheader("Most Recent Investors")
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
    # biggest investments
        big_series=df[df["Investors"].str.contains("investor")].groupby("startup")["amount"].sum().sort_values(ascending=False).head()

        st.subheader("Biggest  Investments")
        fig,ax=plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    st.dataframe(big_series) # for give the biggest  5 tabeluer form data



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


