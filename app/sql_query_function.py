import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env
load_dotenv()


def fetch_query_records(query):
    """
    Creates a connection to database, returns query from specified table.
    Input: query: a SQL query (string)
    Returns: response: cursor.fetchall() object in array form
    """
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Creating Connection Object
    conn= psycopg2.connect(DATABASE_URL)

    
    # Creating Cursor Object
    cursor = conn.cursor()
    # Execute query
    cursor.execute(query)
    # Query results
    response = list(cursor.fetchall())
    # Closing Connection
    conn.close()

    return response


def fetch_query(query, columns):
    """
    Creates a connection to database, returns query from specified table
    as a list of dictionaries.
    Input: query: a SQL query (string)
    Returns: pairs: dataframe of cursor.fetchall() response in JSON pairs
    """
    # Fetch query
    response = fetch_query_records(query)
    # List of tuples to DF
    df = pd.DataFrame(response, columns=columns)
    # DF to dictionary
    pairs = df.to_json(orient='records')
    return pairs