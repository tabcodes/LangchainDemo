import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from langchain.memory import ConversationBufferMemory

import streamlit as st


config = load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.title("LangChain Demo")
st.header("UFC Fighter Lookup")

input_text = st.text_input("Enter the name of an MMA fighter...")

first_input_prompt = PromptTemplate(
    input_variables=["name"], template="Tell me about MMA fighter {name}."
)

# Memory management
fighter_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")

dob_memory = ConversationBufferMemory(input_key="name", memory_key="chat_history")

events_memory = ConversationBufferMemory(
    input_key="dob", memory_key="description_history"
)

llm = OpenAI(temperature=0.8)

chain = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key="fighter",
    memory=fighter_memory,
)

second_input_prompt = PromptTemplate(
    input_variables=["name"], template="Give me only the date that {name} was born."
)

chain2 = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key="dob",
    memory=dob_memory,
)

third_input_prompt = PromptTemplate(
    input_variables=["dob"],
    template="Mention 5 major events that happened around {dob} in the world.",
)

chain3 = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key="events",
    memory=events_memory,
)


parent_chain = SequentialChain(
    chains=[chain, chain2, chain3],
    input_variables=["name"],
    output_variables=["fighter", "dob", "events"],
    verbose=True,
)

if input_text:
    st.write(parent_chain({"name": input_text}))

    with st.expander("Fighter Name", True):
        st.info(fighter_memory.buffer)

    with st.expander("Date of Birth", True):
        st.info(dob_memory.buffer)

    with st.expander("Events", True):
        st.info(events_memory.buffer)
