import os
from constants import openai_key
# from langchain.llms import OpenAI
from langchain_openai import OpenAI
# from langchain_community.llms import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"]=openai_key

## Streamlit framework

st.title("Streamlit Demo with OpenAI")
input_text = st.text_input("Seach Topic")

## OpenAI LLMs

llm = OpenAI(temperature = 0.8)

if input_text:
    st.write(llm.invoke(input_text))

