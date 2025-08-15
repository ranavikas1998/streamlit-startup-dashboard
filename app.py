from tkinter.constants import HORIZONTAL

import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",page_title="Startup Analysis")  # take the space website page title show in bro

file_path = os.path.join(os.path.dirname(__file__), "data", "startup_cleaned.csv")
df = pd.read_csv(file_path)
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["month"]=df["date"].dt.month
df["year"]=df["date"].dt.year

def load_overall_analysis():                # last step find  out month to month sale
    st.title("Overall analysis")
    # total invested  amount
    total=round(df["amount"].sum())
    # maximum amount infused in a startup
    max_funding=df.groupby("startup")["amount"].max().sort_values(ascending=False).values[0]
    # avg ticket size
    avg_funding=df.groupby("startup")["amount"].sum().mean()
    # total  funded  startups
    num_startups=df["startup"].nunique()

    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total",str(total)+"Cr")
    with col2:
        st.metric("Max", str(max_funding) + "Cr")
    with col3:
        st.metric("Avg", str(round(avg_funding)) + "Cr")
    with col4:
        st.metric("Funded Startups", num_startups)

    st.header("Month on Month(Mom) graph")
    selected_option=st.selectbox("Select Type",["Total","Count"])
    if selected_option =="Total":
        temp_df = df.groupby(["year", "month"])["amount"].sum().reset_index()
    else:
        temp_df = df.groupby(["year", "month"])["amount"].count().reset_index()
    # amount wise funding
    temp_df["x_axis"] = temp_df["month"].astype("str") + "-" + temp_df["year"].astype("str")
    fig4, ax4 = plt.subplots()
    ax4.bar(temp_df["x_axis"], temp_df["amount"].values)
    st.pyplot(fig4)


def load_investor_details(investor):
    st.title(investor)

#  Load the recent 5 investments of the investor
    last5_df=df[df["Investors"].str.contains("Investors")][["date", "startup", "vertical", "city", "amount"]].head()
    st.subheader("Most Recent Investors")
    st.dataframe(last5_df)

    col1,col2,col3=st.columns(3)     # for reduce space
    with col1:
    # biggest investments
        big_series=df[df["Investors"].str.contains("investor")].groupby("startup")["amount"].sum().sort_values(ascending=False).head()

        st.subheader("Biggest  Investments")
        fig,ax=plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)

    with col2:
        # biggest investments by vertical
        vertical_series = df[df["Investors"].str.contains("Investors")] \
            .groupby("vertical")["amount"].sum().sort_values(ascending=False).head()

        st.subheader("Sectors invested in Vertical")
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series.values,labels=vertical_series.index, autopct="%0.1f%%") # autopct give the percentage and label give the name
        st.pyplot(fig1)

    with col3:
        # biggest investments by vertical
        city_series = df[df["Investors"].str.contains("Investors")] \
            .groupby("city")["amount"].sum().sort_values(ascending=False).head()

        st.subheader("Sector invest in City")
        fig2, ax1 = plt.subplots()
        ax1.pie(vertical_series.values,labels=vertical_series.index, autopct="%0.1f%%") # autopct give the percentage and label give the name
        st.pyplot(fig2)

    df["year"] = df["date"].dt.year
    year_series=df[df["Investors"].str.contains("Investors",na=False)].groupby("year")["amount"].sum()
    st.subheader("year on Year(YOY) Investments")
    fig3, ax3 = plt.subplots()
    ax3.plot(year_series.index,year_series.values)
    st.pyplot(fig3)

    st.dataframe(big_series) # for give the biggest  5 tabeluer form data



# data cleaning
#df["Investors Name"]=df["Investors Name"].fillna("undisclosed")
#st.dataframe(df)


st.sidebar.title("Startup Funding Analysis")
option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])
if option =="Overall Analysis":
     load_overall_analysis()
#    st.title("Overall Analysis")
#    btn0=st.sidebar.button("Show Overall Analysis")
#    if btn0:
        

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


