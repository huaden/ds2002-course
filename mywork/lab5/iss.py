#!/Users/haydenrobinette/miniforge3/envs/ds2002/bin/python3
import os
import json
import sys
import pandas as pd
import logging
import requests
import time
import mysql.connector


# db config stuff
DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DB = "iss"

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"
jsonFile = "TEMP_JSON_DUMP"


def get_connection():
    """Create and return a database connection."""
    return mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)


def register_reporter(table='reporters', reporter_id='xyb9vz', reporter_name='Hayden Robinette'):
    """Register reporter in DB if not already present."""
    logging.info(f"Checking if reporter '{reporter_id}' exists in {table}...")
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()


        select_query = f"SELECT * FROM {table} WHERE reporter_id = %s"
        recordData = (reporter_id,)
        cursor.execute(select_query, recordData)
        results = cursor.fetchall()

        if len(results) == 0:
            insert_query = f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)"
            recordData = (reporter_id, reporter_name)
            cursor.execute(insert_query, recordData)
            db.commit()
            logging.info(f"Reporter '{reporter_id}' registered successfully.")
        else:
            logging.info(f"Reporter '{reporter_id}' already exists")



    except Exception as e:
        logging.error(f"Error in register_reporter: {e}")
    finally:
        if cursor: cursor.close()
        if db: db.close()



def extract(url):
    """Fetch ISS data from the API and return JSON data."""
    logging.info(f"Getting data from {url}")
    data = None

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        logging.info(f"Extracted raw data and saved as json data")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"A request error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    return data



def transform(data, selected=["timestamp", "latitude", "longitude", "message"]):
    """Transform the JSON data into a clean single-row DataFrame."""


    logging.info("Cleaning and organizing data...")
    
    logging.info("Flattening nested structure...")
    df = pd.json_normalize(data)
    df.columns = df.columns.str.replace('iss_position.', '', regex=False)

    df = df[selected]
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s").dt.strftime("%Y-%m-%d %H:%M:%S")
    logging.debug(f"Selected columns: {selected}")
    df_clean = df.reset_index(drop=True)


    logging.info(f"Transformed: {df_clean.shape[0]} rows × {df_clean.shape[1]} columns")
    
    return df_clean





def load(df, reporter_id='xyb9vz'):
    """ Load: Save transformed data to database """
    logging.info(f"Loading data into the database")
    db = None
    cursor = None
    try:
        db = get_connection()
        cursor = db.cursor()

        insertQuery = "INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id) VALUES (%s, %s, %s, %s, %s)"
        for i, row in df.iterrows():
            recordData = (
                row["message"],
                row["latitude"],
                row["longitude"],
                row["timestamp"],
                reporter_id
            )
            cursor.execute(insertQuery, recordData)
        
        db.commit()
        logging.info(f"Inserted {len(df)} record(s) into locations.")



    except Exception as e:
        logging.error(f"Error in loading data into database: {e}")
    finally:
        if cursor: cursor.close()
        if db: db.close()







def main():
    """Run the complete ETL pipeline."""

    logging.info("ISS Pipeline Lab4")
    register_reporter(reporter_id='xyb9vz', reporter_name='Hayden Robinette')

    data = extract(URL)
    if data is None:
        logging.error("Extraction failed, exitting program")
        sys.exit(1)

    df = transform(data)
    load(df, 'xyb9vz')
    logging.info(f"Processed {len(df)} records")



if __name__ == "__main__":
        main()
