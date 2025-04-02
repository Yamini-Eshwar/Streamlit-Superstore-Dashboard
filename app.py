import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Sample Superstore Data Analysis")
st.header("e-commerce data")
st.subheader("Focused on profits & sales")
st.write("e-commerce data analysis")

st.markdown("Superstore analysis app")

if st.button("click me"):
    st.write("I am clicked")

info1 = st.text_input("Enter your info1")
info2 = st.text_input("Enter your info2")
st.write("info1: ", info1)
st.write("info2: ", info2)

age = st.slider("Enter your age year", 1, 80, 5)
st.write("age: ", age)


data1 = pd.read_excel(r"C:\Users\vamsi\Downloads\SampleSuperstore.xlsx")

st.table(data1.head())         # like book - just static
st.dataframe(data1.describe()) #like phone screen, you can change,sort,scroll,zoom


st.selectbox("select your category", data1["Category"].unique())
st.radio("select your sub-Category", data1["Sub-Category"].unique())


profit_data = data1.groupby("Category")["Profit"].sum()
st.line_chart(profit_data)


fig, ax = plt.subplots()
ax.bar(data1["Category"], data1["Profit"], color="blue")
plt.title("Profit Plot")
st.pyplot(fig)