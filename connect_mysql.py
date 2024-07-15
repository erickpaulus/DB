import mysql.connector
import configparser

# Parse the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve the credentials from the configuration file
db_config = {
    'host': config['mysql']['host'],
    'user': config['mysql']['user'],
    'password': config['mysql']['password'],
    'database': config['mysql']['database']
}

# Establish the connection
conn = mysql.connector.connect(**db_config)

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
