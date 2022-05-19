import paho.mqtt.client as mqttClient
import csv
import requests

def on_message(client, userdata, message):
	global recieved_data
	recieved_data = str(message.payload.decode("utf-8"))
	print("message received", recieved_data)
	
	csv_writer.writerow([recieved_data])
	my_data_file.flush()
	# info = "{\"Recieved_data\":" + str(1) + "}"
	# print(info)
	# r = requests.post("http://18.140.68.118/logging", data=info, headers={"Content-Type":"text/plain"})
	# print(r.status_code)
	# print(r.reason)
	# print(r.text)

hostname = "192.168.30.50"
topic_name = "esp32/output"
file_name = "/home/pi/testing.csv"

client = mqttClient.Client("Alpha1")
client.connect(hostname)
client.loop_start()
client.subscribe(topic_name)

my_data_file = open(file_name, 'w')
csv_writer = csv.writer(my_data_file, delimiter=',')

while True:
	client.on_message = on_message
	
