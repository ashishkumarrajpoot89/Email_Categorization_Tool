# import mysql.connector

# def insert_feedback(email_text, predicted_category, actual_category):
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="AKR00007akr&",  # Change to your MySQL password
#         database="email_tool"
#     )
#     cursor = conn.cursor()
#     query = "INSERT INTO feedback (email_text, predicted_category, actual_category) VALUES (%s, %s, %s)"
#     cursor.execute(query, (email_text, predicted_category, actual_category))
#     conn.commit()
#     conn.close()



# import mysql.connector

# try:
#     # Try connecting to the database
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="AKR00007akr&",  # Change to your MySQL password
#         database="email_tool"
#     )

#     if conn.is_connected():
#         print("✅ Successfully connected to MySQL Workbench!")
#         db_info = conn.get_server_info()
#         print(f"MySQL Server version: {db_info}")

# except mysql.connector.Error as e:
#     print(f"❌ Error connecting to MySQL: {e}")

# finally:
#     if 'conn' in locals() and conn.is_connected():
#         conn.close()
#         print("🔌 Connection closed.")


import mysql.connector
from mysql.connector import Error

# Function to connect to MySQL
def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",       # Change if not local
            user="root",            # Your MySQL username
            password="AKR00007akr&",  # Your MySQL password
            database="email_tool"   # Your database name
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"❌ Error connecting to MySQL: {e}")
        return None

# Function to insert feedback
def insert_feedback(email_text, predicted_category, actual_category):
    conn = create_connection()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO feedback (email_text, predicted_category, actual_category)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (email_text, predicted_category, actual_category))
        conn.commit()
        print("✅ Feedback saved to MySQL!")
    except Error as e:
        print(f"❌ Error inserting feedback: {e}")
    finally:
        cursor.close()
        conn.close()

# Test the connection (optional)
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        print("✅ Successfully connected to MySQL!")
        print("MySQL Server version:", conn.get_server_info())
        conn.close()

