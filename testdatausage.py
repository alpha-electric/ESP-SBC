import paho.mqtt.client as mqttClient
import csv
import requests
import time
from datetime import datetime

BLYNK_DEVICE_NAME = "Hive 001"

hostname = "test.mosquitto.org"
topic_name = "topkek"

client = mqttClient.Client("Alpha1")
print(client.connect(hostname))


for i in range(3600):
    print(i)
#     print(client.publish(topic_name,"{id: 69"\
#                       + ",loc: "\
#                       + BLYNK_DEVICE_NAME \
#                       + ",ts: "
#                       + str(int(time.time())) \
#                       + ",v: 0"\
#                       + ",c: 1"\
#                       + ",p: 100"\
#                       + ",t1: 3"\
#                       + ",t2: 4"\
#                       + ",t3: 5"\
#                       + ",cm: 6"\
#                       + ",dm: 7"\
#                       + ",mxcvn: 8"\
#                       + ",mxcv: 9"\
#                       + ",mncvn: 10"\
#                       + ",mncv: 11}"))
    print(requests.post("http://api.alphaelectrics.co/logging",
                        data={"id": "9juntest"
                      ,"loc": BLYNK_DEVICE_NAME
                      ,"ts": str(int(time.time()))
                      ,"v": 0
                      ,"c": 1 
                      ,"p": 2
                      ,"t1": 3 
                      ,"t2": 4  
                      ,"t3": 5
                      ,"cm": 6  
                      ,"dm": 7  
                      ,"mxcvn": 8  
                      ,"mxcv": 9  
                      ,"mncvn": 10  
                      ,"mncv": 11}).text)