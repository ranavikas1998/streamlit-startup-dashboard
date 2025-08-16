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

    st.header("Month on Month (MoM) graph")
    selected_option = st.selectbox("Select Type", ["Total", "Count"])

    if selected_option == "Total":
        temp_df = df.groupby(df["date"].dt.to_period("M"))["amount"].sum().reset_index()
    else:
        temp_df = df.groupby(df["date"].dt.to_period("M"))["amount"].count().reset_index()

    # Month-Year column
    temp_df["month_year"] = temp_df["date"].astype(str)

    # Plot
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    ax4.bar(temp_df["month_year"], temp_df["amount"].values, color="skyblue")

    plt.xticks(rotation=90)
    ax4.set_xlabel("Month-Year")
    ax4.set_ylabel("Funding Amount (Cr)" if selected_option == "Total" else "Number of Deals")
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
    startup_names = df["startup"].dropna().unique()
    selected_startup=st.sidebar.selectbox("Select Startup",sorted(df["startup"].unique().tolist())) # convert to the list
    st.title("Startup Analysis")
    btn1=st.sidebar.button("Find Startup Details")

    col1,col2=st.columns(2)

    if btn1:
        st.subheader(f"details for {selected_startup}")
        temp_df = df[df["startup"] == selected_startup][["date", "Investors", "amount", "vertical", "city"]]
        st.dataframe(temp_df)

        col1, col2 = st.columns(2)  # <- columns yahin banao

        with col1:
            st.subheader("Funding Summary")
            st.write(f"Total Funding: {temp_df['amount'].sum()} Cr")
            st.write(f"Max Round: {temp_df['amount'].max()} Cr")

            # Line chart (Funding Trend)
            st.subheader("Funding Trend Over Time")
            trend_df = temp_df.copy()
            trend_df["date"] = pd.to_datetime(trend_df["date"], errors="coerce")  #  string → datetime
            trend_df = trend_df.groupby("date")["amount"].sum().reset_index()
            trend_df = trend_df[trend_df["amount"] > 0]

            trend_df = trend_df.sort_values("date")  #  sort by date

            fig, ax = plt.subplots()
            ax.plot(trend_df["date"], trend_df["amount"], marker="o", linestyle="-")
            ax.set_xlabel("Date")
            ax.set_ylabel("Funding Amount (Cr)")
            ax.set_title(f"Funding Trend for {selected_startup}")
            plt.xticks(rotation=45)

            st.pyplot(fig)

        with col2:
            st.subheader("Other Info")
            # Rounds count
            rounds = temp_df[["date", "amount"]].drop_duplicates().shape[0]

            # Unique Investors nikalne ke liye split + explode
            investors_expanded = temp_df.assign(
                Investors=temp_df["Investors"].str.split(",")
            ).explode("Investors")
            investors_expanded["Investors"] = investors_expanded["Investors"].str.strip()

            st.write(f"Number of Rounds: {rounds}")
            st.write(f"Unique Investors: {investors_expanded['Investors'].nunique()}")

            # Investor Participation bar chart (count of rounds)
            st.subheader("Investor Participation (Number of Rounds)")

            investor_participation = investors_expanded.groupby("Investors")["date"].count().reset_index()
            investor_participation = investor_participation.sort_values("date", ascending=False)

            fig2, ax2 = plt.subplots()
            ax2.bar(investor_participation["Investors"], investor_participation["date"], color="skyblue")
            for i, row in investor_participation.iterrows():
                ax2.text(i, row["date"] + 0.05, row["date"], ha="center", fontsize=8)

            ax2.set_xlabel("Investors")
            ax2.set_ylabel("Number of Rounds")
            ax2.set_title(f"Investor Participation for {selected_startup}")
            plt.xticks(rotation=45, ha="right")

            st.pyplot(fig2)


else:
    selected_investor=st.sidebar.selectbox("Select Startup",sorted(set(df["Investors"].str.split(",").sum())))
    btn2=st.sidebar.button("Find Investor Details")
    if btn2 :
        load_investor_details(selected_investor)


