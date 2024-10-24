# import streamlit as st


# st.title("Analyse CSV")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit interface
def main():
    st.title("Interactive CSV Analysis App")

    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Display uploaded data
        # st.write("Uploaded Data:")
        # st.write(df)

        # Plotting options
        plot_options = st.selectbox("Select Plot Type", ["Bar Chart", "Pie Chart", "Line Chart", "Scatter Plot"])
        if plot_options == "Scatter Plot":
            x_column = st.selectbox("Select X-axis", df.columns)
            y_column = st.selectbox("Select Y-axis", df.columns)
            if st.button("Plot"):
                if x_column and y_column:
                    fig, ax = plt.subplots()
                    ax.scatter(df[x_column], df[y_column])
                    ax.set_xlabel(x_column)
                    ax.set_ylabel(y_column)
                    st.pyplot(fig)
        else:
            x_column = st.selectbox("Select X-axis", df.columns)
            y_column = st.selectbox("Select Y-axis", df.columns)
            if st.button("Plot"):
                if x_column and y_column:
                    fig, ax = plt.subplots()
                    if plot_options == "Bar Chart":
                        ax.bar(df[x_column], df[y_column])
                    elif plot_options == "Pie Chart":
                        ax.pie(df[y_column], labels=df[x_column], autopct='%1.1f%%')
                    elif plot_options == "Line Chart":
                        ax.plot(df[x_column], df[y_column])
                    elif plot_options == "Histogram":
                        ax.hist(df[y_column])
                    
                    ax.set_xlabel(x_column)
                    ax.set_ylabel(y_column)
                    st.pyplot(fig)

if __name__ == "__main__":
    main()
