import requests
import os
from os import listdir


Dir = "/home/pi/DataFiles"

FileList = listdir(Dir)
url = "http://api.alphaelectrics.app/csv"

for i in FileList:
    tries = 0
    while tries < 5:
        try:
            file = {'file': open(Dir + "/" + i, "rb")}
            r = requests.post(url, files=file)
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
        




