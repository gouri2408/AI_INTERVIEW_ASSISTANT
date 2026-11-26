import streamlit as st
from groq import Groq

st.set_page_config(page_title='AI Interview Assistant',layout='centered')
st.title('AI Interview Assistant')
st.caption('practice interview with ai generated question and constructive feedback.')
st.caption('Assist by Gouri Vanarase')

try:
  client = Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection successful")
except (KeyError, FileNotFoundError):
  st.error('GROQ_API_KEY is missing. add it to streamlit cloud -> app setting secrets')
  st.stop()

role =st.selectbox("Select Job Role",[
   "Python Developer",
   "Java Developer",
   "Data Analyst",
   "Machine Learning Engineer",
   "Software Engineering",
   "HR Executive"
])

diff=st.selectbox("Diffculty level",[
   "Beginer",
   "Intermediate",
   "Advanced"
])

if st.button("GEnerate Interview Question"):
   prompt = "Generate 5 interview questions for the role of " + role + "with" + diff + "diffculty"
   response = client.chat.completions.create(
       model="openai/gpt-oss-120b",
       messages=[
                {"role":"system","content":"you are an expert technical Interviewr"},
               {"role":"user","content":prompt}
       ]
   )

   output = response.choices[0].message.content
   st.write(output)
