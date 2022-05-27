# ESP-SBC
This repo contains the code to be uploaded to the SBC on the Alpha Hive/Buggy. The SBC acts as a hotspot and broadcast both BLE and WiFi at the same time, with the SSID of the WiFi being hidden. A MQTT server is also being run on the SBC upon start up, which would receive battery data from the ESP32 once the connection is established.

## Overview of send_csv.py
This python script soley attempts to upload the csv file onto the server and then delete the files from the RPi once the upload is successful. This script is run using crontab twice a day at 1230 and 1830.

## Overview of simplesub.py
This python script listens to the MQTT server and saves incoming data from the ESP32 on the batteries into their separate csv files. It also uploads the code onto the Blynk server if internet connection is available which allows live streaming of data.

## Overview of BLEPub
This folder contains the code which allows the bluetooth on the RPi to function as a Bluetooth Low Energy device, which allows it to be detected by the EPS32 BLEScan function.
