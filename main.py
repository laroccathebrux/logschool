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
        print(j)

    return df_tmp

def getData(KEY, df, config, URL, name):

    for i in range(0, 1000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        df = pd.concat([df_tmp, df])
    print(f"{name} Saved!")
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
        getData(KEY, df, config, x['URL'], x['NAME'])
    print("Finished")

if __name__ == "__main__":
    main()