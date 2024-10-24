# import streamlit as st

# # st.title("Contact")


import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import openai
from langchain_openai import ChatOpenAI
#import openai
import os
from dotenv import load_dotenv





def main():
    
    load_dotenv()
    
    st.set_page_config(
        page_title="Ask your CSV ",
        page_icon=":chart:"
    )
    st.header("Ask Your CSV ")

    user_csv = st.file_uploader("Upload your csv file :",type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask Anything about the CSV !") 

        # llm = GPT(temperature=0)
        # llm = openai(temperature=0)

        # Set up the OpenAI API key
        # openai.api_key = "YOUR_OPENAI_API_KEY"

        # Create a completion object with your desired parameters
        # llm = openai.Completion.create(engine="gpt-3.5-turbo-1106", temperature=0)
        # llm = openai.Completion.create(engine="babbage-002", temperature=0)

        # llm = OpenAI(temperature=0)
        # llm = openai.Completion.create(engine="", temperature=0)
        # agent = create_csv_agent(llm,user_csv,verbose=True)

        openai.api_key = os.getenv("OPENAI_API_KEY")

        llm = ChatOpenAI(model="babbage-002",temperature=0)

        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        agent_executor = create_csv_agent(
            llm,
            user_csv,
            agent_type="openai-tools",
            verbose=True
        )
        if user_question is not None and user_question !="":
            response = agent_executor.run(user_question)
            st.write(response)



if __name__ == "__main__":
    main()

