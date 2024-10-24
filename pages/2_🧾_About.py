import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

import json

# Function to load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load Lottie animations
lottie_csv = load_lottiefile("assets/csv_animation.json")
lottie_analyze = load_lottiefile("assets/analyze_animation.json")
lottie_pdf = load_lottiefile("assets/pdf_animation.json")
lottie_salary = load_lottiefile("assets/salary_animation.json")
lottie_gpt = load_lottiefile("assets/gpt_animation.json")

# Streamlit page configuration
st.set_page_config(page_title="About Project", page_icon="📊", layout="wide")


st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            padding-left: 50%;
        }
    </style>
""",unsafe_allow_html=True)


# About the Project
st.title("About the Project")

st.markdown("""
Welcome to our comprehensive data interaction and visualization suite built with Python and Streamlit. This project consists of five distinct modules, each designed to provide tools for querying, analyzing, and visualizing data.
""")

# Chat with CSV
st.header("Chat with CSV")
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_csv, height=200, key="csv")
with col2:
    st.markdown("""
    Upload a CSV file and ask questions directly related to its contents. This module processes your data and provides answers based on the uploaded CSV.
    """)

# Gap after Chat with CSV
st.markdown("---")

# Analyze CSV
st.header("Analyze CSV")
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_analyze, height=200, key="analyze")
with col2:
    st.markdown("""
    Upload a CSV file and analyze it through interactive graphs and plots. This module helps in visualizing data trends and patterns for better insights.
    """)

# Gap after Analyze CSV
st.markdown("---")

# Chat with PDF
st.header("Chat with PDF")
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_pdf, height=200, key="pdf")
with col2:
    st.markdown("""
    Upload a PDF document and ask questions about its content. This module extracts text from the PDF and provides answers based on the information within the document.
    """)

# Gap after Chat with PDF
st.markdown("---")

# Salary Analyzer
st.header("Salary Analyzer")
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_salary, height=200, key="salary")
with col2:
    st.markdown("""
    Input your income and expense data to generate a Sankey chart, visualizing the flow of your finances and helping you understand your financial situation better.
    """)

# Gap after Salary Analyzer
st.markdown("---")

# GPT Clone
st.header("Generative AI")
col1, col2 = st.columns([1, 3])
with col1:
    st_lottie(lottie_gpt, height=200, key="gpt")
with col2:
    st.markdown("""
    Utilize the power of the Chat GPT Model to ask any type of question. This module provides versatile and possible responses, showcasing advanced natural language processing capabilities.
    """)

# Final gap before the ending paragraph
# st.markdown("---")

# st.markdown("""
# Each module integrates powerful Python libraries such as Pandas, Matplotlib, Plotly, and the OpenAI GPT API, demonstrating the potential of Streamlit in creating user-friendly web applications.
# """)



    
# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

# Run snowfall animation
run_snow_animation()
