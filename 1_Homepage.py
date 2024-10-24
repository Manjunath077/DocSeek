import streamlit as st
from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
st.set_page_config(
    page_title="DocSeek",
    page_icon="📚",
)

# st.title("Main Page")
# st.sidebar.success("Select a page above.")

# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)




# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_ai.json"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")


# # Function to get the name from query parameters
# def get_person_name():
#     query_params = st.experimental_get_query_params()
#     return query_params.get("name", ["Friend"])[0]


# # Page configuration
# st.set_page_config(page_title="Home", page_icon="🏠")

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display header with personalized name
# PERSON_NAME = get_person_name()
st.header(f"Hi There!, ✨", anchor=False)

# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=300)

# # Personalized holiday message
st.markdown(
    f"Welcome to a Personalized Web App. 🌟"
)



