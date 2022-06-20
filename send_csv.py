import requests
import os
from os import listdir
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("/home/pi/ESP-SBC/iot.env")
load_dotenv(dotenv_path = dotenv_path)

LOGGING_URL = os.getenv("LOGGING_URL")
LOCATION = os.getenv("LOCATION")
CSV_URL = os.getenv("CSV_URL")
DATA_DIR = os.getenv("DATA_DIR")
RPI_NAME = os.getenv("RPI_NAME")

FileList = listdir(DATA_DIR)

for i in FileList:
    tries = 0
    while tries < 5:
        try:
            file = {'file': open(DATA_DIR + "/" + i, "rb")}
            r = requests.post(CSV_URL, files=file)
            print(r.status_code)
            print(r.text)
            if r.status_code == 200:
                os.remove(Dir + "/" + i)
                break
            else:
                tries += 1
                print("failed to send files")
        except:
            print("no internet connection")
        




