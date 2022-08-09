from distutils.log import error
import requests
import configparser
import pandas as pd
from azure.storage.blob import BlobServiceClient

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

def getAzureAccess(config):
    ACCKEY  = config["AZURE"]["ACCKEY"]
    CONTAINER = config["AZURE"]["CONTAINER"]
    blob_service_client = BlobServiceClient.from_connection_string(ACCKEY)
    container_client = blob_service_client.get_container_client(CONTAINER)
    return container_client

def saveCSVAzure(df, name, container_client):
    output = df.to_csv(index=False, encoding="utf-8")
    blob_client = container_client.get_blob_client(name)
    blob_client.upload_blob(output, blob_type="BlockBlob", overwrite=True)

def getStudent(KEY, df, config):
    URL = "https://ead.logschool.com.br/api/1/student"
    

    for i in range(0, 1000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        df = pd.concat([df_tmp, df])

    container_client = getAzureAccess(config)
    saveCSVAzure(df, "logschool_student.csv", container_client)

def getPermission(KEY, df, config):
    URL = "https://ead.logschool.com.br/api/1/permission"
    

    for i in range(0, 1000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        df = pd.concat([df_tmp, df])

    container_client = getAzureAccess(config)
    saveCSVAzure(df, "logschool_permission.csv", container_client)

def getUserPermission(KEY, df, config):
    URL = "https://ead.logschool.com.br/api/1/userpermission"
    

    for i in range(0, 1000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        df = pd.concat([df_tmp, df])

    container_client = getAzureAccess(config)
    saveCSVAzure(df, "logschool_userpermission.csv", container_client)

def getCategory(KEY, df, config):
    URL = "https://ead.logschool.com.br/api/1/category"
    

    for i in range(0, 1000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        df = pd.concat([df_tmp, df])

    container_client = getAzureAccess(config)
    saveCSVAzure(df, "logschool_category.csv", container_client)

def getCourse(KEY, df, config):
    URL = "https://ead.logschool.com.br/api/1/course"
    

    for i in range(0, 1000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        df = pd.concat([df_tmp, df])

    container_client = getAzureAccess(config)
    saveCSVAzure(df, "logschool_course.csv", container_client)

def getModule(KEY, df, config):
    URL = "https://ead.logschool.com.br/api/1/module"
    

    for i in range(0, 1000, 1000):
        params = {
            "offset": f"{i}"
        }
        df_tmp  = apiAccess(KEY, URL, params)
        df = pd.concat([df_tmp, df])

    container_client = getAzureAccess(config)
    saveCSVAzure(df, "logschool_module.csv", container_client)

def main():

    config = configparser.ConfigParser()
    config.read("credentials.ini")

    KEY = config["API"]["KEY"]
    df = pd.DataFrame()
    
    getStudent(KEY, df, config)
    getPermission(KEY, df, config)
    getUserPermission(KEY, df, config)
    getCategory(KEY, df, config)
    getCourse(KEY, df, config)
    getModule(KEY, df, config)
    
        

if __name__ == "__main__":
    main()