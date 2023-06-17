import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from langchain.memory import ConversationBufferMemory

import streamlit as st


config = load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

st.title("LangChain Demo - OpenAPI")
input_text = st.text_input("Search topic...")

first_input_prompt = PromptTemplate(
    input_variables=["fighter"], template="Tell me about MMA fighter {fighter}."
)

# Memory management
fighter_memory = ConversationBufferMemory(
    input_key="fighter", memory_key="chat_history"
)
dob_memory = ConversationBufferMemory(input_key="person", memory_key="chat_history")

events_memory = ConversationBufferMemory(
    input_key="dob", memory_key="description_history"
)

llm = OpenAI(temperature=0.8)

chain = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key="person",
    memory=fighter_memory,
)

second_input_prompt = PromptTemplate(
    input_variables=["fighter"], template="When was the date that {fighter} was born?"
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
    input_variables=["fighter"],
    output_variables=["person", "dob", "events"],
    verbose=True,
)

if input_text:
    st.write(parent_chain({"fighter": input_text}))

    with st.expander("Fighter Name"):
        st.info(fighter_memory.buffer)

    with st.expander("Events"):
        st.info(events_memory.buffer)
