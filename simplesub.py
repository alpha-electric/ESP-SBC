import paho.mqtt.client as mqttClient
import csv
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("/home/pi/ESP-SBC/iot.env")
load_dotenv(dotenv_path = dotenv_path)


LIVEDATADELAY = 30
battery_dict = {}



def send_backend(received_data):
    print(requests.post(LOGGING_URL,
                        data={"id": received_data[0]
                      ,"loc": LOCATION
                      ,"ts": time.time()
                      ,"v": received_data[1] 
                      ,"c": received_data[2]  
                      ,"p": received_data[3]  
                      ,"t1": received_data[4]  
                      ,"t2": received_data[5]  
                      ,"t3": received_data[6]  
                      ,"cm": received_data[7]  
                      ,"dm": received_data[8]  
                      ,"mxcvn": received_data[9]  
                      ,"mxcv": received_data[10]  
                      ,"mncvn": received_data[11]  
                      ,"mncv": received_data[12]}).text)


def on_message(client, userdata, message):
    #receive the message and make file if doesnt exist
    received_data = str(message.payload.decode("utf-8"))
    received_data = received_data.split(",")
    
    batt_name = received_data[0]
    
    file_name = DATA_DIR + batt_name + "-" + LOCATION + ".csv"
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
    
    print("data came in")
    
    if battery_dict.get(batt_name) == None:
        battery_dict[batt_name] = time.time()
        print("created new battery")
        send_backend(received_data)
    elif time.time() - battery_dict[batt_name] >= LIVEDATADELAY:
        send_backend(received_data)
        print("sending live data")
        battery_dict[batt_name] = time.time()


hostname = "192.168.30.50"
topic_name = "esp32/output"

client = mqttClient.Client("Alpha1")
client.connect(hostname)
client.loop_start()
client.subscribe(topic_name)
client.on_message = on_message

while True:
    pass
    

