import streamlit as st
import pandas as pd
import time

st.title("startup Dashboard")
st.header("I am  learning streamlit")
st.subheader("Vikas Rana")

st.write("This is a normal text")
st.markdown("""
### My favorite movie
- Race 3
- Humshakals
- Housefull
""")

st.code("""
def foo(input):
 return foo**2
x==foo(2)
""")

st.latex("x^2+y^2+2=0")

df=pd.DataFrame({
    "name":["vikas","sachin","rohit"],
    "marks":[50,60,70],
    "package":[10,12,14]
})

st.dataframe(df)

st.metric("Revenue","Rs 3L","-3%")

st.json({
"name":["vikas","sachin","rohit"],
    "marks":[50,60,70],
    "package":[10,12,14]
})
#st.image("campusx.jpg")
# st.video("newvideo.mp4")

st.sidebar.title("Sidebar Title")
col1,col2,col3=st.columns(3)

with col1:
    st.image("campusx.jpg")
with col2:
    st.image("campusx.jpg")
with col3:
    st.image("campusx.jpg")

st.error("Login Failed")
st.success("Login Successful")
st.info("Login Successful")
st.warning("Login Successful")

bar=st.progress(0)
for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)