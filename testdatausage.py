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


for i in range(86400):
    print(client.publish(topic_name,"{id: 69"\
                      + ",loc: "\
                      + BLYNK_DEVICE_NAME \
                      + ",ts: "
                      + str(int(time.time())) \
                      + ",v: 0"\
                      + ",c: 1"\
                      + ",p: 100"\
                      + ",t1: 3"\
                      + ",t2: 4"\
                      + ",t3: 5"\
                      + ",cm: 6"\
                      + ",dm: 7"\
                      + ",mxcvn: 8"\
                      + ",mxcv: 9"\
                      + ",mncvn: 10"\
                      + ",mncv: 11}"))
#     print(requests.post("http://api.alphaelectrics.co/logging",
#                         data={"battery_id": 69
#                       ,"location": BLYNK_DEVICE_NAME
#                       ,"timestamp": time.time()
#                       ,"voltage": 0
#                       ,"current": 1
#                       ,"percentage": 100
#                       ,"temp1": 3  
#                       ,"temp2": 4  
#                       ,"temp3": 5 
#                       ,"Chargemos": 6  
#                       ,"Dischargemos": 7  
#                       ,"MaxCellVnum": 8 
#                       ,"MaxCellV": 9  
#                       ,"minCellVNum": 10  
#                       ,"minCellV": 11}).text)