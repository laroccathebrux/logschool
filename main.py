import requests
import configparser
import pandas as pd
import numpy as np
import json
from dotenv import load_dotenv
load_dotenv()
import cloudinary
import cloudinary.uploader
import cloudinary.api
import time
import create_tables
import psycopg2
import psycopg2.extras as extras
from sql_queries import insert_table_queries
import logging

def apiAccess(KEY, URL, params):
    """
    Connect to API

    Args:
        KEY (_String_): API Key
        URL (_String_): Endpoint URL
        params (_Dict_): Parameters for the API

    Returns:
        _Boolean_: df_tmp
    """
    headers = {
        "Accept": "application/json",
        "Authorization": f'Token token="{KEY}"'
    }

    r = requests.get(url=URL, headers=headers, params=params)
    j = r.json()
    
    df_tmp = pd.DataFrame()
    try:
        df_tmp = pd.DataFrame.from_dict(j)
    except ValueError:
        df_tmp = False

    return df_tmp

def getData(KEY, df, URL, name, table, conn, cur, logger):
    """
    Connect to API and get data
    Save data to csv

    Args:
        KEY (_String_): API Key
        df (_Dataframe_): Dataframe with data
        URL (_String_): Endpoint URL
        name (_String_): Name of the file
    """
    
    i = 0
    while True:
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        if df_tmp is not False:
            i = i + 1000
            df = pd.concat([df, df_tmp])
        else:
            break

    df = df.replace('\n', '', regex=True)
    df = df.replace('\u0000', '', regex=True)
    #df.to_csv(f"csv/{name}")

    tuples = [tuple(x) for x in df.to_numpy()]
    
    try:
        query = insert_table_queries[table]
        print(f"Insert table: {table}")
        extras.execute_batch(cur, query, tuples)
        conn.commit()
    except Exception as e:
        print(f"ERROR INSERTING DATA: {e.args}")
        logger.error(f"ERROR INSERTING DATA: {e.args}")
        logger.error(query)
        logger.error(tuples)
    """
    cloudinary.uploader.upload(f"csv/{name}", 
        folder = "csv/", 
        public_id = f"{name}",
        unique_filename = False,
        overwrite = True,
        resource_type = "auto")
    print(f"Cloudinary Saved! csv/{name}")
    """

def getDataMaster(KEY, df, URL, name, masterName, idName, id, table, conn, cur, logger):
    """
    Connect to API and get data
    Save data to csv

    Args:
        KEY (_String_): API Key
        df (_Dataframe_): Dataframe with data
        URL (_String_): Endpoint URL
        name (_String_): Name of the file
        masterName (_String_): Name of the master file
        idName (_String_): Name of the id
        id (_Int_):  Id
    """
    df_master = pd.read_csv(masterName)
    URL = URL
    name = name
    for value in df_master[id]:
        i = 0
        while True:
            params = {
                "offset": f"{i}",
                idName: value
            }
            df_tmp  = apiAccess(KEY, URL, params)
            if df_tmp is not False:
                i = i + 1000
                df = pd.concat([df, df_tmp])
            else:
                break
        print(f"Processing id: {value} len(df)={len(df)}")

    #df.to_csv(f"csv/{name}")

    tuples = [tuple(x) for x in df.to_numpy()]
    
    try:
        query = insert_table_queries[table]
        print(f"Insert table: {table}")
        extras.execute_batch(cur, query, tuples)
        conn.commit()
    except Exception as e:
        print(f"ERROR INSERTING DATA: {e.args}")
        logger.error(f"ERROR INSERTING DATA: {e.args}")
        logger.error(query)
        logger.error(tuples)
    """
    cloudinary.uploader.upload(f"csv/{name}", 
        folder = "csv/", 
        public_id = f"{name}",
        unique_filename = False,
        overwrite = True,
        resource_type = "auto")
    print(f"Cloudinary Saved! csv/{name}")
    """

def main():
    """
    Main function
    """
    start = time.time()
    config = configparser.ConfigParser()
    config.read("credentials.ini")

    logger = logging.getLogger('LOGSCHOOL')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('data.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    KEY = config["API"]["KEY"]

    create_tables.main()

    HOST = config["POSTGRES"]["HOST"]
    USER = config["POSTGRES"]["USER"]
    PASS = config["POSTGRES"]["PASS"]
    DB = config["POSTGRES"]["DB"]
    conn = psycopg2.connect(f"host={HOST} dbname={DB} user={USER} password={PASS}")
    cur = conn.cursor()

    cloudinary.config(secure = True)
    df = pd.DataFrame()
    
    with open("dictAPI.txt") as f:
        data = f.read()
      
    dictAPI = json.loads(data)
    print("Getting Data...")
    for x in dictAPI.values():
        getData(KEY, df, x['URL'], x['NAME'], x["TABLE"], conn, cur, logger)
    print("Finished")
    
    with open("dictMaster.txt") as f:
        data = f.read()
     
    dictAPI = json.loads(data)
    print("Getting Data Master...")
    for x in dictAPI.values():
        getDataMaster(KEY, df, x['URL'], x['NAME'], x["MASTERNAME"], x["IDNAME"], x["ID"], x["TABLE"], conn, cur, logger)
    
    end = time.time()
    
    spent = end-start
    
    print(f"Finished! Elipsed Time: {spent:.2f} s")
    

if __name__ == "__main__":
    main()