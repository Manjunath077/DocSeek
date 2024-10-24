# import streamlit as st


# st.title("Chat with pdf")


import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import faiss
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI 
from langchain_community.callbacks.manager import get_openai_callback


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat With pdf")
    st.header("Ask Your PDF 💬")

    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf is not None:
        try:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            # split into chunks
            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=100,
                length_function=len
            )
            chunks = text_splitter.split_text(text)

            # create embeddings
            embeddings = OpenAIEmbeddings()
            knowledge_base = faiss.FAISS.from_texts(chunks, embeddings)

            # show user input 
            user_question = st.text_input("Ask Your Pdf :")
            if user_question:
                docs = knowledge_base.similarity_search(user_question)

                llm = OpenAI()
                chain = load_qa_chain(llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(input_documents=docs, question=user_question)
                    print(cb)

                st.write(response)

        except Exception as e:
            st.error("try again .")
            # Log the error if needed
            print(e)




if __name__ == '__main__':
    main()