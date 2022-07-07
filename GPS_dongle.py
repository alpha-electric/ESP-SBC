import serial
import time
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("/home/pi/ESP-SBC/iot.env")
load_dotenv(dotenv_path = dotenv_path)

LOCATION = os.getenv("LOCATION")
RPI_NAME = os.getenv("RPI_NAME")

gps_disconnected = True
gps_setup = False
GPSDELAY = 5
GPS_LOGGING_URL = "http://api.alphaelectrics.app/gps/"
# TESTING_URL = "http://httpbin.org/post"

def check_gps_dongle():
	global ser, gps_disconnected
	try:
		ser = serial.Serial('/dev/ttyUSB2',115200)
		ser.flushInput()
		gps_disconnected = False
		return True
		
	except Exception as e:
		print(e)
		gps_disconnected = True
		return False # Dongle not connected

def setup_gps():
	global gps_setup
	gps_setup = True
	answer = 0
	print('Start GPS session...')
	rec_buff = ''
	send_at('AT+CGPS=1','OK',1)
	time.sleep(2)

# Helper code to send AT command
def send_at(command,back,timeout):
	rec_buff = ''
	ser.write((command+'\r\n').encode())
	time.sleep(timeout)
	if ser.inWaiting():
		time.sleep(0.1)
		rec_buff = ser.read(ser.inWaiting())
	if rec_buff != '':
		if back not in rec_buff.decode():
			print(command + ' ERROR')
			print(command + ' back:\t' + rec_buff.decode())
			return 0
		else:
			### For checking serial output
			# print(rec_buff.decode())
			
			### For human readable data
			global GPSDATA, FinalLat, FinalLong, speed
			GPSDATA = str(rec_buff.decode())
			cleaned = GPSDATA[25:]
			try:
				full_lat, NS, full_long, EW, date, UTC_time, alt, speed, course= cleaned.split(",")
				# print(cleaned)
				# print(full_lat, NS, full_long, EW, date, UTC_time, alt, speed, course)
				
				Lat = full_lat[:2]
				SmallLat = full_lat[2:]
				
				Long = full_long[:3]
				SmallLong = full_long[3:]
				
				FinalLat = "{:.5f}".format(float(Lat) + (float(SmallLat)/60))
				FinalLong = "{:.5f}".format(float(Long) + (float(SmallLong)/60))
				
				if NS == 'S' : FinalLat = -FinalLat
				if EW == 'W' : FinalLong = -FinalLong
				
				print(FinalLat, FinalLong, speed)
				return 1
				
			except:
				print("Received data: {}".format(cleaned))
				print("GPS not ready")
				return 0
	else:
		print('GPS is not ready')
		return 0

def get_gps_position():
	rec_buff = ''
	answer = send_at('AT+CGPSINFO','+CGPSINFO: ',1)
	if 1 == answer:
		answer = 0
		if ',,,,,,' in rec_buff:
			print('GPS is not ready')
			time.sleep(1)
	else:
		print('error %d'%answer)
		rec_buff = ''
		# send_at('AT+CGPS=0','OK',1)
		
def send_gps_backend():
    gps_url = GPS_LOGGING_URL +  str(FinalLat) + ',' + str(FinalLong) + ',' + str(speed) + ',' + str(LOCATION)
    print(gps_url) # for debugging
    print(requests.post(gps_url, headers={'Content-Type': 'text/plain'}).text)
    """print(requests.post(GPS_LOGGING_URL,
                        data=str(FinalLat) +
                      "," + str(FinalLong) +
                      "," + str(speed),headers={'Content-Type': 'text/plain'}).text) """


### Main code
while True:
	try:
		while (gps_disconnected == True):
			print("Retrying connection to dongle")
			check_gps_dongle()

		
		if (gps_setup == False):
			setup_gps()
		
		get_gps_position()
		send_gps_backend()
	except Exception as e:
		print(e)
		print("GPS disconnected")
		gps_disconnected = True
		gps_setup = False
		time.sleep(10)
		
	time.sleep(GPSDELAY) # send gps pos every 5 seconds
