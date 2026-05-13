import os
import psycopg2
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Database connection parameters
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

# Create a cursor object
cur = conn.cursor()

# Execute the query to fetch all rows from the "loan" table
cur.execute("SELECT * FROM loan;")

# Fetch all rows from the result of the query
rows = cur.fetchall()

# Print the fetched rows
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()