import streamlit as st
import pandas as pd

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
st.image("campusx.jpg")
# st.video("newvideo.mp4")