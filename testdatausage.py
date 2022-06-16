import paho.mqtt.client as mqttClient
import csv
import requests
import time
from datetime import datetime

BLYNK_DEVICE_NAME = "H001"

hostname = "test.mosquitto.org"
topic_name = "esp"

client = mqttClient.Client("Alpha1")
print(client.connect(hostname, keepalive=300))


for i in range(86400):
    print(i)
    print(client.publish(topic_name,"[69"\
                      + ","\
                      + BLYNK_DEVICE_NAME \
                      + ","
                      + str(int(time.time())) \
                      + ",54.2"\
                      + ",-10"\
                      + ",50.0"\
                      + ",33.3"\
                      + ",33.3"\
                      + ",33.3"\
                      + ",1"\
                      + ",1"\
                      + ",4.43"\
                      + ",1"\
                      + ",4.42"\
                      + ",13]",qos=0))
#     print(requests.post("http://api.alphaelectrics.app/logging",
#                         data={"id": "001"
#                       ,"loc": BLYNK_DEVICE_NAME
#                       ,"ts": str(int(time.time()))
#                       ,"v": 0
#                       ,"c": 1 
#                       ,"p": 2
#                       ,"t1": 3 
#                       ,"t2": 4  
#                       ,"t3": 5
#                       ,"cm": 6  
#                       ,"dm": 7  
#                       ,"mxcvn": 8  
#                       ,"mxcv": 9  
#                       ,"mncvn": 10  
#                       ,"mncv": 11}).text)