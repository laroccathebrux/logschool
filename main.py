import requests
import configparser

config = configparser.ConfigParser()
config.read("credentials.ini")

KEY = config["API"]["KEY"]
URL = "https://ead.logschool.com.br/api/1/student"

headers = {"Accept": "application/json", "Token": KEY}

r = requests.get(url=URL, headers=headers)

print(r.content)