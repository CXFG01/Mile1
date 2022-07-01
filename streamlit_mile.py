import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Heart Prediction", layout="wide")
st.header("Heart Disease App")

def start():
	st.markdown(""" <p style="font-size: 22px;">Please answer the questions below: </p>""", unsafe_allow_html=True)
	st.markdown(""" <p style="font-size: 22px;">What is your BMI? </p>""", unsafe_allow_html=True)
	BMI= st.number_input("Insert BMI",min_value=10.000, max_value=100.000)
	
	st.markdown(""" <p style="font-size: 22px;">Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]</p>""", unsafe_allow_html=True)
	Smoking= st.selectbox("Select your answer", ("No", "Yes"))
	
	


if st.button("Proceed", on_click=start()):
	st.markdown(""" """)
else:
	st.markdown("""
	<p style="font-size: 22px;">Hey there! </p>
	
	<p style="font-size: 22px;">This app here uses the power of machine learning(traditional and neural) to help predict the affliction of an individual with Coronary Heart Disease or Myocardial Infraction(Heart Attack). </p>
	<p style="font-size: 28px;"><b>
	By no means is this a medical tool and only a certified doctor can inquire further in your problem.
	Irrelevant of the result, have periodic visits at the doctor to know more about the body's condition.
	</b></p>
	
	<p style="font-size: 22px;">Now, let's see what the AI says about your situation! (Press Proceed at the top) </p>
	""", unsafe_allow_html=True)
  

