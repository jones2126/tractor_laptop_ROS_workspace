#!/usr/bin/python
import time
import serial
#    "/dev/ttyUSB0",
port =serial.Serial(
    "/dev/ttyUSB0",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout = 0,
    timeout = 10)
# $serial->sendMessage("\xFF\x01\x01");
#data=bytes([0xFF,0x01,0x01]) # on
print("Port opened?") 
print(port.isOpen()) 
print("Sending Data - on")
port.write("\xFF\x01\x01")
#port.write(data) 
print("Data Sent")
time.sleep(3)
#data=bytes([0xFF,0x01,0x00]) # off
print("Sending Data - off")
port.write("\xFF\x01\x01")
#port.write(data) 
print("Data Sent")
print("EOJ")
