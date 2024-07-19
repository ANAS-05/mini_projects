import streamlit as st
import google.generativeai as genai
import time

API_KEY = "YOUR_API_KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.logo("logo.jpg")
st.title("Interactive Text Generation using Google's Gemini AI")
st.markdown("***")

with st.chat_message("User"):
    topic = st.text_input("**Enter Topic**",placeholder="default value...")

st.write("### How many lines do you want the answer to be in:")
lines = st.slider('Number of lines',1,7)

st.selectbox("Model",['Gemini 1.0 Pro','Gemini 1.5 Pro','Gemini 1.5 Flash'])
language = st.selectbox("Language",['English','Hindi'])


def generate_content(topic,line,language):
    response = model.generate_content(f'Tell me about {topic} in {language} and {line} lines at max')
    with st.status("In progress...") as status:
        time.sleep(2)
        status.update(label = "Answer Generated")
    st.success(response.text)
    st.balloons()
    

if st.button("Generate"):
    generate_content(topic,lines,language)
