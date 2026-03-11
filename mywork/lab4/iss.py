#!/Users/haydenrobinette/miniforge3/envs/ds2002/bin/python3
import sys
import os
import json
import pandas as pd
import logging
import requests
import time


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"
jsonFile = "TEMP_JSON_DUMP"

def parse_args():
    """ Look through arguments for provided csv file, log an error otherwise """
    try:
        outputCSV = sys.argv[1]
    except IndexError:
        logging.error(f"Usage: python {sys.argv[0]} <csv_file>")
        sys.exit(1)
    return outputCSV




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



def transform(data, selected=["timestamp", "latitude", "longitude"]):
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





def load(df, csvFile):
    """
    Load: Save transformed data to CSV and display summary.
          Additionally, add the data to the existing CSV if it is already there
    """
    if os.path.exists(csvFile):
        current = pd.read_csv(csvFile)
        combine = pd.concat([current, df], ignore_index=True)
        combine.to_csv(csvFile, index=False)
        logging.info(f"Appended record ({len(combine)} total rows) to {csvFile}")

    else:
        df.to_csv(csvFile, index=False)
        logging.info(f"Loaded transformed data (saved to {csvFile})")






def main():
    """Run the complete ETL pipeline."""

    logging.info("ISS Pipeline Lab4")

    
    csvFile = parse_args()

    data = extract(URL)
    if data is None:
        logging.error("Extraction failed, exitting program")
        sys.exit(1)

    df = transform(data)
    load(df, csvFile)
    logging.info(f"Processed {len(df)} records")



if __name__ == "__main__":
        main()
