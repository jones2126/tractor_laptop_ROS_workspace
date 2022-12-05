import serial
ser = serial.Serial('/dev/gps', 115200)

while True:
    data = ser.readline()
    if data:
        print(data)