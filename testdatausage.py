import paho.mqtt.client as mqttClient
import csv
import struct
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("/home/pi/ESP-SBC/iot.env")
load_dotenv(dotenv_path = dotenv_path)

# locid = 100

hostname = "test.mosquitto.org"
topic_name = "esp"


# def on_message(client, userdata, message):
#     print(int.from_bytes(message.payload[0:2], byteorder = "big", signed = False)) #batt id 
#     print(chr(int.from_bytes(message.payload[2:3], byteorder = "big", signed = False))) #location char
#     print(int.from_bytes(message.payload[3:5], byteorder = "big", signed = False)) #location number
#     print(int.from_bytes(message.payload[5:9], byteorder = "big", signed = False)) #timestamp
#     print(struct.unpack("f",message.payload[9:13])) #voltage
#     print(struct.unpack("f",message.payload[13:17])) #current
#     print(struct.unpack("f",message.payload[17:21])) #percentage
#     print(struct.unpack("f",message.payload[21:25])) #t1
#     print(struct.unpack("f",message.payload[25:29])) #t2
#     print(struct.unpack("f",message.payload[29:33])) #t3
#     print(int.from_bytes(message.payload[33:34], byteorder = "big", signed = False)) #cm
#     print(int.from_bytes(message.payload[34:35], byteorder = "big", signed = False)) #dm
#     print(struct.unpack("f",message.payload[35:39])) #mxcv
#     print(int.from_bytes(message.payload[39:40], byteorder = "big", signed = False)) #mxcvn
#     print(struct.unpack("f",message.payload[40:44])) #mncv
#     print(int.from_bytes(message.payload[44:45], byteorder = "big", signed = False)) #mncvn
    


# client = mqttClient.Client("Alpha1")
# client2 = mqttClient.Client("Alpha2")
# print(client2.connect(hostname, keepalive=300))
# print(client.connect(hostname, keepalive=300))
# client2.loop_start()
# client2.subscribe(topic_name)
# client2.on_message = on_message

# for i in range(86400):
#     identity = 69
#     tosend = bytearray()
#     tosend += bytearray(identity.to_bytes(2,byteorder='big',signed=False))
#     tosend += bytearray([ord("h")])
#     tosend += bytearray(locid.to_bytes(2,byteorder='big',signed=False))
#     tosend += bytearray(int(time.time()).to_bytes(4,byteorder='big',signed=False))
#     tosend += bytearray(struct.pack("f",54.2))
#     tosend += bytearray(struct.pack("f",-50.0))
#     tosend += bytearray(struct.pack("f",50.0))
#     tosend += bytearray(struct.pack("f",33.3))
#     tosend += bytearray(struct.pack("f",33.3))
#     tosend += bytearray(struct.pack("f",33.3))
#     tosend += bytearray([1])
#     tosend += bytearray([1])
#     tosend += bytearray(struct.pack("f",4.43))
#     tosend += bytearray([1])
#     tosend += bytearray(struct.pack("f",4.40))
#     tosend += bytearray([13])
#     print(client.publish(topic_name,tosend,qos=0))


# for i in range(86400):
#     print(i)
#     print(client.publish(topic_name,"[69"\
#                       + ","\
#                       + BLYNK_DEVICE_NAME \
#                       + ","
#                       + str(int(time.time())) \
#                       + ",54.2"\
#                       + ",-10"\
#                       + ",50.0"\
#                       + ",33.3"\
#                       + ",33.3"\
#                       + ",33.3"\
#                       + ",1"\
#                       + ",1"\
#                       + ",4.43"\
#                       + ",1"\
#                       + ",4.42"\
#                       + ",13]",qos=0))
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
print(requests.post(LOGGING_URL,
                        data=str(received_data[0]) +
                      "," + LOCATION +
                      "," + str(int(time.time())) +
                      "," + str(received_data[1]) +
                      "," + str(received_data[2]) + 
                      "," + str(received_data[3]) +
                      "," + str(received_data[4]) + 
                      "," + str(received_data[5]) + 
                      "," + str(received_data[6]) + 
                      "," + str(received_data[7]) + 
                      "," + str(received_data[8]) + 
                      "," + str(received_data[9]) + 
                      "," + str(received_data[10]) +
                      "," + str(received_data[11]) + 
                      "," + str(received_data[12])).text)