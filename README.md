# ─────────────── STREAMLIT STARTUP DASHBOARD ───────────────
# Copy-paste this ENTIRE block into your terminal/text editor

# 1️⃣ Create project folder
mkdir streamlit-startup-dashboard
cd streamlit-startup-dashboard

# 2️⃣ Create files and folders

# ---------- app.py ----------
cat <<EOL > app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_doc import helper_function

st.set_page_config(page_title="Startup Dashboard", layout="wide")
st.title("Startup Dashboard")
st.write("Welcome to the Streamlit Startup Dashboard!")

# Load dummy data
data = pd.read_csv("data/dummy_data.csv")

st.subheader("Data Preview")
st.dataframe(data.head())

st.subheader("Statistics")
st.write(data.describe())

st.subheader("Plot Example")
fig = px.bar(data, x="Startup", y="Revenue")
st.plotly_chart(fig)

st.subheader("Helper Function Example")
st.write(helper_function(5))
EOL

# ---------- streamlit_doc.py ----------
cat <<EOL > streamlit_doc.py
def helper_function(x):
    return f"Helper function received: {x}"
EOL

# ---------- requirements.txt ----------
cat <<EOL > requirements.txt
streamlit
pandas
numpy
matplotlib
plotly
EOL

# ---------- data folder & dummy CSV ----------
mkdir data
cat <<EOL > data/dummy_data.csv
Startup,Revenue,Employees
Alpha,100000,10
Beta,150000,15
Gamma,120000,12
Delta,90000,8
Epsilon,130000,11
EOL

# ---------- notebooks folder & dummy notebook ----------
mkdir notebooks
cat <<EOL > notebooks/demo_notebook.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Demo Notebook\\n",
    "This is a dummy notebook for Streamlit Startup Dashboard."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\\n",
    "data = pd.read_csv('../data/dummy_data.csv')\\n",
    "data.head()"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
EOL

# ---------- campusx.jpg ----------
# (Use any placeholder image, e.g., download from https://via.placeholder.com/150)
curl -o campusx.jpg https://via.placeholder.com/150

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the Streamlit app
streamlit run app.py
