import paho.mqtt.client as mqttClient
import csv
import requests
import time
from datetime import datetime

BLYNK_TEMPLATE_ID = "TMPLhNGEvK6P"
BLYNK_DEVICE_NAME = "Alpha Buggy 1"
BLYNK_AUTH_TOKEN = "ouV8pw6v719r6S-c3ru5MBi8bGYR_UYt"

BatteryList = ["",""]
global Batt1timer
global Batt1timedout
Batt1timedout = False
Batt1timer = time.time()
Batt1timeout = 15
global Batt2timer
global Batt2timedout
Batt2timedout = False
Batt2timer = time.time()
Batt2timeout = 15

def send_blynk(batt, received_data, refresh = True):
    global Batt1timer
    global Batt2timer
    global Batt1timedout
    global Batt2timedout
    try:
        print(requests.get("https://sgp1.blynk.cloud/external/api/update?token=" + BLYNK_AUTH_TOKEN + "&v14=1").text)
        if batt == 1:
            Batt1timer = time.time()
            Batt1timedout = False
            print(requests.get("https://sgp1.blynk.cloud/external/api/batch/update?token=" + BLYNK_AUTH_TOKEN + "&v6=" + received_data[0] + "&v7=" + received_data[1] + "&v8=" + received_data[2] + "&v9=" + received_data[3] + "&v10=" + received_data[4] + "&v11=" + received_data[5] + "&v12=" + received_data[6]).text)
            print("updated batt 1")
        elif batt == 2:
            Batt2timer = time.time()
            Batt2timedout = False
            print(requests.get("https://sgp1.blynk.cloud/external/api/batch/update?token=" + BLYNK_AUTH_TOKEN + "&v13=" + received_data[0] + "&v0=" + received_data[1] + "&v1=" + received_data[2] + "&v2=" + received_data[3] + "&v3=" + received_data[4] + "&v4=" + received_data[5] + "&v5=" + received_data[6]).text)
            print("updated batt 2")
    except:
        print("No internet connection")

def on_message(client, userdata, message):
    #receive the message and make file if doesnt exist
    received_data = str(message.payload.decode("utf-8"))
    received_data = received_data.split(",")
    file_name = "/home/pi/DataFiles/" + received_data[0] + ".csv"
    try:
        my_data_file = open(file_name, 'x')
        csv_writer = csv.writer(my_data_file, delimiter=',')
        csv_writer.writerow(["timestamp","voltage","current","percentage","temp1","temp2","temp3","chargemos","dischargemos","MaxCellVNum","MaxCellV","MinCellVNum","MinCellV"])
    except:
        print("file already exists")
        
    #open file to append data
    my_data_file = open(file_name, 'a')
    csv_writer = csv.writer(my_data_file, delimiter=',')
    csv_data = [datetime.now().strftime('%d-%b-%Y, %H:%M:%S')] + received_data[1:]
    print("message received", csv_data)
    csv_writer.writerow(csv_data)
    my_data_file.flush()
    my_data_file.close()
    
    #if battery already accounted for in battery list, send to blynk and refresh timer
    if received_data[0] in BatteryList:
        print("batt already here")
        if BatteryList.index(received_data[0]) == 0:
            send_blynk(1,received_data)
        else:
            send_blynk(2,received_data)
    
    #if battery does not exist, check if battery list has space, otherwise remove the most outdated battery
    else:
        try:
            print("entering add new batt")
            emptyindex = BatteryList.index("")
            if emptyindex == 0:
                BatteryList[0] = received_data[0]
                send_blynk(1,received_data)
            elif emptyindex == 1:
                print("adding battery 2")
                BatteryList[1] = received_data[0]
                send_blynk(2,received_data)
        except:                
            if Batt2timer > Batt1timer:
                BatteryList[0] = received_data[0]
                send_blynk(1,received_data)
            else:
                BatteryList[1] = received_data[0]
                send_blynk(2,received_data)
        
    
    # info = "{\"received_data\":" + str(1) + "}"
    # print(info)
    # r = requests.post("http://18.140.68.118/logging", data=info, headers={"Content-Type":"text/plain"})
    # print(r.status_code)
    # print(r.reason)
    # print(r.text)

hostname = "192.168.30.50"
topic_name = "esp32/output"

client = mqttClient.Client("Alpha1")
client.connect(hostname)
client.loop_start()
client.subscribe(topic_name)
client.on_message = on_message

while True:
    if Batt1timedout == False and time.time() - Batt1timer >= Batt1timeout:
        Batt1timedout = True
        BatteryList[0] = ""
    if Batt2timedout == False and time.time() - Batt2timer >= Batt2timeout:
        Batt2timedout = True
        BatteryList[1] = ""