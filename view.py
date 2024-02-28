import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('medium_posts_meta_data.db')

# Execute a SELECT statement to retrieve the data
data = pd.read_sql_query("SELECT * FROM meta_data", conn)

# Close the connection
conn.close()

# Print the data in a tabular format
print(data)
