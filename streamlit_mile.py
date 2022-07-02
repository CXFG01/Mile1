import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Heart Prediction", layout="wide")
st.header("Heart Disease App")
lis=list()
BMI=19

if 'k' not in st.session_state:
    st.session_state.k = 0

if 'm' not in st.session_state:
    st.session_state.m = list()

if 'state' not in st.session_state:
    st.session_state.state = 0

if 'form' not in st.session_state :
    st.session_state.form = 0

def add(value):
	lis.append(value)
	
def state():
	st.session_state.state = 1
	st.session_state.form = 1
	st.session_state.m=lis
	

def start():
	with st.form(key='form1'):
		st.markdown(""" <p style="font-size: 22px;">Please answer the questions below: </p>""", unsafe_allow_html=True)
		st.markdown(""" <p style="font-size: 22px;">What is your BMI? </p>""", unsafe_allow_html=True)
		BMI= st.number_input("Insert BMI",min_value=10.000, max_value=100.000, key=1)
		st.write(BMI)
	
		st.markdown(""" <p style="font-size: 22px;">Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]</p>""", unsafe_allow_html=True)
		Smoking= st.selectbox("Select your answer", ("No", "Yes"), key=2)

		
		st.markdown(""" <p style="font-size: 22px;">Are you a heavy drinker? (Adult men having more than 14 drinks per week and adult women having more than 7 drinks per week</p>""", unsafe_allow_html=True)
		AlcoholDrinking= st.selectbox("Select your answer", ("No", "Yes"), key=3)

		
		st.markdown(""" <p style="font-size: 22px;">Ever told/you had stroke?</p>""", unsafe_allow_html=True)
		Stroke= st.selectbox("Select your answer", ("No", "Yes"), key=4)

		
		st.markdown(""" <p style="font-size: 22px;">Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days)</p>""", unsafe_allow_html=True)
		PhysicalHealth= st.number_input("Insert days",min_value=0.00, max_value=30.00, key=5)

		
		st.markdown(""" <p style="font-size: 22px;">Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days)</p>""", unsafe_allow_html=True)
		MentalHealth= st.number_input("Insert days",min_value=0.00, max_value=30.00, key=6)

		
		st.markdown(""" <p style="font-size: 22px;">Do you have serious difficulty walking or climbing stairs?</p>""", unsafe_allow_html=True)
		DiffWalking= st.selectbox("Select your answer", ("No", "Yes"), key=7)

		
		st.markdown(""" <p style="font-size: 22px;">Are you male or female?</p>""", unsafe_allow_html=True)
		Sex= st.selectbox("Select your answer", ("Female", "Male"), key=8)

		
		st.markdown(""" <p style="font-size: 22px;">In what age category do you fit in?</p>""", unsafe_allow_html=True)
		AgeCategory = st.selectbox("Select your answer", ("18-24", "25-29","30-34","35-39","40-44","45-59","50-54","55-59","60-64","65-69","70-74","75-79","80 or older"), key=9)

		
		st.markdown(""" <p style="font-size: 22px;">Race</p>""", unsafe_allow_html=True)
		Race = st.selectbox("Select your answer", ('American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White'), key=10)

		
		st.markdown(""" <p style="font-size: 22px;">Ever Told/Had diabetes?p>""", unsafe_allow_html=True)
		Diabetic= st.selectbox("Select your answer", ('No', 'No, borderline diabetes', 'Yes', 'Yes (during pregnancy)'), key=11)

		
		st.markdown(""" <p style="font-size: 22px;">Have you been engaging in physical activity or exercise during the past 30 days other than your regular job</p>""", unsafe_allow_html=True)
		PhysicalActivity= st.selectbox("Select your answer", ('No','Yes'), key=12)

		
		st.markdown(""" <p style="font-size: 22px;">Would you say that in general your health is...</p>""", unsafe_allow_html=True)
		GenHealth= st.selectbox("Select your answer", ('Excellent','Very good' ,'Good', 'Fair', 'Poor'), key=13)

		
		st.markdown(""" <p style="font-size: 22px;">On average, how many hours of sleep do you get in a 24-hour period?</p>""", unsafe_allow_html=True)
		SleepTime = st.number_input("Time",min_value=1.00, max_value=24.00, key=14)

		
		st.markdown(""" <p style="font-size: 22px;">Ever told/you had asthma?</p>""", unsafe_allow_html=True)
		Asthma= st.selectbox("Select your answer", ("No", "Yes"), key=15)

		
		st.markdown(""" <p style="font-size: 22px;">Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?</p>""", unsafe_allow_html=True)
		KidneyDisease= st.selectbox("Select your answer", ("No", "Yes"), key=16)

		
		st.markdown(""" <p style="font-size: 22px;">Ever told/you had skin cancer?</p>""", unsafe_allow_html=True)
		SkinCancer = st.selectbox("Select your answer", ("No", "Yes"), key=17)

		
				
		st.form_submit_button(label='Submit', on_click=state())
			
def predict(results):
	st.write(results)

butt1=st.button("Proceed", key='pro', disabled=st.session_state.state)

if not butt1 and st.session_state.state==0:
	st.markdown("""
	<p style="font-size: 22px;">Hey there! </p>
	
	<p style="font-size: 22px;">This app here uses the power of machine learning(traditional and neural) to help predict the affliction of an individual with Coronary Heart Disease or Myocardial Infraction(Heart Attack). </p>
	<p style="font-size: 28px;"><b>
	By no means is this a medical tool and only a certified doctor can inquire further in your problem.
	Irrelevant of the result, have periodic visits at the doctor to know more about the body's condition.
	</b></p>
	
	<p style="font-size: 22px;">Now, let's see what the AI says about your situation! (Press Proceed at the top) </p>
	""", unsafe_allow_html=True)
	
elif butt1 and st.session_state.state==0 :
	start()
if st.session_state.state==1 and st.session_state.form==1 :
	st.write(BMI)
	#d = {'BMI': [st.session_state.m[0]],
	#	     'Smoking': [st.session_state.m[1]],
	#	     'AlchoholDrinking': [st.session_state.m[2]],
	#	     'Stroke': [st.session_state.m[3]],
	#	     'PhysicalHealth': [st.session_state.m[4]],
	#	     'MentalHealth': [st.session_state.m[5]],
	#	     'DiffWalking': [st.session_state.m[6]],
	#	     'Sex': [st.session_state.m[7]],
	#	     'AgeCategory': [st.session_state.m[8]],
	#	     'Race': [st.session_state.m[9]],
	#	     'Diabetic': [st.session_state.m[10]],
	#	     'PhysicalActivity': [st.session_state.m[11]],
	#	     'GenHealth':[st.session_state.m[12]],
	#	     'SleepTime': [st.session_state.m[13]],
	#	     'Asthma': [st.session_state.m[14]],
	#	     'KidneyDisease': [st.session_state.m[15]],
	#	     'SkinCancer': [st.session_state.m[16]]}
	#df = pd.DataFrame(data=d)
	#df
  

