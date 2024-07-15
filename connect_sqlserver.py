import pyodbc
import configparser

# Parse the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve the credentials from the configuration file
db_config = {
    'driver': config['sqlserver']['driver'],
    'server': config['sqlserver']['server'],
    'database': config['sqlserver']['database'],
    'uid': config['sqlserver']['uid'],
    'pwd': config['sqlserver']['pwd']
}

# Format the connection string
connection_string = (
    f"Driver={db_config['driver']};"
    f"Server={db_config['server']};"
    f"Database={db_config['database']};"
    f"UID={db_config['uid']};"
    f"PWD={db_config['pwd']};"
)

# Establish the connection
conn = pyodbc.connect(connection_string)

if conn:
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
