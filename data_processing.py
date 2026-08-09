from database import get_connection
import pandas as pd

query = """"
SELECT *
FROM user
"""

def create_data_frame(query):
    conn = get_connection()

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

