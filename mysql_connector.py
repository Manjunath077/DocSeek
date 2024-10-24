import mysql.connector

# Global variables for connection and cursor
conn = None
cursor = None

# Function to connect to MySQL
def connect_to_mysql():
    global conn, cursor
    if not conn:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="income_expenses_db"  # Replace with your database name
        )
    if not cursor:
        cursor = conn.cursor()

# Function to close the database connection
def close_connection():
    global conn, cursor
    if cursor:
        cursor.close()
    if conn:
        conn.close()

# Function to save data to MySQL
def save_data(period, incomes, expenses, comment):
    global cursor, conn
    if not cursor:
        connect_to_mysql()  # Reconnect if cursor is not connected
    try:
        insert_query = """
        INSERT INTO financial_data (period, salary, blog, other_income, rent, utilities, groceries, car, other_expenses, savings, comment)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            period,
            incomes["Salary"],
            incomes["Blog"],
            incomes["Other Income"],
            expenses["Rent"],
            expenses["Utilities"],
            expenses["Groceries"],
            expenses["Car"],
            expenses["Other Expenses"],
            expenses["Savings"],
            comment,
        )
        cursor.execute(insert_query, values)
        conn.commit()  # Commit changes to the database
    except Exception as e:
        print(f"Error saving data: {e}")

# Function to retrieve data from MySQL
def get_data(period):
    global cursor, conn
    if not cursor:
        connect_to_mysql()  # Reconnect if cursor is not connected
    try:
        select_query = f"""
        SELECT * FROM financial_data
        WHERE period = '{period}';
        """
        cursor.execute(select_query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

# Function to fetch distinct periods from MySQL
def get_periods():
    global cursor, conn
    if not cursor:
        connect_to_mysql()  # Reconnect if cursor is not connected
    try:
        if cursor:
            cursor.execute("SELECT DISTINCT period FROM financial_data ORDER BY period ASC;")
            periods = [row[0] for row in cursor.fetchall()]  # Fetch all distinct periods and store them in a list
            return periods
        else:
            raise Exception("Cursor is not connected.")
    except Exception as e:
        print(f"Error fetching periods: {e}")
        return []


