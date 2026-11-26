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
