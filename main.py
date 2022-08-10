from distutils.log import error
import requests
import configparser
import pandas as pd
import json

def apiAccess(KEY, URL, params):
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

def getData(KEY, df, URL, name):
    for i in range(0, 20000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        if df_tmp is not False:
            df = pd.concat([df, df_tmp])
    print(f"Saved! csv/{name}")
    df.to_csv(f"csv/{name}")

def getDataMaster(KEY, df, URL, name, masterName, idName, id):
    df_master = pd.read_csv(masterName)
    URL = URL
    name = name
    for value in df_master[id]:
        for i in range(0, 10000, 1000):
            params = {
                "offset": f"{i}",
                idName: value
            }
            df_tmp  = apiAccess(KEY, URL, params)
            if df_tmp is not False:
                df = pd.concat([df, df_tmp])
        print(f"Processing id: {value} len(df)={len(df)}")
    print(f"Saved! csv/{name}")
    df.to_csv(f"csv/{name}")

def main():

    config = configparser.ConfigParser()
    config.read("credentials.ini")

    KEY = config["API"]["KEY"]
    df = pd.DataFrame()
    
    with open("dictAPI.txt") as f:
        data = f.read()
      
    dictAPI = json.loads(data)
    print("Getting Data...")
    for x in dictAPI.values():
        getData(KEY, df, x['URL'], x['NAME'])
    print("Finished")
    
    with open("dictMaster.txt") as f:
        data = f.read()
      
    dictAPI = json.loads(data)
    print("Getting Data Master...")
    for x in dictAPI.values():
        getDataMaster(KEY, df, x['URL'], x['NAME'], x["MASTERNAME"], x["IDNAME"], x["ID"])
    
    print("Finished")
    

if __name__ == "__main__":
    main()