import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
st.markdown(response.text)
