from db.database import get_connection
import pandas as pd

def create_data_frame(query):
    conn = get_connection()

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

