import os
from constants import openai_key
from langchain_openai import OpenAI
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationSummaryBufferMemory

# Set your API key
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit UI
st.title("Celebrity Search")
input_text = st.text_input("Search Topic")

# Shared LLM
llm = OpenAI(temperature=0.8)

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me something about {name}"
)

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born"
)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events that happened around {dob} in the world"
)

# Memory
person_memory = ConversationSummaryBufferMemory(llm=llm, input_key='name', memory_key='chat_history')
dob_memory = ConversationSummaryBufferMemory(llm=llm, input_key='person', memory_key='chat_history')
events_memory = ConversationSummaryBufferMemory(llm=llm, input_key='dob', memory_key='chat_history')

# Chains
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='events', memory=events_memory)

# Sequential chain
Super_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'events'],
    verbose=True
)

# Run app
if input_text:
    output = Super_chain({'name': input_text})
    st.write(output)

    with st.expander('Person Info'):
        st.info(person_memory.buffer)

    with st.expander('Date of Birth'):
        st.info(dob_memory.buffer)

    with st.expander('Major Events'):
        st.info(events_memory.buffer)
