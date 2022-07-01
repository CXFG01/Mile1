import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Heart Prediction", layout="wide")
st.header("Heart Disease App")

st.markdown("""

Hey there!

<p style="font-size: 22px;">This app here uses the power of machine learning(traditional and neural) to help predict the affliction of an individual with Coronary Heart Disease or Myocardial Infraction(Heart Attack). </p>

# By no means is this a medical tool and only a certified doctor can inquire further in your problem.
# Irrelevant of the result, have periodic visits at the doctor to know more about the body's condition.

""", unsafe_allow_html=True)
