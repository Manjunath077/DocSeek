# Default package
import calendar
from datetime import datetime

# External imports
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from mysql_connector import save_data, get_data, get_periods
from streamlit_extras.let_it_rain import rain

# ----------  Settings ------------
incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Savings"]
currency = "Rupees"
# page config
page_title = "Income and Expenses Tracker"
page_icon = ":money_with_wings:"
layout = "centered"  # can also changed to "wide"

#--------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

#-------- drop down values for selecting the period ---------
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

#--------streamlit style-----------
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """

st.markdown(hide_st_style, unsafe_allow_html=True)

#-------navigation menu------------
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],   # https://icons.getbootstrap.com
    orientation="horizontal",
)

#----------input and save periods----------
if selected == "Data Entry":
    st.header(f"Data Entry in {currency}")
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month:", months, key="month")
        col2.selectbox("Select Year:", years, key="year")

        "---"

        with st.expander("Income"):
            for income in incomes:
                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
        with st.expander("Comment"):
            comment = st.text_area("", placeholder="Enter a comment here ...", key="comment")

        "---"

        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            incomes = {income: st.session_state[income] for income in incomes}
            expenses = {expense: st.session_state[expense] for expense in expenses}
            comment = st.session_state["comment"]

            # Insert the values into the database
            save_data(period, incomes, expenses, comment)
            st.success("Data Saved !")


#------ plot graphs --------
if selected == "Data Visualization":
    st.header("Data Visualization")
    periods = get_periods()  # Fetch periods from the database

    with st.form("saved_periods"):
        period = st.selectbox("Select Period:", periods)  # Use fetched periods in the select box
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            # Get data for the selected period from the database
            period_data = get_data(period)  # Assuming get_data() returns the data for the selected period
            if period_data:  # Check if data is not empty
                # Extract data from the first row of the result
                first_row = period_data[0]  # Assuming period_data is a list of tuples
                comment = first_row[11]  # Assuming the comment is at index 11 in your database row
                expenses = {
                    "Rent": first_row[5],  # Assuming rent is at index 5 in your database row
                    "Utilities": first_row[6],  # Assuming utilities is at index 6
                    "Groceries": first_row[7],  # Assuming groceries is at index 7
                    "Car": first_row[8],  # Assuming car is at index 8
                    "Other Expenses": first_row[9],  # Assuming other_expenses is at index 9
                    "Savings": first_row[10],  # Assuming savings is at index 10
                }
                incomes = {
                    "Salary": first_row[2],  # Assuming salary is at index 2
                    "Blog": first_row[3],  # Assuming blog is at index 3
                    "Other Income": first_row[4],  # Assuming other_income is at index 4
                }

                # Convert values to integers or floats before summing
                incomes = {key: int(value) for key, value in incomes.items()}
                expenses = {key: int(value) for key, value in expenses.items()}

                # Create metrics
                total_income = sum(incomes.values())
                total_expense = sum(expenses.values())
                remaining_budget = total_income - total_expense
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Income", f"{total_income} {currency}")
                col2.metric("Total Expense", f"{total_expense} {currency}")
                col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
                st.text(f"Comment: {comment}")

                # Create sankey chart
                label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
                source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
                target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
                value = list(incomes.values()) + list(expenses.values())

                # Data to dict, dict to sankey
                link = dict(source=source, target=target, value=value)
                node = dict(label=label, pad=20, thickness=30, color="#E694FF")
                data = go.Sankey(link=link, node=node)

                # Plot it!
                fig = go.Figure(data)
                fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No data found for the selected period.")



# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

# Run snowfall animation
run_snow_animation()