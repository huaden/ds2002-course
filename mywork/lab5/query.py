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



def get_connection():
    """Create and return a database connection."""
    return mysql.connector.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DB)

db = get_connection()
cursor = db.cursor()

query = """
        SELECT * 
        FROM reporters r
        JOIN locations l ON r.reporter_id = l.reporter_id
        WHERE r.reporter_id = "xyb9vz"
        """
cursor.execute(query)
results = cursor.fetchall()
for result in results:
    print(result)