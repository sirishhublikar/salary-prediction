import streamlit as st
import joblib
string = "Salary Prediction"
st.set_page_config(page_title=string)
st.title("Predict Your Salary!")
st.write("""
# Salary Prediction Model
Salary vs. *Experience*
""")
mymodel = joblib.load("salary.pkl")
exp = st.sidebar.slider('Experience',1.0,50.0,2.0)
salary = round(mymodel.predict([[exp]])[0],2)
st.write(f"Experience: ", exp)
st.write(f"Salary: ", float(salary))
