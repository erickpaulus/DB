import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host="your_host",            #change your_host"
    user="your_username",        #change your_username"
    password="your_password",    #change your_password"
    database="your_database_name"    #change your_database_name"
)

if conn.is_connected():
    print("Successfully connected to the database")
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute a query
    cursor.execute("SELECT * FROM your_table_name")
    
    # Fetch all rows from the executed query
    rows = cursor.fetchall()
    
    # Loop through the rows and print them
    for row in rows:
        print(row)
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
else:
    print("Failed to connect to the database")
