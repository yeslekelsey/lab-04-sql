import os
import pandas as pd
import mysql.connector
import logging
import matplotlib.pyplot as plt

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DBNAME = os.environ.get('DBNAME')

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DBNAME)
cur = db.cursor()

def get_data_by_group(value):
    """Return MOCK_DATA rows whose last_name matches ``value`` (list of tuples)."""
    query = "SELECT * FROM MOCK WHERE `group` = %s;"
    try:
        cur.execute(query, (value,))
        results = cur.fetchall()
        output = []
        for r in results:
            output.append(r)
        return output
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        return None

def plot_counts(groupby):
    """Count rows per distinct value of specified column, show a bar chart, and return the DataFrame."""
    allowed_columns = [
        "id",
        "group",
        "last_name",
        "email",
        "gender",
        "ip_address"
    ]

    if groupby not in allowed_columns:
        raise ValueError("Invalid column name")
    
    query = f"SELECT `{groupby}`, COUNT(`{groupby}`) FROM mock GROUP BY `{groupby}`;"
    try:
        cur.execute(query)
        results = cur.fetchall()
        output = []
        for r in results:
            output.append(r)
        df = pd.DataFrame(output)
        df.plot.bar(x=0, y=1)
        plt.tight_layout()
        plt.show()
        return df
    except mysql.connector.Error as e:
        print("MySQL Error: ", str(e))
        return None

def main():
    print("=== rows in group A ===")
    group_results = get_data_by_group("Group A")
    print(group_results)

    print("=== counts by gender ===")
    counts = plot_counts("gender")
    print(counts)

if __name__ == "__main__":
    main()