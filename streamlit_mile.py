import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Heart Prediction", layout="wide")
st.header("Heart Disease App")
k=0
def add(n):
	n=n+1

def start():
	with st.form(key='form1'):
		st.markdown(""" <p style="font-size: 22px;">Please answer the questions below: </p>""", unsafe_allow_html=True)
		st.markdown(""" <p style="font-size: 22px;">What is your BMI? </p>""", unsafe_allow_html=True)
		BMI= st.number_input("Insert BMI",min_value=10.000, max_value=100.000, key=1, on_change=add(k))
	
		st.markdown(""" <p style="font-size: 22px;">Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]</p>""", unsafe_allow_html=True)
		Smoking= st.selectbox("Select your answer", ("No", "Yes"), key=2)
	
		st.markdown(""" <p style="font-size: 22px;">Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week</p>""", unsafe_allow_html=True)
		AlcoholDrinking= st.selectbox("Select your answer", ("Not a heavy drinker", "A heavy drinker"), key=3)
	
		st.markdown(""" <p style="font-size: 22px;">Told/had a stroke?</p>""", unsafe_allow_html=True)
		Stroke= st.selectbox("Select your answer", ("No i have not", "Yes i have"), key=4)
	
		st.markdown(""" <p style="font-size: 22px;">Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days)</p>""", unsafe_allow_html=True)
		PhysicalHealth= st.number_input("Insert days",min_value=0.00, max_value=30.00, key=5)
	
		st.markdown(""" <p style="font-size: 22px;">Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days)</p>""", unsafe_allow_html=True)
		MentalHealth= st.number_input("Insert days",min_value=0.00, max_value=30.00, key=6)
	
		st.markdown(""" <p style="font-size: 22px;">Do you have serious difficulty walking or climbing stairs?</p>""", unsafe_allow_html=True)
		DiffWalking= st.selectbox("Select your answer", ("No i do not", "Yes I do"), key=7)
	
		st.markdown(""" <p style="font-size: 22px;">Are you male or female?</p>""", unsafe_allow_html=True)
		Sex= st.selectbox("Select your answer", ("Female", "Male"), key=8)
	
		st.markdown(""" <p style="font-size: 22px;">In what age category do you fit in?</p>""", unsafe_allow_html=True)
		AgeCategory = st.selectbox("Select your answer", ("18-24", "25-29","30-34","35-39","40-44","45-59","50-54","55-59","60-64","65-69","70-74","75-79","80 or older"), key=9)
	
		results=BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, AgeCategory
		if st.form_submit_button(label='Submit'):
			return results
if st.button("Proceed", key='pro'):
	m=str(start())
	st.write(m)
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
  

