import os
import pandas as pd
import mysql.connector
import logging

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DBNAME = os.environ.get('DBNAME')

def read_data(filename):
    '''Loads the CSV into a pandas DataFrame.'''
    try: 
        data = pd.read_csv(filename) #read the csv file
        logging.info("Successfully read data from %s", filename) #logging
        return data
    except Exception as error:
        logging.error("Error reading data: %s", error)
        raise


def clean_data(data):
    '''Removes rows with missing values, and returns the cleaned DataFrame.'''
    try:
        data = data.dropna() #drop rows
        logging.info("Successfully cleaned data") #logging
        return data
    except Exception as error:
        logging.error("Error cleaning data: %s", error)
        raise


def load_data(data, table):
    '''A function load_data that writes the Dataframe to MySQL'''
    connection = None
    cursor = None
    try:
        #connect to MySQL
        connection = mysql.connector.connect(
            host="ds2022.cgls84scuy1e.us-east-1.rds.amazonaws.com",
            port=3306,
            user="nky7nt",
            password="nky7nt",
            database="nky7nt_mock"
        )

        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS mock")
        
        #create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mock (
                id BIGINT,
                `group` VARCHAR(255),
                last_name VARCHAR(255),
                email VARCHAR(255),
                gender VARCHAR(255),
                ip_address VARCHAR(255)
            )
        """)

        #insert each row of the df
        insert_query = """
            INSERT INTO mock (id, `group`, last_name, email, gender, ip_address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        for row in data.itertuples(index=False, name=None):
            cursor.execute(insert_query, row)

        #save changes
        connection.commit()
        logging.info("data uploaded successfully!")

    except mysql.connector.Error as error:
        logging.error(f"error uploading data: {error}")

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

def main(): #read all functions
    data = read_data("mock_data.csv")
    data = clean_data(data)
    load_data(data, "mock")

if __name__ == "__main__":
    main()