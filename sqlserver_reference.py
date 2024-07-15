import pyodbc

# Define the connection string
connection_string = (
    "Driver={SQL Server};"
    "Server=your_server_name;"
    "Database=your_database_name;"
    "UID=your_username;"
    "PWD=your_password;"
)

# Establish the connection
conn = pyodbc.connect(connection_string)

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
